from typing import Optional

from pydantic import BaseModel, ConfigDict


class TitanicModelDTO(BaseModel):
    """
    DTO for Titanic models.

    It is returned when accessing Titanic models from the API.
    """

    PassengerId: int
    Survived: int
    Pclass: int
    Pname: str
    Sex: str
    Age: Optional[float]
    SibSp: int
    Parch: int
    Ticket: str
    Fare: float
    Cabin: Optional[str]
    Embarked: Optional[str]
    model_config = ConfigDict(from_attributes=True)


class TitanicModelInputDTO(BaseModel):
    """DTO for creating new Titanic model."""

    PassengerId: int
    Survived: int
    Pclass: int
    Name: str
    Sex: str
    Age: Optional[float]
    SibSp: int
    Parch: int
    Ticket: str
    Fare: float
    Cabin: Optional[str]
    Embarked: Optional[str]
    model_config = ConfigDict(from_attributes=True)
