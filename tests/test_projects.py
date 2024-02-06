import pytest


@pytest.mark.asyncio
async def test_get_all_projects(client):
    response = await client.get("/projects/get_all")
    assert response.status_code == 200
