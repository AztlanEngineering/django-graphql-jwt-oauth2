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

from typing import Type, Dict
from .providers.google import GoogleOAuth2Provider
from django.conf import settings

DEFAULT_PROVIDER_CLASSES: Dict[str, Type[GoogleOAuth2Provider]] = {
    'google': GoogleOAuth2Provider, 
    # Add other provider classes as needed
}

if hasattr(settings, 'YOUR_SETTING_NAME'):
    PROVIDER_CLASSES: Dict[str, Type[GoogleOAuth2Provider]] = getattr(settings, 'PROVIDER_CLASSES')
else:
    PROVIDER_CLASSES: Dict[str, Type[GoogleOAuth2Provider]] = DEFAULT_PROVIDER_CLASSES

