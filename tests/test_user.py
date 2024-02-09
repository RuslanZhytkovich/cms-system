import json

import pytest
from users.enums import RoleEnum


@pytest.mark.asyncio
async def test_get_all_users(client):
    response = await client.get("/users/get_all")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_user(client):
    spec_data = {  # FK for creating user
        "specialization_name": "specialization1",
        "is_deleted": False,
    }

    create_spec_resp = await client.post(
        "/specializations/create", data=json.dumps(spec_data)
    )
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
        "specialization_id": data_from_create_spec["specialization_id"],
    }

    create_user_response = await client.post(
        "/users/create", data=json.dumps(user_data)
    )
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


@pytest.mark.asyncio
async def test_soft_delete_user(client):
    create_spec_resp = await client.post(
        "/specializations/create",
        data=json.dumps(
            {
                "specialization_name": "specialization2",
                "is_deleted": False,
            }
        ),
    )

    create_user_response = await client.post(
        "/users/create",
        data=json.dumps(
            {
                "email": "user@example2.com",
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
                "specialization_id": create_spec_resp.json()["specialization_id"],
            }
        ),
    )

    soft_delete_user = await client.patch(
        f"/users/soft_delete/{create_user_response.json()['user_id']}"
    )

    assert soft_delete_user.status_code == 200
    assert soft_delete_user.json()["is_active"] is False


@pytest.mark.asyncio
async def test_get_user_by_id(client):
    create_spec_resp = await client.post(
        "/specializations/create",
        data=json.dumps(
            {
                "specialization_name": "specialization3",
                "is_deleted": False,
            }
        ),
    )

    create_user_response = await client.post(
        "/users/create",
        data=json.dumps(
            {
                "email": "user@example3.com",
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
                "specialization_id": create_spec_resp.json()["specialization_id"],
            }
        ),
    )

    get_user_by_id = await client.get(
        f"/users/get_by_id/{create_user_response.json()['user_id']}"
    )

    assert get_user_by_id.status_code == 200
    assert get_user_by_id.json()["is_active"] is True


@pytest.mark.asyncio
async def test_update_user(client):
    create_spec_resp = await client.post(
        "/specializations/create",
        data=json.dumps(
            {
                "specialization_name": "specialization5",
                "is_deleted": False,
            }
        ),
    )

    create_user_data = {
        "email": "user@example4.com",
        "password": "string",
        "name": "string",
        "last_name": "string",
        "role": RoleEnum.developer,
        "telegram": "strinfdg",
        "phone_number": "string",
        "on_bench": False,
        "time_created": "2024-02-07",
        "last_login": "2024-02-07",
        "is_active": True,
        "specialization_id": create_spec_resp.json()["specialization_id"],
    }

    create_user_response = await client.post(
        "/users/create",
        data=json.dumps(create_user_data),
    )

    update_user = await client.patch(
        f"/users/update/{create_user_response.json()['user_id']}",
        json={
            "email": "new_email@gmail.com",
            "password": "string",
            "name": "new_name",
            "last_name": "string",
            "role": "admin",
            "telegram": "strgifdfng",
            "phone_number": "string",
            "on_bench": False,
            "time_created": "2024-02-08",
            "last_login": "2024-02-08",
            "is_active": True,
            "specialization_id": create_spec_resp.json()["specialization_id"],
        },
    )

    assert update_user.status_code == 200
    assert update_user.json()["email"] == "new_email@gmail.com"
    assert update_user.json()["name"] == "new_name"
