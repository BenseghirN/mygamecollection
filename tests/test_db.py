from src.myGameCollection.infrastructure.database.session import engine
from src.myGameCollection.infrastructure.database.base import Base
from src.myGameCollection.infrastructure.database.model import GameModel

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Database tables created successfully.")