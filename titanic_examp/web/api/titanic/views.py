from typing import List, Optional

from fastapi import APIRouter
from fastapi.param_functions import Depends

from titanic_examp.db.dao.titanic_dao import TitanicDAO
from titanic_examp.web.api.titanic.schema import TitanicModelDTO

router = APIRouter()


@router.get("/", response_model=List[TitanicModelDTO])
async def get_titanic_models(  # noqa: WPS211
    pname: Optional[str] = None,
    survived: Optional[int] = None,
    pclass: Optional[int] = None,
    sex: Optional[str] = None,
    age: Optional[float] = None,
    sibsp: Optional[int] = None,
    parch: Optional[int] = None,
    ticket: Optional[str] = None,
    fare: Optional[float] = None,
    cabin: Optional[str] = None,
    embarked: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
    titanic_dao: TitanicDAO = Depends(),
) -> List[TitanicModelDTO]:
    """
    Retrieve all titanic objects from the database.

    :param pname: name of titanic instance.
    :param survived: survived status of titanic instance.
    :param pclass: class of titanic instance.
    :param sex: sex of titanic instance.
    :param age: age of titanic instance.
    :param sibsp: siblings/spouses of titanic instance.
    :param parch: parents/children of titanic instance.
    :param ticket: ticket of titanic instance.
    :param fare: fare of titanic instance.
    :param cabin: cabin of titanic instance.
    :param embarked: embarked location of titanic instance.
    :param limit: limit of titanic objects, defaults to 10.
    :param offset: offset of titanic objects, defaults to 0.
    :param titanic_dao: DAO for titanic models.
    :return: list of titanic objects from database.
    """
    passengers = await titanic_dao.filter(
        pname=pname,
        survived=survived,
        pclass=pclass,
        sex=sex,
        age=age,
        sibsp=sibsp,
        parch=parch,
        ticket=ticket,
        fare=fare,
        cabin=cabin,
        embarked=embarked,
        limit=limit,
        offset=offset,
    )
    return [TitanicModelDTO.from_orm(passenger) for passenger in passengers]


@router.get("/all", response_model=List[TitanicModelDTO])
async def get_all_titanic_models(
    limit: int = 10,
    offset: int = 0,
    titanic_dao: TitanicDAO = Depends(),
) -> List[TitanicModelDTO]:
    """
    Retrieve all titanic objects from the database.

    :param limit: limit of titanic objects, defaults to 10.
    :param offset: offset of titanic objects, defaults to 0.
    :param titanic_dao: DAO for titanic models.
    :return: list of titanic objects from database.
    """
    passengers = await titanic_dao.get_all_passengers(limit=limit, offset=offset)
    return [TitanicModelDTO.from_orm(passenger) for passenger in passengers]


@router.put("/")
async def load_titanic_models(
    titanic_dao: TitanicDAO = Depends(),
) -> None:
    """
    Creates titanic model in the database using titanic.csv.

    :param titanic_dao: DAO for titanic models.
    """
    await titanic_dao.load_titanic_models()
