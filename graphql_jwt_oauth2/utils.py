"""
jwt.py

This module handles JWT (JSON Web Token) and refresh token functionalities 
for the django-graphene-jwt-oauth2 library, including token creation, 
setting cookies, and token expiration checks.

Functions:
- calculate_expiration: Calculate the expiration time for a token.
- set_cookies: Set JWT and refresh tokens as HttpOnly cookies in the HttpResponse object.
- is_refresh_token_expired: Check the expiration status of a refresh token.

Classes:
- None

Variables:
- None
"""

from datetime import datetime, timedelta
from typing import Any, Dict
from urllib.parse import parse_qs, urlencode, urlsplit, urlunsplit

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from graphql_jwt.refresh_token.shortcuts import create_refresh_token, get_refresh_token
from graphql_jwt.settings import jwt_settings
from graphql_jwt.utils import jwt_encode, jwt_payload, set_cookie


def append_query_params(
    response: HttpResponseRedirect, new_params: Dict[str, str]
) -> None:
    """
    Append additional query parameters to the URL of a HttpResponseRedirect,
    mutating it in place, preserving any existing parameters.

    :param response: HttpResponseRedirect object to be modified.
    :param new_params: Dictionary of new query parameters to append.
    """
    # Split the URL
    url_parts = list(urlsplit(response["Location"]))
    query = dict(parse_qs(url_parts[3]))

    # Update with new query parameters
    query.update(new_params)

    # Reconstruct the URL
    url_parts[3] = urlencode(query, doseq=True)
    response["Location"] = urlunsplit(url_parts)


def set_cookies(
    response: HttpResponse, user: Any, transfer_timestamps: bool = True
) -> None:
    """
    Set JWT and refresh token cookies on the HttpResponse object with CSRF rotation.

    :param response: HttpResponse object for setting cookies, headers, and CSRF rotation.
    :type response: HttpResponse
    :param user: User instance for generating JWT and refresh tokens.
    :type user: Any
    :param transfer_timestamps: Whether to append the timestamps to the response querystring.
    :type transfer_tyimestamps: bool
    """
    # JWT Token
    payload = jwt_payload(user)
    token = jwt_encode(payload)
    jwt_expires = calculate_expiration(jwt_settings.JWT_EXPIRATION_DELTA)
    set_cookie(
        response,
        jwt_settings.JWT_COOKIE_NAME,
        token,
        jwt_expires,
    )
    # Refresh Token with Model Instance
    if jwt_settings.JWT_ALLOW_REFRESH:
        refresh_token_instance = create_refresh_token(user)
        refresh_expires = calculate_expiration(
            jwt_settings.JWT_REFRESH_EXPIRATION_DELTA
        )
        set_cookie(
            response,
            jwt_settings.JWT_REFRESH_TOKEN_COOKIE_NAME,
            refresh_token_instance.get_token(),
            refresh_expires,
        )

    if transfer_timestamps:
        query_params = {
            "jwt_expires": jwt_expires.timestamp()
        }
        if jwt_settings.JWT_ALLOW_REFRESH:
            query_params["refresh_expires"] = refresh_expires.timestamp()
        append_query_params(response, query_params)


def calculate_expiration(delta: timedelta) -> datetime:
    """
    Calculate the expiration time based on the provided timedelta.

    :param delta: Timedelta for expiration.
    :type delta: timedelta
    :return: Datetime object representing the expiration time.
    :rtype: datetime
    """
    return datetime.utcnow() + delta


def is_refresh_token_expired(refresh_token: str, request: HttpRequest) -> bool:
    """
    Check if the provided refresh token is expired.

    :param refresh_token: Refresh token to be checked.
    :type refresh_token: str
    :param request: HttpRequest object.
    :type request: HttpRequest
    :return: True if the token is expired, otherwise False.
    :rtype: bool
    """
    rt_instance = get_refresh_token(refresh_token, request)
    return rt_instance.is_expired(request)
