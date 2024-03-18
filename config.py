import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.sql import text

from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = os.getenv('DB_CONFIG')

engine = create_async_engine(DB_CONFIG, echo=True)
async_db = async_sessionmaker(engine)