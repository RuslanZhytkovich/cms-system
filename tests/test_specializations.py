import pytest


@pytest.mark.asyncio
async def test_get_all_specializations(client):
    response = await client.get("/specializations/get_all")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_specializations(client):
    response = await client.post(
        "/specializations/create",
        json={
            "specialization_name": "test_name",
            "is_deleted": False,
        },
    )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_specializations(client):
    response = await client.delete("specializations/delete_by_id/1")
    assert response.status_code == 200
