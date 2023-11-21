# src package

## Subpackages

* [src.providers package](src.providers.md)
  * [Submodules](src.providers.md#submodules)
  * [src.providers.google module](src.providers.md#src-providers-google-module)
  * [Module contents](src.providers.md#module-src.providers)

## Submodules

## src.constants module

## src.decorators module

## src.errors module

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

### *exception* src.errors.ObscureException(message: str = 'Unauthorized')

Bases: `Exception`

Custom exception class with an optional message.

This exception class is designed to obscure error details in non-debug mode,
providing a generic error message.

* **Parameters:**
  **message** – The exception message.

### src.errors.ObscureHttpResponse(reason: str = 'Unauthorized', code: int = 401)

Create an HTTP response with the provided reason and status code or defaults,
obscuring the error details in non-debug mode.

* **Parameters:**
  * **reason** – The reason for the HTTP response.
  * **code** – The HTTP status code.
* **Returns:**
  The HTTP response with obscured details.

## src.jwt_helpers module

## src.provider module

provider.py

This module defines the OAuth2Provider base class for the django-graphene-jwt-oauth2 library, 
providing the structure and required methods for specific OAuth2 providers.

Classes:
- OAuth2Provider: Base class for implementing OAuth2 providers.

Functions:
- None

Variables:
- None

### *class* src.provider.OAuth2Provider(client_id: str | None = None, client_secret: str | None = None, scope: str | None = None, config: Dict | None = None, timeout: int | None = None)

Bases: `object`

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
|   \_\_init_\_(config: Dict[str, str]): Initializes the OAuth2Provider instance.
|   get_callback_url(request: HttpRequest) -> str: Method to build the callback URL

> for OAuth2 authorization.
get_authorization_url(request: HttpRequest, state: Dict) -> str: Method to build
the OAuth2 authorization URL.
<br/>
get_oauth2_token(code: str, request: HttpRequest) -> Tuple[Optional[Dict[str, Any]],
Optional[HttpResponse]]: Method to retrieve the OAuth2 token.
<br/>
fetch_profile(access_token: str) -> Optional[Dict[str, Any]]: Method to fetch the
user profile.
<br/>
extract_profile(profile: Dict[str, Any]) -> Dict[str, Any]: Method to extract user
data from the profile.
<br/>

#### extract_profile(profile: dict)

Extracts essential user data from the profile information.

* **Parameters:**
  **profile** – Dictionary containing the user profile information.
* **Returns:**
  Dictionary with extracted user data.

#### fetch_profile(access_token: str)

Fetches the user profile from the provider using the access token.

* **Parameters:**
  **access_token** – Access token for authenticating the request.
* **Returns:**
  User profile information as a dictionary, or None in case of an error.

#### get_authorization_url(request: HttpRequest, encoded_state: Dict)

Builds the OAuth2 authorization URL for the provider.

* **Parameters:**
  **request** – HttpRequest object.
* **Returns:**
  The absolute URI for OAuth2 authorization.

#### get_callback_url(request: HttpRequest)

Builds the OAuth2 authorization URL using Django’s HttpRequest object.

* **Parameters:**
  **request** – HttpRequest object.
* **Returns:**
  The absolute URI for OAuth2 authorization.

#### get_oauth2_token(code: str, request: HttpRequest)

Retrieves the OAuth2 token from the provider.

* **Parameters:**
  * **code** – Authorization code received from the OAuth provider.
  * **scope** – Scope of the access request.
  * **redirect_uri** – Redirect URI after authorization.
* **Returns:**
  A tuple of the token response content and an error HttpResponse if any.

#### timeout *= 10*

## src.queries module

## src.state_manager module

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

### *class* src.state_manager.OAuth2StateManager(\*\*kwargs: Any)

Bases: `object`

This class handles the state of OAuth2 authentication processes by encoding and decoding state
information using JWT tokens.

Attributes:
: payload (Optional[Dict[str, Any]]): The payload to be encoded or decoded.
  encoded_state (Optional[str]): The encoded state string.

Methods:
: \_\_init_\_(
  <br/>
  ```
  **
  ```
  <br/>
  kwargs): Initializes the OAuth2StateManager instance with optional payload or
  encoded state.

## Module contents
