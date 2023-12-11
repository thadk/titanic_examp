from typing import List, Optional

import pandas as pd
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from titanic_examp.db.dependencies import get_db_session
from titanic_examp.db.models.titanic_model import TitanicModel


class TitanicDAO:
    """Class for accessing titanic table."""

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    async def create_titanic_model_single(  # noqa: WPS211
        self,
        pname: str,
        survived: int,
        pclass: int,
        sex: str,
        age: float,
        sibsp: int,
        parch: int,
        ticket: str,
        fare: float,
        cabin: str,
        embarked: str,
    ) -> None:
        """
                Add single titanic model to session.
        :param age: filter parameter
        :param cabin: filter parameter
        :param embarked: filter parameter
        :param fare: filter parameter
        :param parch: filter parameter
        :param pclass: filter parameter
        :param pname: filter parameter
        :param sex: filter parameter
        :param sibsp: filter parameter
        :param survived: filter parameter
        :param ticket: filter parameter
        """
        self.session.add(
            TitanicModel(
                Pname=pname,
                Survived=survived,
                Pclass=pclass,
                Sex=sex,
                Age=age,
                SibSp=sibsp,
                Parch=parch,
                Ticket=ticket,
                Fare=fare,
                Cabin=cabin,
                Embarked=embarked,
            ),
        )

    async def load_titanic_models(self) -> None:
        """
        Add the whole list of titanic models."""
        csv_file = "titanic_examp/static/titanic.csv"
        # Load data from CSV into a Pandas DataFrame
        df = pd.read_csv(csv_file)

        # Insert data into the TitanicModel table
        for _index, row in df.iterrows():
            titanic_entry = TitanicModel(
                PassengerId=row["PassengerId"],
                Survived=row["Survived"],
                Pclass=row["Pclass"],
                Pname=row["Name"],
                Sex=row["Sex"],
                Age=row["Age"],
                SibSp=row["SibSp"],
                Parch=row["Parch"],
                Ticket=row["Ticket"],
                Fare=row["Fare"],
                Cabin=row["Cabin"],
                Embarked=row["Embarked"],
            )
            self.session.add(titanic_entry)

    async def get_all_passengers(self, limit: int, offset: int) -> List[TitanicModel]:
        """
        Get all titanic models with limit/offset pagination.

        :param limit: limit of titanic passengers.
        :param offset: offset of titanic passengers.
        :return: stream of titanic passengers.
        """
        raw_titanic = await self.session.execute(
            select(TitanicModel).limit(limit).offset(offset),
        )

        return list(raw_titanic.scalars().fetchall())

    async def filter(  # noqa: WPS211 # noqa: C901
        self,
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
        limit: Optional[int] = 10,
        offset: Optional[int] = 0,
    ) -> List[TitanicModel]:
        """
        Get specific titanic model.

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
        :param limit: limit for return
        "param offset: number to skip
        :return: titanic models.
        """
        query = select(TitanicModel)
        if pname:
            query = query.where(TitanicModel.Pname.contains(pname))
        if survived is not None:
            query = query.where(TitanicModel.Survived == survived)
        if pclass is not None:
            query = query.where(TitanicModel.Pclass == pclass)
        if sex:
            query = query.where(TitanicModel.Sex.contains(sex))
        if age is not None:
            query = query.where(TitanicModel.Age == age)
        if sibsp is not None:
            query = query.where(TitanicModel.SibSp == sibsp)
        if parch is not None:
            query = query.where(TitanicModel.Parch == parch)
        if ticket:
            query = query.where(TitanicModel.Ticket.contains(ticket))
        if fare is not None:
            query = query.where(TitanicModel.Fare == fare)
        if cabin:
            query = query.where(TitanicModel.Cabin.contains(cabin))
        if embarked:
            query = query.where(TitanicModel.Embarked.contains(embarked))
        rows = await self.session.execute(query.limit(limit).offset(offset))
        return list(rows.scalars().fetchall())
