# graphql_jwt_oauth2 package

## Subpackages

* [graphql_jwt_oauth2.providers package](graphql_jwt_oauth2.providers.md)
  * [Submodules](graphql_jwt_oauth2.providers.md#submodules)
  * [graphql_jwt_oauth2.providers.google module](graphql_jwt_oauth2.providers.md#module-graphql_jwt_oauth2.providers.google)
    * [`GoogleOAuth2Provider`](graphql_jwt_oauth2.providers.md#graphql_jwt_oauth2.providers.google.GoogleOAuth2Provider)
      * [`GoogleOAuth2Provider.client_id`](graphql_jwt_oauth2.providers.md#graphql_jwt_oauth2.providers.google.GoogleOAuth2Provider.client_id)
      * [`GoogleOAuth2Provider.client_secret`](graphql_jwt_oauth2.providers.md#graphql_jwt_oauth2.providers.google.GoogleOAuth2Provider.client_secret)
      * [`GoogleOAuth2Provider.config`](graphql_jwt_oauth2.providers.md#graphql_jwt_oauth2.providers.google.GoogleOAuth2Provider.config)
      * [`GoogleOAuth2Provider.extract_profile()`](graphql_jwt_oauth2.providers.md#graphql_jwt_oauth2.providers.google.GoogleOAuth2Provider.extract_profile)
      * [`GoogleOAuth2Provider.fetch_profile()`](graphql_jwt_oauth2.providers.md#graphql_jwt_oauth2.providers.google.GoogleOAuth2Provider.fetch_profile)
      * [`GoogleOAuth2Provider.get_authorization_url()`](graphql_jwt_oauth2.providers.md#graphql_jwt_oauth2.providers.google.GoogleOAuth2Provider.get_authorization_url)
      * [`GoogleOAuth2Provider.get_callback_url()`](graphql_jwt_oauth2.providers.md#graphql_jwt_oauth2.providers.google.GoogleOAuth2Provider.get_callback_url)
      * [`GoogleOAuth2Provider.get_oauth2_token()`](graphql_jwt_oauth2.providers.md#graphql_jwt_oauth2.providers.google.GoogleOAuth2Provider.get_oauth2_token)
      * [`GoogleOAuth2Provider.name`](graphql_jwt_oauth2.providers.md#graphql_jwt_oauth2.providers.google.GoogleOAuth2Provider.name)
      * [`GoogleOAuth2Provider.scope`](graphql_jwt_oauth2.providers.md#graphql_jwt_oauth2.providers.google.GoogleOAuth2Provider.scope)
  * [Module contents](graphql_jwt_oauth2.providers.md#module-graphql_jwt_oauth2.providers)

## Submodules

## graphql_jwt_oauth2.constants module

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

## graphql_jwt_oauth2.decorators module

decorators.py

This module provides decorators used in the django-graphene-jwt-oauth2 library
to handle OAuth2 callback functionality.

Functions:
- callback: A decorator to process OAuth2 callback and pass data to the decorated view function.

Classes:
- None

Variables:
- None

### graphql_jwt_oauth2.decorators.callback(view_func: Callable[[...], Any])

Decorator to process OAuth2 callback and pass data to the decorated view function.

This decorator handles the OAuth2 callback process, validating the received code and state,
and extracting user data from the OAuth2 provider.

* **Parameters:**
  **view_func** (*Callable**[**...**,* *Any**]*) – The view function to be decorated.
* **Returns:**
  The wrapped view function.
* **Return type:**
  Callable[…, HttpResponse]

## graphql_jwt_oauth2.errors module

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

### *exception* graphql_jwt_oauth2.errors.ObscureException(message: str = 'Unauthorized')

Bases: `Exception`

Custom exception class with an optional message.

This exception class is designed to obscure error details in non-debug mode,
providing a generic error message.

* **Parameters:**
  **message** – The exception message.

### graphql_jwt_oauth2.errors.ObscureHttpResponse(reason: str = 'Unauthorized', code: int = 401)

Create an HTTP response with the provided reason and status code or defaults,
obscuring the error details in non-debug mode.

* **Parameters:**
  * **reason** – The reason for the HTTP response.
  * **code** – The HTTP status code.
* **Returns:**
  The HTTP response with obscured details.

## graphql_jwt_oauth2.jwt_helpers module

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

### graphql_jwt_oauth2.jwt_helpers.calculate_expiration(delta: timedelta)

Calculate the expiration time based on the provided timedelta.

* **Parameters:**
  **delta** (*timedelta*) – Timedelta for expiration.
* **Returns:**
  Datetime object representing the expiration time.
* **Return type:**
  datetime

### graphql_jwt_oauth2.jwt_helpers.is_refresh_token_expired(refresh_token: str, request: HttpRequest)

Check if the provided refresh token is expired.

* **Parameters:**
  * **refresh_token** (*str*) – Refresh token to be checked.
  * **request** (*HttpRequest*) – HttpRequest object.
* **Returns:**
  True if the token is expired, otherwise False.
* **Return type:**
  bool

### graphql_jwt_oauth2.jwt_helpers.set_cookies(response: HttpResponse, user: Any)

Set JWT and refresh token cookies on the HttpResponse object with CSRF rotation.

* **Parameters:**
  * **response** (*HttpResponse*) – HttpResponse object for setting cookies, headers, and CSRF rotation.
  * **user** (*Any*) – User instance for generating JWT and refresh tokens.

## graphql_jwt_oauth2.provider module

provider.py

This module defines the OAuth2Provider base class for the django-graphene-jwt-oauth2 library, 
providing the structure and required methods for specific OAuth2 providers.

Classes:
- OAuth2Provider: Base class for implementing OAuth2 providers.

Functions:
- None

Variables:
- None

### *class* graphql_jwt_oauth2.provider.OAuth2Provider(client_id: str | None = None, client_secret: str | None = None, scope: str | None = None, config: Dict | None = None, timeout: int | None = None)

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

## graphql_jwt_oauth2.queries module

queries.py

This module defines GraphQL queries and corresponding object 
types for the django-graphene-jwt-oauth2 library, 
including dynamic generation of OAuth2 provider links.

Classes:
- OAuth2LinksProviderMetaclass: A metaclass for dynamically

> generating GraphQL fields for OAuth2 providers.
- OAuth2LinksProvider: GraphQL ObjectType utilizing the metaclass for OAuth2 provider links.
- OAuth2LinksQuery: GraphQL ObjectType for querying OAuth2 authentication URLs.

Functions:
- None

Variables:
- None

### *class* graphql_jwt_oauth2.queries.OAuth2LinksProvider(google: Any = None)

Bases: `InterObjectType`, `ObjectType`

GraphQL ObjectType for OAuth2LinksProvider.

Utilizes OAuth2LinksProviderMetaclass for dynamic field generation. Each field represents
an OAuth2 provider’s authentication link.

#### google *= <graphene.types.field.Field object>*

#### resolve_google(info: GraphQLResolveInfo)

Resolver for generating OAuth2 login links.

* **Parameters:**
  * **self** – Instance of the class
  * **info** – GraphQL query information
  * **kwargs** – Keyword arguments
* **Returns:**
  Authorization URL for the OAuth2 provider

### *class* graphql_jwt_oauth2.queries.OAuth2LinksProviderMetaclass(name, bases, attrs)

Bases: `ObjectTypeMeta`

Metaclass for creating GraphQL fields and resolvers for OAuth2 links.

This metaclass dynamically generates GraphQL fields and corresponding resolvers
for various OAuth2 providers based on PROVIDER_CLASSES.

* **Parameters:**
  **graphene.ObjectType** (*type*) – Base class for GraphQL object types

### *class* graphql_jwt_oauth2.queries.OAuth2LinksQuery(o_auth2_links: Any = None)

Bases: `InterObjectType`, `ObjectType`

GraphQL query class for OAuth2 authentication URLs.

Provides a query field to retrieve authentication URLs for various OAuth2 providers.

* **Variables:**
  **o_auth2_urls** – Field to query OAuth2 authentication URLs

#### o_auth2_links *= <graphene.types.field.Field object>*

#### resolve_o_auth2_links(\*\*kwargs)

Resolver for the o_auth2_urls query field.

* **Parameters:**
  * **info** – GraphQL query information
  * **kwargs** – Keyword arguments containing ‘resource’ and ‘additional_state_payload’
* **Returns:**
  Dictionary containing the requested data

## graphql_jwt_oauth2.state_manager module

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

### *class* graphql_jwt_oauth2.state_manager.OAuth2StateManager(\*\*kwargs: Any)

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
