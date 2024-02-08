import json

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_all_specializations(client: AsyncClient):
    response = await client.get("/specializations/get_all")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_specialization(client: AsyncClient):
    create_specialization_response = await client.post(
        "/specializations/create",
        json={
            "specialization_name": "Specialization1",
            "is_deleted": False,
        },
    )
    assert create_specialization_response.status_code == 200


@pytest.mark.asyncio
async def test_get_specialization_by_id(client: AsyncClient):
    response = await client.get("/specializations/get_by_id/1")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_soft_delete_specialization(client: AsyncClient):
    response = await client.patch("/specializations/soft_delete/1")
    assert response.status_code == 200


async def test_update_specialization(client):
    create_specialization_response = await client.post(
        "/specializations/create",
        data=json.dumps(
            {"specialization_name": "Specialization3",
             "is_deleted": False}
        ),
    )

    update_specialization = await client.patch(
        f"/specializations/update_by_id/{create_specialization_response.json()["specialization_id"]}", json={
            "specialization_name": "new_specializations2",
            "is_deleted": True,
        })

    assert update_specialization.status_code == 200
    assert create_specialization_response.status_code == 200
    assert update_specialization.json()["specialization_name"] == "new_specializations2"
    assert update_specialization.json()["is_deleted"] is True
