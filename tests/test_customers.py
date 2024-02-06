import pytest


@pytest.mark.asyncio
async def test_get_all_customers(client):
    response = await client.get("/customers/get_all")
    assert response.status_code == 200
