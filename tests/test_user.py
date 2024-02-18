import pytest
from tests.data_for_tests import test_get_all_users_data, test_get_user_by_id, test_create_user, test_users_patch_data, \
    test_soft_delete_developer_data, test_soft_delete_admin_data
from users.enums import RoleEnum


@pytest.mark.asyncio
@pytest.mark.parametrize("url, expected_status, user_type", test_get_all_users_data)
async def test_get_all_users(client, url, expected_status, user_type, create_admin, create_manager,create_developer ):
    if user_type == "admin":
        user_headers = create_admin
    elif user_type == "manager":
        user_headers = create_manager
    elif user_type == "developer":
        user_headers = create_developer

    response = await client.get(url, headers=user_headers)
    assert response.status_code == expected_status


@pytest.mark.asyncio
async def test_register(client):
    user_data={
        "email": "test@email.com",
        "password": "qwerty123123",

    }
    response = await client.post("/register", json=user_data)
    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "url, expected_status, user_type", test_get_user_by_id
)
async def test_get_user_by_id(
    client,
    url,
    expected_status,
    user_type,
    create_admin,
    create_developer,
    create_manager,
):
    if user_type == "admin":
        user_headers = create_admin
    if user_type == "developer":
        user_headers = create_developer
    if user_type == "manager":
        user_headers = create_manager
    response = await client.get(url, headers=user_headers)
    assert response.status_code == expected_status


@pytest.mark.asyncio
@pytest.mark.parametrize("url, expected_status, user_type", test_create_user)
async def test_create_user(url, client,expected_status, user_type, create_admin, create_developer, create_manager):
    json_data = {
          "email": "createuser@example.com",
          "password": "string",
          "name": "string",
          "last_name": "string",
          "role": RoleEnum.admin,
          "telegram": "string",
          "phone_number": "string",
          "on_bench": False,
          "time_created": "2024-02-18",
          "last_login": "2024-02-18",
          "is_active": True,
          "specialization_id": 1
        }

    if user_type == "admin":
        user_headers = create_admin
    elif user_type == "developer":
        user_headers = create_developer
    elif user_type == "manager":
        user_headers = create_manager

    response = await client.post(url, headers=user_headers, json=json_data)
    assert response.status_code == expected_status



@pytest.mark.asyncio
async def test_patch_developer_by_admin(client, create_admin, create_developer):
    json_data = {
        "email": "patchuser@example.com",
        "password": "string",
        "name": "string",
        "last_name": "string",
        "role": RoleEnum.developer,
        "telegram": "string",
        "phone_number": "string",
        "on_bench": False,
        "time_created": "2024-02-18",
        "last_login": "2024-02-18",
        "is_active": True,
        "specialization_id": 1
    }
    response = await client.patch("/users/update/eab93dd2-8d2d-434e-9916-6d8608aca8e6", headers=create_admin, json=json_data)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_patch_manager_by_admin(client, create_admin, create_manager):
    json_data = {
        "email": "patchamanager@example.com",
        "password": "string",
        "name": "string",
        "last_name": "string",
        "role": RoleEnum.developer,
        "telegram": "string",
        "phone_number": "string",
        "on_bench": False,
        "time_created": "2024-02-18",
        "last_login": "2024-02-18",
        "is_active": True,
        "specialization_id": 1
    }
    response = await client.patch("/users/update/eab73dd2-8d2d-434e-9916-6d8608aca8e6", headers=create_admin, json=json_data)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_patch_admin_by_admin(client, create_admin, create_admin_for_patch):
    json_data = {
        "email": "dasdas@example.com",
        "password": "string",
        "name": "string",
        "last_name": "string",
        "role": RoleEnum.developer,
        "telegram": "string",
        "phone_number": "string",
        "on_bench": False,
        "time_created": "2024-02-18",
        "last_login": "2024-02-18",
        "is_active": True,
        "specialization_id": 1
    }
    response = await client.patch("/users/update/eab32dd2-8d2d-434e-9916-6d8608aca8e6", headers=create_admin, json=json_data)
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_patch_admin_by_developer(client, create_admin, create_developer_for_patch):
    json_data = {
        "email": "patchadmin@example.com",
        "password": "string",
        "name": "string",
        "last_name": "string",
        "role": RoleEnum.developer,
        "telegram": "string",
        "phone_number": "string",
        "on_bench": False,
        "time_created": "2024-02-18",
        "last_login": "2024-02-18",
        "is_active": True,
        "specialization_id": 1
    }
    response = await client.patch("/users/update/eab83dd2-8d2d-434e-9916-6d8608aca8e6", headers=create_developer_for_patch, json=json_data)
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_patch_manager_by_developer(client, create_manager_for_patch, create_developer_for_patch):
    json_data = {
        "email": "patchadmin@example.com",
        "password": "string",
        "name": "string",
        "last_name": "string",
        "role": RoleEnum.developer,
        "telegram": "string",
        "phone_number": "string",
        "on_bench": False,
        "time_created": "2024-02-18",
        "last_login": "2024-02-18",
        "is_active": True,
        "specialization_id": 1
    }
    response = await client.patch("/users/update/eab75dd2-8d2d-434e-9916-6d8608aca8e6", headers=create_developer_for_patch, json=json_data)
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_patch_developer_by_developer(client, create_developer_for_patch):
    json_data = {
        "email": "patchadmin@example.com",
        "password": "string",
        "name": "string",
        "last_name": "string",
        "role": RoleEnum.developer,
        "telegram": "string",
        "phone_number": "string",
        "on_bench": False,
        "time_created": "2024-02-18",
        "last_login": "2024-02-18",
        "is_active": True,
        "specialization_id": 1
    }
    response = await client.patch("/users/update/eab93dd2-8d2d-434e-9916-6d8608aca8e6", headers=create_developer_for_patch, json=json_data)
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_patch_admin_by_manager(client, create_manager, create_admin_for_patch):
    json_data = {
        "email": "patchadmin2@example.com",
        "password": "string",
        "name": "string",
        "last_name": "string",
        "role": RoleEnum.developer,
        "telegram": "string",
        "phone_number": "string",
        "on_bench": False,
        "time_created": "2024-02-18",
        "last_login": "2024-02-18",
        "is_active": True,
        "specialization_id": 1
    }
    response = await client.patch("/users/update/eab32dd2-8d2d-434e-9916-6d8608aca8e6", headers=create_manager, json=json_data)
    assert response.status_code == 403


@pytest.mark.asyncio
async def test_patch_manager_by_manager(client, create_manager, create_manager_for_patch):
    json_data = {
        "email": "patchadmin2@example.com",
        "password": "string",
        "name": "string",
        "last_name": "string",
        "role": RoleEnum.developer,
        "telegram": "string",
        "phone_number": "string",
        "on_bench": False,
        "time_created": "2024-02-18",
        "last_login": "2024-02-18",
        "is_active": True,
        "specialization_id": 1
    }
    response = await client.patch("/users/update/eab75dd2-8d2d-434e-9916-6d8608aca8e6", headers=create_manager, json=json_data)
    assert response.status_code == 403



@pytest.mark.asyncio
async def test_patch_developer_by_manager(client, create_manager, create_developer_for_patch):
    json_data = {
        "email": "trololo@example.com",
        "password": "string",
        "name": "string",
        "last_name": "string",
        "role": RoleEnum.developer,
        "telegram": "string",
        "phone_number": "string",
        "on_bench": False,
        "time_created": "2024-02-18",
        "last_login": "2024-02-18",
        "is_active": True,
        "specialization_id": 1
    }
    response = await client.patch("/users/update/eab94dd2-8d2d-434e-9916-6d8608aca8e6", headers=create_manager, json=json_data)
    assert response.status_code == 200



@pytest.mark.asyncio
@pytest.mark.parametrize("url, expected_status, user_type", test_soft_delete_developer_data)
async def test_soft_delete_developer(client, url, expected_status, user_type, create_admin_for_soft_delete, create_developer_for_soft_delete,
                                          create_manager_for_soft_delete, create_developer_for_patch):
    if user_type == "admin":
        user_headers = create_admin_for_soft_delete
    elif user_type == "developer":
        user_headers = create_developer_for_soft_delete
    elif user_type == "manager":
        user_headers = create_manager_for_soft_delete

    response = await client.patch(url, headers=user_headers)
    assert response.status_code == expected_status


@pytest.mark.asyncio
@pytest.mark.parametrize("url, expected_status, user_type", test_soft_delete_admin_data)
async def test_soft_delete_admin(client, url, expected_status, user_type, create_admin_for_soft_delete, create_developer_for_soft_delete,
                                          create_manager_for_soft_delete, create_admin_for_patch):
    if user_type == "admin":
        user_headers = create_admin_for_soft_delete
    elif user_type == "developer":
        user_headers = create_developer_for_soft_delete
    elif user_type == "manager":
        user_headers = create_manager_for_soft_delete

    response = await client.patch(url, headers=user_headers)
    assert response.status_code == expected_status