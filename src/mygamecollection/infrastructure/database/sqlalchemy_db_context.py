from sqlalchemy.orm import Session

class SQLAlchemyGameCollectionDbContext:
    def __init__(self, session: Session):
        self._session = session

    def add(self, obj) -> None:
        self._session.add(obj)

    def commit(self) -> None:
        self._session.commit()

    def refresh(self, obj) -> None:
        self._session.refresh(obj)

    def execute(self, query):
        return self._session.execute(query)

    def delete(self, obj) -> None:
        self._session.delete(obj)

    def rollback(self) -> None:
        self._session.rollback()

    def close(self) -> None:
        self._session.close()