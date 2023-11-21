"""
decorators.py

This module provides decorators used in the django-graphene-jwt-oauth2 library
to handle OAuth2 callback functionality.

Functions:
- callback: A decorator to process OAuth2 callback and pass data to the decorated view function.

Classes:
- None

Variables:
- None
"""

from typing import Any, Callable

import jwt
from django.http import HttpRequest, HttpResponse
from django.middleware.csrf import rotate_token
from graphql_jwt.settings import jwt_settings

from .constants import PROVIDER_CLASSES
from .errors import ObscureHttpResponse
from .state_manager import OAuth2StateManager


def callback(view_func: Callable[..., Any]) -> Callable[..., HttpResponse]:
    """
    Decorator to process OAuth2 callback and pass data to the decorated view function.

    This decorator handles the OAuth2 callback process, validating the received code and state,
    and extracting user data from the OAuth2 provider.

    :param view_func: The view function to be decorated.
    :type view_func: Callable[..., Any]
    :return: The wrapped view function.
    :rtype: Callable[..., HttpResponse]
    """

    def wrapped_view(
        request: HttpRequest, provider: str, *args, **kwargs
    ) -> HttpResponse:
        provider_class = PROVIDER_CLASSES.get(provider)
        if not provider_class:
            return ObscureHttpResponse("Invalid OAuth2 provider")

        provider_instance = provider_class()
        code = request.GET.get("code")
        try:
            state = OAuth2StateManager(encoded_state=request.GET.get("state")).payload
        except jwt.exceptions.InvalidSignatureError:
            return ObscureHttpResponse("Invalid state or signature")

        if not code:
            return ObscureHttpResponse("Authorization code not provided")

        token_response, token_error = provider_instance.get_oauth2_token(code, request)
        if token_error:
            return ObscureHttpResponse("OAuth2 token retrieval failed", token_error)

        profile = provider_instance.fetch_profile(token_response["access_token"])
        if not profile:
            return ObscureHttpResponse("Failed to fetch user profile")

        user_data = provider_instance.extract_profile(profile)

        if jwt_settings.JWT_CSRF_ROTATION:
            rotate_token(request)

        resource = state.get("resource")

        return view_func(request, provider, user_data, state, resource, *args, **kwargs)

    return wrapped_view
