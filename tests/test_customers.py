import json

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_all_customers(client: AsyncClient):
    response = await client.get("/customers/get_all")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_customer(client: AsyncClient):
    create_customer_response = await client.post(
        "/customers/create",
        json={
            "customer_name": "Jlack",
            "is_deleted": False,
        },
    )
    assert create_customer_response.status_code == 200


@pytest.mark.asyncio
async def test_get_customer_by_id(client: AsyncClient):
    response = await client.get("/customers/get_by_id/1")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_soft_delete_customer(client: AsyncClient):
    response = await client.patch("/customers/soft_delete/1")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_customer(client):
    create_customer_response = await client.post(
        "/customers/create",
        data=json.dumps({"customer_name": "dasd", "is_deleted": False}),
    )

    update_customer = await client.patch(
        f"/customers/update_by_id/{create_customer_response.json()['customer_id']}",
        json={
            "customer_name": "new_customer",
            "is_deleted": True,
        },
    )

    assert update_customer.status_code == 200
    assert create_customer_response.status_code == 200
    assert update_customer.json()["customer_name"] == "new_customer"
    assert update_customer.json()["is_deleted"] is True
