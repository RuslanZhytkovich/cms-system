import pytest

from tests.data_for_tests import test_create_project
from tests.data_for_tests import test_get_all_projects_data
from tests.data_for_tests import test_get_project_by_id_data
from tests.data_for_tests import test_projects_patch_data
from tests.data_for_tests import test_soft_delete_projects_data


@pytest.mark.asyncio
@pytest.mark.parametrize("url, expected_status, user_type", test_create_project)
async def test_create_project(
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
        json_data = {
            "project_name": "admin_customer",
            "start_date": "2024-02-14",
            "end_date": "2024-02-14",
            "is_finished": False,
            "is_deleted": False,
            "customer_id": 1,
        }
    elif user_type == "developer":
        json_data = {
            "project_name": "developer_customer",
            "start_date": "2024-02-14",
            "end_date": "2024-02-14",
            "is_finished": False,
            "is_deleted": False,
            "customer_id": 1,
        }
        user_headers = create_developer
    elif user_type == "manager":
        json_data = {
            "project_name": "manager_customer",
            "start_date": "2024-02-14",
            "end_date": "2024-02-14",
            "is_finished": False,
            "is_deleted": False,
            "customer_id": 1,
        }
        user_headers = create_manager

    response = await client.post(url, headers=user_headers, json=json_data)
    assert response.status_code == expected_status


@pytest.mark.asyncio
@pytest.mark.parametrize("url, expected_status, user_type", test_get_all_projects_data)
async def test_get_all_projects(
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
@pytest.mark.parametrize("url, expected_status, user_type", test_get_project_by_id_data)
async def test_get_projects_by_id(
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
@pytest.mark.parametrize(
    "user_type, payload, expected_status", test_projects_patch_data
)
async def test_patch_projects(
    client,
    user_type,
    payload,
    expected_status,
    create_admin,
    create_developer,
    create_manager,
):
    if user_type == "admin":
        user_headers = create_admin
    elif user_type == "developer":
        user_headers = create_developer
    elif user_type == "manager":
        user_headers = create_manager

    response = await client.patch(
        "/projects/update_by_id/1", json=payload, headers=user_headers
    )
    assert response.status_code == expected_status


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "url, expected_status, user_type", test_soft_delete_projects_data
)
async def test_soft_delete_projects(
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
    elif user_type == "developer":
        user_headers = create_developer
    elif user_type == "manager":
        user_headers = create_manager

    response = await client.patch(url, headers=user_headers)
    assert response.status_code == expected_status
