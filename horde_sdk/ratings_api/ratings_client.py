"""Definitions to help interact with the Ratings API."""

import asyncio

import aiohttp

from horde_sdk.generic_api.generic_clients import GenericAsyncHordeAPIManualClient, GenericHordeAPIManualClient
from horde_sdk.ratings_api.metadata import RatingsAPIPathFields, RatingsAPIQueryFields


class RatingsAPIClient(GenericHordeAPIManualClient):
    """Represent a client specifically configured for the Ratings API."""

    def __init__(self) -> None:
        """Create a new instance of the RatingsAPIClient."""
        super().__init__(
            path_fields=RatingsAPIPathFields,
            query_fields=RatingsAPIQueryFields,
        )


class AsyncRatingsAPIClient(GenericAsyncHordeAPIManualClient):
    """Represent a async client specifically configured for the Ratings APi."""

    def __init__(self, aiohttp_session: aiohttp.ClientSession) -> None:
        """Create a new instance of the AsyncRatingsAPIClient."""
        super().__init__(
            path_fields=RatingsAPIPathFields, query_fields=RatingsAPIQueryFields, aiohttp_session=aiohttp_session
        )
