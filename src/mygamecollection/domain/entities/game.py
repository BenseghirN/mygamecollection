class game:
    def __init__(
            self,
            igdb_id: int,
            name: str,
            summary: str | None = None,
            release_date: str | None = None,
            cover_url: str | None = None
    ):
        self.igdb_id = igdb_id
        self.name = name
        self.summary = summary
        self.release_date = release_date
        self.cover_url = cover_url

    def __repr__(self):
        return f"Game(igdb_id={self.igdb_id}, name='{self.name}', summary='{self.summary}', release_date='{self.release_date}', cover_url='{self.cover_url}')"
    
    def create_new_game(
            self,
            igdb_id: int,
            name: str,
            summary: str | None = None,
            release_date: str | None = None,
            cover_url: str | None = None
    ):
        return game(igdb_id, name, summary, release_date, cover_url)
    
    def update_game(
            self,
            name: str,
            summary: str | None = None,
            release_date: str | None = None,
            cover_url: str | None = None
    ):
        self.name = name
        self.summary = summary
        self.release_date = release_date
        self.cover_url = cover_url
    
    def delete_game(self):
        del self