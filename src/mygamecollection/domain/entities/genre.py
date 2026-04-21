from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mygamecollection.domain.entities.game import Game


class Genre:
    def __init__(
            self,
            igdb_id: int,
            name: str,
            id: int | None = None
    ):
        self._id = id
        self._igdb_id = igdb_id
        self._name = name

        self._games: list[Game] = []

    # region Properties Getters
    @property
    def id(self):
        return self._id

    @property
    def igdb_id(self):
        return self._igdb_id

    @property
    def name(self):
        return self._name

    @property
    def games(self):
        return list(self._games)
    # endregion

    # region Factory Methods
    @classmethod
    def create(
            cls,
            igdb_id: int,
            name: str
    ):
        if not name.strip():
            raise ValueError("Genre name cannot be empty")

        return cls(
            igdb_id = igdb_id,
            name = name
        )
    # endregion

    # region Magic Methods
    def __hash__(self):
        return hash(self._igdb_id)

    def __eq__(self, other):
        if not isinstance(other, Genre):
            return False
        return self._igdb_id == other._igdb_id

    def __repr__(self):
        return f"Genre(id={self._id}, igdb_id={self._igdb_id}, name={self._name!r})"
    # endregion