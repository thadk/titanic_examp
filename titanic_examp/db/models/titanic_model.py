from typing import Optional

from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from titanic_examp.db.base import Base


class TitanicModel(Base):
    __tablename__ = "titanic"
    PassengerId: Mapped[int] = mapped_column(Integer, primary_key=True)
    Survived: Mapped[int] = mapped_column(Integer)
    Pclass: Mapped[int] = mapped_column(Integer)
    Pname: Mapped[str] = mapped_column(String)
    Sex: Mapped[str] = mapped_column(String)
    Age: Mapped[Optional[float]] = mapped_column(Float)
    SibSp: Mapped[int] = mapped_column(Integer)
    Parch: Mapped[int] = mapped_column(Integer)
    Ticket: Mapped[str] = mapped_column(String)
    Fare: Mapped[float] = mapped_column(Float)
    Cabin: Mapped[Optional[str]] = mapped_column(String)
    Embarked: Mapped[Optional[str]] = mapped_column(String)


#   PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
