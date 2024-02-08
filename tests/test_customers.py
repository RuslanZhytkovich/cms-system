import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_get_all_customers(client: AsyncClient):
    response = await client.get("/customers/get_all")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_customer(client: AsyncClient):
    response = await client.post(
        "/customers/create",
        json={
            "customer_name": "Jlack",
            "is_deleted": False,
        },
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_customer_by_id(client: AsyncClient):
    response = await client.get("/customers/get_by_id/1")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_customer_by_id3(client: AsyncClient):
    response = await client.get("/customers/get_by_id/1")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_soft_delete_customer(client: AsyncClient):
    response = await client.patch("/customers/soft_delete/1")
    assert response.status_code == 200
