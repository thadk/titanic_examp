from sqlalchemy.orm import DeclarativeBase

from titanic_examp.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta
