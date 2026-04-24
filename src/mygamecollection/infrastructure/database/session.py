from contextlib import asynccontextmanager
import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.mygamecollection.infrastructure.database.sqlalchemy_db_context import SQLAlchemyGameCollectionDbContext

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable not found")

engine = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(
    engine, 
    autocommit=False, 
    autoflush=False, 
    expire_on_commit=False
)

@asynccontextmanager
async def get_db_session():
    async with SessionLocal() as session:
        yield SQLAlchemyGameCollectionDbContext(session)