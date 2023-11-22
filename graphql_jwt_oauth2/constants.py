"""
constants.py

This module provides constants used throughout the django-graphene-jwt-oauth2 library, 
including default provider classes and settings.

Classes:
- GoogleOAuth2Provider: The OAuth2 provider class for Google.

Functions:
- None

Variables:
- DEFAULT_PROVIDER_CLASSES: A dictionary mapping provider names to their respective classes.
- PROVIDER_CLASSES: A dictionary of provider classes, customizable via Django settings.
"""

from typing import Dict, Type

from django.conf import settings

from .provider import OAuth2Provider
from .providers.google import GoogleOAuth2Provider

DEFAULT_PROVIDER_CLASSES: Dict[str, Type[OAuth2Provider]] = {
    "google": GoogleOAuth2Provider,
    # Add other provider classes as needed
}

PROVIDER_CLASSES = DEFAULT_PROVIDER_CLASSES

if hasattr(settings, "OAUTH_PROVIDER_CLASSES"):
    PROVIDER_CLASSES: Dict[str, Type[GoogleOAuth2Provider]] = getattr(
        settings, "OAUTH2_PROVIDER_CLASSES"
    )
