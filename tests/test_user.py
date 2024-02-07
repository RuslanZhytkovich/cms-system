import json
import pytest
from conftest import client
from users.enums import RoleEnum


@pytest.mark.asyncio
async def test_get_all_users(client):
    response = await client.get("/users/get_all")
    assert response.status_code == 200


async def test_create_user(client):
    spec_data = {                   # FK for creating user
        "specialization_name": "specialization1",
        "is_deleted": False,
    }

    create_spec_resp = await client.post("/specializations/create", data=json.dumps(spec_data))
    data_from_create_spec = create_spec_resp.json()

    user_data = {
        "email": "user@example.com",
        "password": "string",
        "name": "string",
        "last_name": "string",
        "role": RoleEnum.developer,
        "telegram": "string",
        "phone_number": "string",
        "on_bench": False,
        "time_created": "2024-02-07",
        "last_login": "2024-02-07",
        "is_active": True,
        "specialization_id": data_from_create_spec["specialization_id"]
     }

    create_user_response = await client.post("/users/create", data=json.dumps(user_data))
    data_from_create_user = create_user_response.json()

    assert create_user_response.status_code == 200
    assert create_spec_resp.status_code == 200
    assert data_from_create_user["email"] == user_data["email"]
    assert data_from_create_user["password"] == user_data["password"]
    assert data_from_create_user["name"] == user_data["name"]
    assert data_from_create_user["last_name"] == user_data["last_name"]
    assert data_from_create_user["telegram"] == user_data["telegram"]
    assert data_from_create_user["phone_number"] == user_data["phone_number"]
    assert data_from_create_user["on_bench"] is False
    assert data_from_create_user["time_created"] == user_data["time_created"]
    assert data_from_create_user["last_login"] == user_data["last_login"]
    assert data_from_create_user["is_active"] is True
    assert data_from_create_user["specialization_id"] == user_data["specialization_id"]








