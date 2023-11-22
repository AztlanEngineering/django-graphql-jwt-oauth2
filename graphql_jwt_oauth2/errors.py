"""
errors.py

This module defines custom error handling for the django-graphene-jwt-oauth2 library, 
including a custom exception and an HttpResponse subclass to obscure error 
details in non-debug mode.

Classes:
- ObscureException: Custom exception class with an optional message.

Functions:
- ObscureHttpResponse: Function to create an HTTP response with obscured error details.

Variables:
- DEFAULT_ERROR_MESSAGE: Default error message used in non-debug mode.
- DEFAULT_STATUS_CODE: Default status code for obscured HTTP responses.
"""

from django.conf import settings
from django.http import HttpResponse

# Constants for default error message and status code
DEFAULT_ERROR_MESSAGE: str = "Unauthorized"
DEFAULT_STATUS_CODE: int = 401


def ObscureHttpResponse(  # pylint: disable=C0103
    reason: str = DEFAULT_ERROR_MESSAGE, code: int = DEFAULT_STATUS_CODE
) -> HttpResponse:
    """
    Create an HTTP response with the provided reason and status code or defaults,
    obscuring the error details in non-debug mode.

    :param reason: The reason for the HTTP response.
    :param code: The HTTP status code.
    :return: The HTTP response with obscured details.
    """
    return HttpResponse(
        reason if settings.DEBUG else DEFAULT_ERROR_MESSAGE, status=code
    )


class ObscureException(Exception):
    """
    Custom exception class with an optional message.

    This exception class is designed to obscure error details in non-debug mode,
    providing a generic error message.

    :param message: The exception message.
    """

    def __init__(self, message: str = DEFAULT_ERROR_MESSAGE):
        super().__init__(message if settings.DEBUG else DEFAULT_ERROR_MESSAGE)
