import pytest


@pytest.mark.asyncio
async def test_get_all_reports(client):
    response = await client.get("/reports/get_all")
    assert response.status_code == 200
