import os

from titanic_examp.settings import settings

# from sqlalchemy.orm import sessionmaker


async def create_database() -> None:
    """Create a database."""


async def drop_database() -> None:
    """Drop current database."""
    if settings.db_file.exists():
        os.remove(settings.db_file)
