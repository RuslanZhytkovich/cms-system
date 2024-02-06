import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_add_specific_operations(client: AsyncClient):
    response = await client.get("/customers/get_all")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test(client: AsyncClient):
    response = await client.post("/customers/create", json={
        "customer_name": "Jlack",
        "is_deleted": False,
    })

    assert response.status_code == 200