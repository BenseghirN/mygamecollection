from __future__ import annotations

from mygamecollection.domain.enums.game_status import GameStatus


class UserGame:
    def __init__(
            self,
            user_id: int,
            game_id: int,
            status: GameStatus = GameStatus.TO_DO
    ):
        self._user_id = user_id
        self._game_id = game_id
        self._status = status

    # region Properties Getters
    @property
    def user_id(self):
        return self._user_id

    @property
    def game_id(self):
        return self._game_id

    @property
    def status(self):
        return self._status
    # endregion

    # region Factory Methods
    @classmethod
    def create(
            cls,
            user_id: int,
            game_id: int
    ):
        return cls(
            user_id = user_id,
            game_id = game_id
        )

    def update_status(self, status: GameStatus):
        self._status = status
    # endregion

    # region Magic Methods
    def __hash__(self):
        return hash((self._user_id, self._game_id))

    def __eq__(self, other):
        if not isinstance(other, UserGame):
            return False
        return self._user_id == other._user_id and self._game_id == other._game_id

    def __repr__(self):
        return f"UserGame(user_id={self._user_id}, game_id={self._game_id}, status={self._status!r})"
    # endregion