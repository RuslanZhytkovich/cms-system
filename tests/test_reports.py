import pytest
from projects.models import Project
from projects.schemas import CreateProject
from sqlalchemy import insert
from sqlalchemy import select
from users.models import User

from tests.data_for_tests import test_create_report


@pytest.mark.asyncio
@pytest.mark.parametrize("url, expected_status, user_type", test_create_report)
@pytest.mark.run(order=-1)
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

    # Insert the project data into the Project table
    project_insert = insert(Project).values(**project_data.dict()).returning(Project)
    await session.execute(project_insert)

    query = select(User).where(User.email == "admin@gmail.com")
    result = await session.execute(query)
    user = result.scalar_one()

    if user_type == "admin":
        user_headers = create_admin
    elif user_type == "developer":
        user_headers = create_developer
    elif user_type == "manager":
        user_headers = create_manager

    json_data = {
        "date": "2024-02-14",
        "hours": 4,
        "comment": "string",
        "user_id": str(user.user_id),
        "project_id": 1,
    }

    response = await client.post(url, headers=user_headers, json=json_data)
    assert response.status_code == expected_status
