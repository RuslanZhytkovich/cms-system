import pytest
from conftest import client


@pytest.mark.asyncio
async def test_get_all_users(client):
    response = await client.get("/users/get_all")
    assert response.status_code == 200



