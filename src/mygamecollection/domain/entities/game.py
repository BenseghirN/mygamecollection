from dataclasses import dataclass, field

@dataclass
class Game:
    igdb_id: int
    name: str
    summary: str | None = None
    release_date: str | None = None
    cover_url: str | None = None
    id: int | None = None

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
            igdb_id,
            name,
            summary,
            release_date,
            cover_url)

    def update(
            self,
            name: str,
            summary: str | None = None,
            release_date: str | None = None,
            cover_url: str | None = None
    ):
        if not name.strip():
            raise ValueError("Game name cannot be empty")
        self.name = name
        self.summary = summary
        self.release_date = release_date
        self.cover_url = cover_url