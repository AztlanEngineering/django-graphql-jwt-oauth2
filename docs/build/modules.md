# graphql_jwt_oauth2

* [graphql_jwt_oauth2 package](graphql_jwt_oauth2.md)
  * [Subpackages](graphql_jwt_oauth2.md#subpackages)
    * [graphql_jwt_oauth2.providers package](graphql_jwt_oauth2.providers.md)
      * [Submodules](graphql_jwt_oauth2.providers.md#submodules)
      * [graphql_jwt_oauth2.providers.google module](graphql_jwt_oauth2.providers.md#module-graphql_jwt_oauth2.providers.google)
      * [Module contents](graphql_jwt_oauth2.providers.md#module-graphql_jwt_oauth2.providers)
  * [Submodules](graphql_jwt_oauth2.md#submodules)
  * [graphql_jwt_oauth2.constants module](graphql_jwt_oauth2.md#module-graphql_jwt_oauth2.constants)
  * [graphql_jwt_oauth2.decorators module](graphql_jwt_oauth2.md#module-graphql_jwt_oauth2.decorators)
    * [`callback()`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.decorators.callback)
  * [graphql_jwt_oauth2.errors module](graphql_jwt_oauth2.md#module-graphql_jwt_oauth2.errors)
    * [`ObscureException`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.errors.ObscureException)
    * [`ObscureHttpResponse()`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.errors.ObscureHttpResponse)
  * [graphql_jwt_oauth2.jwt_helpers module](graphql_jwt_oauth2.md#module-graphql_jwt_oauth2.jwt_helpers)
    * [`calculate_expiration()`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.jwt_helpers.calculate_expiration)
    * [`is_refresh_token_expired()`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.jwt_helpers.is_refresh_token_expired)
    * [`set_cookies()`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.jwt_helpers.set_cookies)
  * [graphql_jwt_oauth2.provider module](graphql_jwt_oauth2.md#module-graphql_jwt_oauth2.provider)
    * [`OAuth2Provider`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.provider.OAuth2Provider)
      * [`OAuth2Provider.extract_profile()`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.provider.OAuth2Provider.extract_profile)
      * [`OAuth2Provider.fetch_profile()`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.provider.OAuth2Provider.fetch_profile)
      * [`OAuth2Provider.get_authorization_url()`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.provider.OAuth2Provider.get_authorization_url)
      * [`OAuth2Provider.get_callback_url()`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.provider.OAuth2Provider.get_callback_url)
      * [`OAuth2Provider.get_oauth2_token()`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.provider.OAuth2Provider.get_oauth2_token)
      * [`OAuth2Provider.timeout`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.provider.OAuth2Provider.timeout)
  * [graphql_jwt_oauth2.queries module](graphql_jwt_oauth2.md#module-graphql_jwt_oauth2.queries)
    * [`OAuth2LinksProvider`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.queries.OAuth2LinksProvider)
      * [`OAuth2LinksProvider.google`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.queries.OAuth2LinksProvider.google)
      * [`OAuth2LinksProvider.resolve_google()`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.queries.OAuth2LinksProvider.resolve_google)
    * [`OAuth2LinksProviderMetaclass`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.queries.OAuth2LinksProviderMetaclass)
    * [`OAuth2LinksQuery`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.queries.OAuth2LinksQuery)
      * [`OAuth2LinksQuery.o_auth2_links`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.queries.OAuth2LinksQuery.o_auth2_links)
      * [`OAuth2LinksQuery.resolve_o_auth2_links()`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.queries.OAuth2LinksQuery.resolve_o_auth2_links)
  * [graphql_jwt_oauth2.state_manager module](graphql_jwt_oauth2.md#module-graphql_jwt_oauth2.state_manager)
    * [`OAuth2StateManager`](graphql_jwt_oauth2.md#graphql_jwt_oauth2.state_manager.OAuth2StateManager)
  * [Module contents](graphql_jwt_oauth2.md#module-graphql_jwt_oauth2)
