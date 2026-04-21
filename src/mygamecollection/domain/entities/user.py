from __future__ import annotations

from datetime import datetime, timezone
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mygamecollection.domain.entities.user_game import UserGame


class User:
    def __init__(
            self,
            login: str,
            first_name: str,
            last_name: str,
            id: int | None = None
    ):
        self._id = id
        self._login = login
        self._first_name = first_name
        self._last_name = last_name
        self._created_at = datetime.now(timezone.utc)

        self._user_games: list[UserGame] = []

    # region Properties Getters
    @property
    def id(self):
        return self._id

    @property
    def login(self):
        return self._login

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def created_at(self):
        return self._created_at

    @property
    def user_games(self):
        return list(self._user_games)
    # endregion

    # region Factory Methods
    @classmethod
    def create(
            cls,
            login: str,
            first_name: str,
            last_name: str
    ):
        if not login.strip():
            raise ValueError("Login cannot be empty")
        if not first_name.strip():
            raise ValueError("First name cannot be empty")
        if not last_name.strip():
            raise ValueError("Last name cannot be empty")

        return cls(
            login = login,
            first_name = first_name,
            last_name = last_name
        )

    def update(
            self,
            login: str,
            first_name: str,
            last_name: str,
    ):
        if not login.strip():
            raise ValueError("Login cannot be empty")
        if not first_name.strip():
            raise ValueError("First name cannot be empty")
        if not last_name.strip():
            raise ValueError("Last name cannot be empty")

        self._login = login
        self._first_name = first_name
        self._last_name = last_name

    def add_user_game(self, user_game: UserGame):
        if not any(ug.game_id == user_game.game_id for ug in self._user_games):
            self._user_games.append(user_game)

    def remove_user_game(self, game_id: int):
        self._user_games =  [ug for ug in self._user_games if ug.game_id != game_id]
    # endregion

    # region Magic Methods
    def __hash__(self):
        return hash((self.login, self.first_name, self.last_name))

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.login == other.login and self.first_name == other.first_name and self.last_name == other.last_name

    def __repr__(self):
        return f"User(id={self._id}, login={self._login!r}, first_name={self._first_name!r}, last_name={self._last_name!r})"
    # endregion