import json

import pytest
from httpx import AsyncClient

from tests.data_for_tests import test_get_specialization_data, test_create_specialization, \
    test_specialization_patch_data, test_soft_delete_specialization_data, test_get_specialization_by_id_data


@pytest.mark.asyncio
@pytest.mark.parametrize("url, expected_status, user_type", test_get_specialization_data)
async def test_get_all_specializations(client, url, expected_status, user_type, create_admin, create_manager,create_developer ):
    if user_type == "admin":
        user_headers = create_admin
    elif user_type == "manager":
        user_headers = create_manager
    elif user_type == "developer":
        user_headers = create_developer

    response = await client.get(url, headers=user_headers)
    assert response.status_code == expected_status


@pytest.mark.asyncio
@pytest.mark.parametrize("url, expected_status, user_type", test_create_specialization)
async def test_create_specialization(client, url, expected_status, user_type, create_admin, create_developer, create_manager):

    if user_type == "admin":
        user_headers = create_admin
        json_data = {"specialization_name": "Pupsik <3"}
    elif user_type == "developer":
        json_data = {"specialization_name": "Pupsik <3"}
        user_headers = create_developer
    elif user_type == "manager":
        json_data = {"specialization_name": "Pupsik2 <3"}
        user_headers = create_manager

    response = await client.post(url, headers=user_headers, json=json_data)
    assert response.status_code == expected_status


# @pytest.mark.asyncio
# async def test_duplicate_data(client, create_admin):
#     specialization_data = {"specialization_name": "Pupsik <3"}
#     response = await client.post("/specializations/create", headers=create_admin, json=specialization_data, )
#     assert response.status_code == 500


@pytest.mark.asyncio
@pytest.mark.parametrize("user_type, payload, expected_status", test_specialization_patch_data)
async def test_patch_specialization(client, user_type, payload, expected_status, create_admin, create_developer,
                                    create_manager):
    if user_type == "admin":
        user_headers = create_admin
    elif user_type == "developer":
        user_headers = create_developer
    elif user_type == "manager":
        user_headers = create_manager

    response = await client.patch("/specializations/update_by_id/1", json=payload, headers=user_headers)
    assert response.status_code == expected_status


@pytest.mark.asyncio
@pytest.mark.parametrize("url, expected_status, user_type", test_soft_delete_specialization_data)
async def test_soft_delete_specialization(client, url, expected_status, user_type, create_admin, create_developer,
                                          create_manager):
    if user_type == "admin":
        user_headers = create_admin
    elif user_type == "developer":
        user_headers = create_developer
    elif user_type == "manager":
        user_headers = create_manager

    response = await client.patch(url, headers=user_headers)
    assert response.status_code == expected_status


@pytest.mark.asyncio
@pytest.mark.parametrize("url, expected_status, user_type", test_get_specialization_by_id_data)
async def test_get_specializations_by_id(client, url, expected_status, user_type, create_admin, create_developer,
                                         create_manager):
    if user_type == "admin":
        user_headers = create_admin
    elif user_type == "developer":
        user_headers = create_developer
    elif user_type == "manager":
        user_headers = create_manager

    response = await client.get(url, headers=user_headers)
    assert response.status_code == expected_status
