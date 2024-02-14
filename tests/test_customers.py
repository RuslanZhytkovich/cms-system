import pytest

from tests.data_for_tests import test_create_customer
from tests.data_for_tests import test_customers_patch_data
from tests.data_for_tests import test_get_all_customers_by_id_data
from tests.data_for_tests import test_get_all_customers_data
from tests.data_for_tests import test_soft_delete_customers_data


@pytest.mark.asyncio
@pytest.mark.parametrize("url, expected_status, user_type", test_create_customer)
async def test_create_customer(
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
        json_data = {"customer_name": "Pupsik <3"}
    elif user_type == "developer":
        json_data = {"customer_name": "Pupsik <3"}
        user_headers = create_developer
    elif user_type == "manager":
        json_data = {"customer_name": "Pupsik2 <3"}
        user_headers = create_manager

    response = await client.post(url, headers=user_headers, json=json_data)
    assert response.status_code == expected_status


@pytest.mark.asyncio
@pytest.mark.parametrize("url, expected_status, user_type", test_get_all_customers_data)
async def test_get_all_customers(
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
    "url, expected_status, user_type", test_get_all_customers_by_id_data
)
async def test_get_customers_by_id(
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
    "user_type, payload, expected_status", test_customers_patch_data
)
async def test_patch_customers(
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
        "/customers/update_by_id/1", json=payload, headers=user_headers
    )
    assert response.status_code == expected_status


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "url, expected_status, user_type", test_soft_delete_customers_data
)
async def test_soft_delete_customers(
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
