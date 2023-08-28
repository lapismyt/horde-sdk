"""This module contains extra API models that are not part of the official API specification.

However, this module may still assist in the construction of valid requests to the API, primarily
by providing additional type hints for the request and response payloads and validation.
"""
import uuid
from typing import Any

from pydantic import RootModel, field_validator
from typing_extensions import override


class UUID_Identifier(RootModel[uuid.UUID]):
    """Represents a UUID type identifier used by the API."""

    model_config = {"frozen": True}

    root: uuid.UUID

    @field_validator("root", mode="before")
    def id_must_be_uuid(cls, v: str | uuid.UUID) -> str | uuid.UUID:
        """Ensure that the ID is a valid UUID."""
        if isinstance(v, uuid.UUID):
            return v

        if v == "":  # FIXME? This is a workaround for the swagger doc having `""`
            return uuid.UUID(int=0)

        try:
            return uuid.UUID(v, version=4)
        except ValueError as e:
            raise ValueError(f"Invalid UUID {v}") from e

    @override
    def __repr__(self) -> str:
        return self.__str__()

    @override
    def __str__(self) -> str:
        return self.root.__str__()

    @override
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, str):
            return self.root.__str__() == other

        if isinstance(other, uuid.UUID):
            return self.root == other

        return False

    @override
    def __hash__(self) -> int:
        return self.root.__hash__()


class JobID(UUID_Identifier):
    """Represents the ID of a generation job. Instances of this class can be compared with a `str` or a UUID object."""


class WorkerID(UUID_Identifier):
    """Represents the ID of a worker. Instances of this class can be compared with a `str` or a UUID object."""


class ImageID(UUID_Identifier):
    """Represents the ID of an image. Instances of this class can be compared with a `str` or a UUID object."""


class TeamID(UUID_Identifier):
    """Represents the ID of a team. Instances of this class can be compared with a `str` or a UUID object."""
