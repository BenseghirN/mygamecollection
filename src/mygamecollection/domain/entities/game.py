from __future__ import annotations

from datetime import datetime, timezone
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mygamecollection.domain.entities.genre import Genre
    from mygamecollection.domain.entities.user_game import UserGame


class Game:
    def __init__(
            self,
            igdb_id: int,
            name: str,
            summary: str | None = None,
            release_date: str | None = None,
            cover_url: str | None = None,
            id: int | None = None
    ):
        self._id = id
        self._igdb_id = igdb_id
        self._name = name
        self._summary = summary
        self._release_date = release_date
        self._cover_url = cover_url
        self._created_at = datetime.now(timezone.utc)

        self._genres: list[Genre] = []
        self._user_games: list[UserGame] = []

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
    def summary(self):
        return self._summary

    @property
    def release_date(self):
        return self._release_date

    @property
    def cover_url(self):
        return self._cover_url

    @property
    def created_at(self):
        return self._created_at

    @property
    def genres(self):
        return list(self._genres)

    @property
    def user_games(self):
        return list(self._user_games)
    # endregion

    # region Factory Methods
    @classmethod
    def create(
            cls,
            igdb_id: int,
            name: str,
            summary: str | None = None,
            release_date: str | None = None,
            cover_url: str | None = None
    ):
        if not name.strip():
            raise ValueError("Game name cannot be empty")

        return cls(
            igdb_id = igdb_id,
            name = name,
            summary = summary,
            release_date = release_date,
            cover_url = cover_url)

    def update(
            self,
            name: str,
            summary: str | None = None,
            release_date: str | None = None,
            cover_url: str | None = None
    ):
        if not name.strip():
            raise ValueError("Game name cannot be empty")

        self._name = name
        self._summary = summary
        self._release_date = release_date
        self._cover_url = cover_url

    def add_genre(self, genre: Genre):
        if not any(g.id == genre.id for g in self._genres):
            self._genres.append(genre)

    def remove_genre(self, genre: Genre):
        self._genres = [g for g in self._genres if g.id != genre.id]
    # endregion

    # region Magic Methods
    def __hash__(self):
        return hash(self.igdb_id)

    def __eq__(self, other):
        if not isinstance(other, Game):
            return False
        return self._igdb_id == other._igdb_id

    def __repr__(self):
        return f"Game(id={self._id}, igdb_id={self._igdb_id}, name={self._name!r})"
    # endregion