"""
provider.py

This module defines the OAuth2Provider base class for the django-graphene-jwt-oauth2 library, 
providing the structure and required methods for specific OAuth2 providers.

Classes:
- OAuth2Provider: Base class for implementing OAuth2 providers.

Functions:
- None

Variables:
- None
"""

from typing import Any, Dict, Optional, Tuple

from django.http import HttpRequest, HttpResponse


class OAuth2Provider:
    """
    Base class for OAuth2 providers.

    This class outlines the necessary methods and attributes for OAuth2 providers.
    It acts as a template for specific provider implementations.

    Attributes:
    |   client_id (str): The OAuth2 client ID.
    |   client_secret (str): The OAuth2 client secret.
    |   name (str): The name of the OAuth2 provider.
    |   scope (str): The scope of the initial token request.
    |   config (dict): Configuration for URLs used in the OAuth2 flow.
    |   timeout (int): The timeout in seconds for the requests.

    Methods:
    |   __init__(config: Dict[str, str]): Initializes the OAuth2Provider instance.
    |   get_callback_url(request: HttpRequest) -> str: Method to build the callback URL
        for OAuth2 authorization.
    |   get_authorization_url(request: HttpRequest, state: Dict) -> str: Method to build
        the OAuth2 authorization URL.
    |   get_oauth2_token(code: str, request: HttpRequest) -> Tuple[Optional[Dict[str, Any]],
        Optional[HttpResponse]]: Method to retrieve the OAuth2 token.
    |   fetch_profile(access_token: str) -> Optional[Dict[str, Any]]: Method to fetch the
        user profile.
    |   extract_profile(profile: Dict[str, Any]) -> Dict[str, Any]: Method to extract user
        data from the profile.
    """

    timeout = 10

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        scope: Optional[str] = None,
        config: Optional[Dict] = None,
        timeout: Optional[int] = None,
    ):
        self.client_id = client_id or self.client_id
        self.client_secret = client_secret or self.client_secret
        self.scope = scope or self.scope
        self.timeout = timeout or self.timeout
        self.config = config or self.config

    def get_callback_url(self, request: HttpRequest) -> str:
        """
        Builds the OAuth2 authorization URL using Django's HttpRequest object.

        :param request: HttpRequest object.

        :return: The absolute URI for OAuth2 authorization.
        """
        raise NotImplementedError("Subclasses must implement this method")

    def get_authorization_url(self, request: HttpRequest, encoded_state: Dict) -> str:
        """
        Builds the OAuth2 authorization URL for the provider.

        :param request: HttpRequest object.

        :return: The absolute URI for OAuth2 authorization.
        """
        raise NotImplementedError("Subclasses must implement this method")

    def get_oauth2_token(
        self, code: str, request: HttpRequest
    ) -> Tuple[Optional[Dict[str, Any]], Optional[HttpResponse]]:
        """
        Retrieves the OAuth2 token from the provider.

        :param code: Authorization code received from the OAuth provider.
        :param scope: Scope of the access request.
        :param redirect_uri: Redirect URI after authorization.

        :return: A tuple of the token response content and an error HttpResponse if any.
        """
        raise NotImplementedError("Subclasses must implement this method")

    def fetch_profile(self, access_token: str) -> Optional[dict]:
        """
        Fetches the user profile from the provider using the access token.

        :param access_token: Access token for authenticating the request.

        :return: User profile information as a dictionary, or None in case of an error.
        """
        raise NotImplementedError("Subclasses must implement this method")

    def extract_profile(self, profile: dict) -> dict:
        """
        Extracts essential user data from the profile information.

        :param profile: Dictionary containing the user profile information.

        :return: Dictionary with extracted user data.
        """
        raise NotImplementedError("Subclasses must implement this method")
