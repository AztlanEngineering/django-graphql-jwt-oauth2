"""
queries.py

This module defines GraphQL queries and corresponding object 
types for the django-graphene-jwt-oauth2 library, 
including dynamic generation of OAuth2 provider links.

Classes:
- OAuth2LinksProviderMetaclass: A metaclass for dynamically 
  generating GraphQL fields for OAuth2 providers.
- OAuth2LinksProvider: GraphQL ObjectType utilizing the metaclass for OAuth2 provider links.
- OAuth2LinksQuery: GraphQL ObjectType for querying OAuth2 authentication URLs.

Functions:
- None

Variables:
- None
"""
import json
from typing import Any

import graphene

from .constants import PROVIDER_CLASSES
from .state_manager import OAuth2StateManager


class OAuth2LinksProviderMetaclass(type(graphene.ObjectType)):
    """
    Metaclass for creating GraphQL fields and resolvers for OAuth2 links.

    This metaclass dynamically generates GraphQL fields and corresponding resolvers
    for various OAuth2 providers based on PROVIDER_CLASSES.

    :param type graphene.ObjectType: Base class for GraphQL object types
    """

    def __new__(mcs, name, bases, attrs):
        """
        Dynamically creates fields and resolvers for each provider.

        Iterates through PROVIDER_CLASSES to create a GraphQL field
        and a resolver method for each OAuth2 provider.

        :param name: Name of the class
        :param bases: Base classes of the class
        :param attrs: Attributes/dict of the class
        :return: New class object with dynamically added fields and resolvers
        """
        provider = None
        for provider_name, provider_class in PROVIDER_CLASSES.items():
            field_name = provider_name.lower()
            field_description = f"Login link for {provider_name} authentication"
            provider = provider_class()

            def resolver(parent: Any, info: graphene.ResolveInfo) -> str:
                """
                Resolver for generating OAuth2 login links.

                :param self: Instance of the class
                :param info: GraphQL query information
                :param kwargs: Keyword arguments
                :return: Authorization URL for the OAuth2 provider
                """
                print("being called")
                state_payload = {"resource": parent.get("resource")}
                additional_state_payload_json = parent.get("additional_state_payload")
                if additional_state_payload_json:
                    additional_state_payload = json.loads(additional_state_payload_json)
                    state_payload.update(additional_state_payload)

                encoded_state = OAuth2StateManager(payload=state_payload).encoded_state
                return provider.get_authorization_url(info.context, encoded_state)

            attrs[field_name] = graphene.Field(
                graphene.String, description=field_description, required=True
            )
            attrs[f"resolve_{field_name}"] = resolver

        return super().__new__(mcs, name, bases, attrs)


class OAuth2LinksProvider(graphene.ObjectType, metaclass=OAuth2LinksProviderMetaclass):
    """
    GraphQL ObjectType for OAuth2LinksProvider.

    Utilizes OAuth2LinksProviderMetaclass for dynamic field generation. Each field represents
    an OAuth2 provider's authentication link.
    """


class OAuth2LinksQuery(graphene.ObjectType):
    """
    GraphQL query class for OAuth2 authentication URLs.

    Provides a query field to retrieve authentication URLs for various OAuth2 providers.

    :ivar o_auth2_urls: Field to query OAuth2 authentication URLs
    """

    o_auth2_links = graphene.Field(
        OAuth2LinksProvider,
        resource=graphene.Argument(
            graphene.String,
            required=True,
            description="Resource identifier for the OAuth2 provider",
        ),
        additional_state_payload=graphene.Argument(
            graphene.String,
            description="Additional state payload for OAuth2 authentication",
        ),
        description="Retrieve OAuth2 authentication URLs for various providers",
    )

    def resolve_o_auth2_links(
        self, info: graphene.ResolveInfo, **kwargs
    ):  # pylint: disable=W0613
        """
        Resolver for the o_auth2_urls query field. This resolver is necessary to pass the
        field kwargs to the children.

        :param info: GraphQL query information
        :param kwargs: Keyword arguments containing 'resource' and 'additional_state_payload'
        :return: Dictionary containing the requested data
        """
        return kwargs
