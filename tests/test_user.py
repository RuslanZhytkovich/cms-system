import pytest


@pytest.mark.asyncio
async def test_create_customer_by_manager(client):
    response = await client.get("/specializations/get_all")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_specialization(client):
    customer_data = {
  "specialization_name": "stmnring",
  "is_deleted": False
}
    response = await client.post("/specializations/create",  json=customer_data)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_customer_(client):
    response = await client.get("/specializatifons/get_all")
    assert response.status_code == 404