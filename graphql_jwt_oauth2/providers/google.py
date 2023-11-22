"""
google.py

This module defines the GoogleOAuth2Provider class, a subclass of
OAuth2Provider, specifically for handling OAuth2 authentication 
with Google.

Classes:
- GoogleOAuth2Provider: Provides OAuth2 authentication functionality for Google.

Functions:
- None

Variables:
- None
"""

from typing import Any, Dict, Optional, Tuple
from urllib.parse import urlencode

import requests
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.urls import reverse

from ..errors import ObscureHttpResponse
from ..provider import OAuth2Provider


class GoogleOAuth2Provider(OAuth2Provider):
    """
    OAuth2 provider for Google.

    This class provides methods for OAuth2 authentication flow, including
    building authorization URLs, retrieving tokens, fetching user profiles,
    and extracting user data for Google.

    Attributes:
        client_id (str): The OAuth2 client ID for Google.
        client_secret (str): The OAuth2 client secret for Google.
        name (str): Name of the provider.
        scope (str): The scope of the initial token request.
        config (dict): Configuration for URLs used in the OAuth2 flow.
    """

    name = "google"  # Name of the provider
    client_id = settings.OAUTH2_CONFIG["GOOGLE"]["CLIENT_ID"]
    client_secret = settings.OAUTH2_CONFIG["GOOGLE"]["CLIENT_SECRET"]

    config = {
        "AUTHORIZATION_URL": "https://accounts.google.com/o/oauth2/v2/auth",
        "TOKEN_URL": "https://oauth2.googleapis.com/token",
        "PROFILE_URL": "https://www.googleapis.com/oauth2/v3/userinfo",
    }
    scope = "openid email profile"

    def get_callback_url(self, request: HttpRequest) -> str:
        """
        Builds the OAuth2 authorization URL for Google using Django's HttpRequest object.

        :param request: HttpRequest object.

        :return: The absolute URI for OAuth2 authorization.
        """
        local_uri = reverse("oauth2-callback", kwargs={"provider": self.name})
        return request.build_absolute_uri(local_uri)

    def get_authorization_url(self, request: HttpRequest, encoded_state: str) -> str:
        """
        Builds the OAuth2 authorization URL for Google.

        :param request: HttpRequest object.

        :return: The absolute URI for OAuth2 authorization.
        """
        # local_uri = reverse('oauth2-authorize', kwargs={'provider': self.name})
        query_params = {
            "client_id": self.client_id,
            "response_type": "code",
            "scope": " ".join(["openid", "profile", "email"]),
            "redirect_uri": self.get_callback_url(request),
            "state": encoded_state,
        }
        return f"{self.config['AUTHORIZATION_URL']}?{urlencode(query_params)}"

    def get_oauth2_token(
        self, code: str, request: HttpRequest
    ) -> Tuple[Optional[Dict[str, Any]], Optional[HttpResponse]]:
        """
        Retrieves the OAuth2 token from Google.

        :param code: Authorization code received from the OAuth provider.
        :param scope: Scope of the access request.
        :param redirect_uri: Redirect URI after authorization.

        :return: A tuple of the token response content and an error HttpResponse if any.
        """
        try:
            response = requests.post(
                self.config["TOKEN_URL"],
                data={
                    "grant_type": "authorization_code",
                    "code": code,
                    "scope": self.scope,
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                    "redirect_uri": self.get_callback_url(request),
                },
                timeout=self.timeout,
            )

            response.raise_for_status()
            return response.json(), None
        except requests.exceptions.RequestException as e:
            return None, ObscureHttpResponse(f"Error during token retrieval: {str(e)}")

    def fetch_profile(self, access_token: str) -> Optional[dict]:
        """
        Fetches the user profile from Google using the access token.

        :param access_token: Access token for authenticating the request.

        :return: User profile information as a dictionary, or None in case of an error.
        """
        try:
            response = requests.get(
                self.config["PROFILE_URL"],
                headers={"Authorization": f"Bearer {access_token}"},
                timeout=self.timeout,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None, ObscureHttpResponse(f"Error while fetching the profile")

    def extract_profile(self, profile: dict) -> dict:
        """
        Extracts essential user data from the Google user profile information.

        :param profile: Dictionary containing the Google user profile information.

        :return: Dictionary with extracted user data.
        """
        return {
            "first_name": profile.get("given_name", None),
            "last_name": profile.get("family_name", None),
            "username": profile.get("email"),
            "email": profile.get("email"),
            "profile_picture": profile.get("profile", None),
        }
