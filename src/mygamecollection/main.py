from mygamecollection.infrastructure.database.session import SessionLocal
from mygamecollection.infrastructure.database.sqlalchemy_db_context import SQLAlchemyGameCollectionDbContext

def main():
    session = SessionLocal()
    db_context = SQLAlchemyGameCollectionDbContext(session)

    try:
        print(f"DbContext initialized: {db_context}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db_context.close()


if __name__ == "__main__":
    main()