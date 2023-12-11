import uuid

import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from titanic_examp.db.dao.titanic_dao import TitanicDAO


@pytest.mark.anyio
async def test_creation(
    fastapi_app: FastAPI,
    client: AsyncClient,
    dbsession: AsyncSession,
) -> None:
    """Tests titanic instance creation."""
    dao = TitanicDAO(dbsession)
    testname = uuid.uuid4().hex
    await dao.create_titanic_model_single(
        pname=testname,
        survived=0,
        pclass=0,
        sex=testname,
        age=1,
        sibsp=2,
        parch=2,
        ticket=testname,
        fare=0.02,
        cabin=testname,
        embarked=testname,
    )
    dao = TitanicDAO(dbsession)
    instances = await dao.filter(pname=testname)
    assert instances[0].Pname == testname

    url = fastapi_app.url_path_for("get_titanic_models")
    response = await client.get(url)
    titanic = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(titanic) == 1


@pytest.mark.anyio
async def test_getting(
    fastapi_app: FastAPI,
    client: AsyncClient,
    dbsession: AsyncSession,
) -> None:
    """Tests titanic instance retrieval.

    After loading all the passengers, filter the first 100 embarked=Q passengers.
    Expect 77"""
    url = fastapi_app.url_path_for("load_titanic_models")
    response = await client.put(
        url,
        json={},
    )
    response = await client.get(url)
    # PUT request to load titanic.csv:
    response.json()

    # GET request:
    url2 = (
        fastapi_app.url_path_for("get_titanic_models")
        + "?embarked=Q&limit=100&offset=0"
    )
    response2 = await client.get(
        url2,
    )
    titanic = response2.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(titanic) > 50  # target: 77
