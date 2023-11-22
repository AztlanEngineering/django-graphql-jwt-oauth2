"""
state_manager.py

This module defines the OAuth2StateManager class for managing the state in OAuth2 authentication
processes in the django-graphene-jwt-oauth2 library. This includes encoding and decoding state
information.

Classes:
- OAuth2StateManager: Manages state during OAuth2 authentication.

Functions:
- None

Variables:
- None
"""

from typing import Any, Dict, Optional

import jwt
from django.conf import settings


class OAuth2StateManager:
    """
    This class handles the state of OAuth2 authentication processes by encoding and decoding state
    information using JWT tokens.

    Attributes:
        payload (Optional[Dict[str, Any]]): The payload to be encoded or decoded.
        encoded_state (Optional[str]): The encoded state string.

    Methods:
        __init__(**kwargs): Initializes the OAuth2StateManager instance with optional payload or
        encoded state.
    """

    def __init__(self, **kwargs: Any) -> None:
        self.payload: Optional[Dict[str, Any]] = kwargs.pop("payload", None)
        self.encoded_state: Optional[str] = kwargs.pop("encoded_state", None)

        if self.encoded_state:
            self.payload = jwt.decode(
                self.encoded_state, settings.SECRET_KEY, algorithms=["HS256"], **kwargs
            )

        if self.payload:
            self.encoded_state = jwt.encode(
                self.payload, settings.SECRET_KEY, algorithm="HS256"
            )
