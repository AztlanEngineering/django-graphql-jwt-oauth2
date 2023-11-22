# graphql_jwt_oauth2.providers package

## Submodules

## graphql_jwt_oauth2.providers.google module

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

### *class* graphql_jwt_oauth2.providers.google.GoogleOAuth2Provider(client_id: str | None = None, client_secret: str | None = None, scope: str | None = None, config: Dict | None = None, timeout: int | None = None)

Bases: [`OAuth2Provider`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.provider.OAuth2Provider)

OAuth2 provider for Google.

This class provides methods for OAuth2 authentication flow, including
building authorization URLs, retrieving tokens, fetching user profiles,
and extracting user data for Google.

Attributes:
: client_id (str): The OAuth2 client ID for Google.
  client_secret (str): The OAuth2 client secret for Google.
  name (str): Name of the provider.
  scope (str): The scope of the initial token request.
  config (dict): Configuration for URLs used in the OAuth2 flow.

#### client_id *= None*

#### client_secret *= None*

#### config *= {'AUTHORIZATION_URL': 'https://accounts.google.com/o/oauth2/v2/auth', 'PROFILE_URL': 'https://www.googleapis.com/oauth2/v3/userinfo', 'TOKEN_URL': 'https://oauth2.googleapis.com/token'}*

#### extract_profile(profile: dict)

Extracts essential user data from the Google user profile information.

* **Parameters:**
  **profile** – Dictionary containing the Google user profile information.
* **Returns:**
  Dictionary with extracted user data.

#### fetch_profile(access_token: str)

Fetches the user profile from Google using the access token.

* **Parameters:**
  **access_token** – Access token for authenticating the request.
* **Returns:**
  User profile information as a dictionary, or None in case of an error.

#### get_authorization_url(request: HttpRequest, encoded_state: str)

Builds the OAuth2 authorization URL for Google.

* **Parameters:**
  **request** – HttpRequest object.
* **Returns:**
  The absolute URI for OAuth2 authorization.

#### get_callback_url(request: HttpRequest)

Builds the OAuth2 authorization URL for Google using Django’s HttpRequest object.

* **Parameters:**
  **request** – HttpRequest object.
* **Returns:**
  The absolute URI for OAuth2 authorization.

#### get_oauth2_token(code: str, request: HttpRequest)

Retrieves the OAuth2 token from Google.

* **Parameters:**
  * **code** – Authorization code received from the OAuth provider.
  * **scope** – Scope of the access request.
  * **redirect_uri** – Redirect URI after authorization.
* **Returns:**
  A tuple of the token response content and an error HttpResponse if any.

#### name *= 'google'*

#### scope *= 'openid email profile'*

## Module contents
