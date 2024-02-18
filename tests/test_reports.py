import pytest
from projects.models import Project
from projects.schemas import CreateProject
from sqlalchemy import insert


from tests.data_for_tests import test_create_report, test_get_all_reports_data, test_get_report_by_id_data, \
    test_soft_delete_report_data, test_reports_patch_data


@pytest.mark.asyncio
@pytest.mark.parametrize("url, expected_status, user_type", test_create_report)
async def test_create_report(
    client,
    url,
    expected_status,
    user_type,
    create_admin,
    create_developer,
    create_manager,
    session,
):

    project_data = CreateProject(
        project_id=1,
        project_name="fsdfsd",
        start_date="2024-02-14",
        end_date="2024-02-14",
        is_deleted=False,
        is_finished=False,
        customer_id=1,
    )

    project_insert = insert(Project).values(**project_data.dict()).returning(Project)
    await session.execute(project_insert)


    if user_type == "admin":
        user_headers = create_admin
    elif user_type == "developer":
        user_headers = create_developer
    elif user_type == "manager":
        user_headers = create_manager

    json_data = {
        "report_id": 1,
        "date": "2024-02-14",
        "hours": 4,
        "comment": "string",
        "user_id": "eab83dd2-8d2d-434e-9916-6d8608aca8e6",
        "project_id": 1,
    }

    response = await client.post(url, headers=user_headers, json=json_data)
    assert response.status_code == expected_status


@pytest.mark.asyncio
@pytest.mark.parametrize("url, expected_status, user_type", test_get_all_reports_data)
async def test_get_all_reports(
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
    "url, expected_status, user_type", test_get_report_by_id_data
)
async def test_get_report_by_id(
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
    "url, expected_status, user_type", test_soft_delete_report_data
)
async def test_soft_delete_report(
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


@pytest.mark.asyncio
@pytest.mark.parametrize("user_type, payload, expected_status", test_reports_patch_data)
async def test_patch_reports(
    client,
    user_type,
    payload,
    expected_status,
    create_admin,
    create_developer,
    create_manager,
    session,
):

    if user_type == "admin":
        user_headers = create_admin
    elif user_type == "developer":
        user_headers = create_developer
    elif user_type == "manager":
        user_headers = create_manager

    response = await client.patch(
        "/reports/update_by_id/1", json=payload, headers=user_headers
    )
    assert response.status_code == expected_status