import json

import pytest

from users.enums import RoleEnum


@pytest.mark.asyncio
async def test_get_all_reports(client):
    response = await client.get("/reports/get_all")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_report(client):
    spec_data = {  # FK for creating user
        "specialization_name": "specialization11",
        "is_deleted": False,
    }

    create_spec_resp = await client.post(
        "/specializations/create", data=json.dumps(spec_data)
    )
    data_from_create_spec = create_spec_resp.json()

    user_data = {
        "email": "user@exampldse.com",
        "password": "string",
        "name": "string",
        "last_name": "string",
        "role": RoleEnum.developer,
        "telegram": "stridsng",
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

    create_customer_resp = await client.post(
        "/customers/create", data=json.dumps({
        "customer_name": "project3",
        "is_deleted": False,
    }))


    create_project_response = await client.post(
        "/projects/create", data=json.dumps({
        "project_name": "strifsfng",
        "start_date": "2024-02-08",
        "end_date": "2024-02-08",
        "is_finished": False,
        "is_deleted": False,
        "customer_id": create_customer_resp.json()["customer_id"],
    }))

    create_report_response = await client.post(
        "/reports/create", data=json.dumps({
            "report_name": "strifsfng",
            "date": "2024-02-08",
            "hours": "4",
            "comment": "dsadasd",
            "is_deleted": False,
            "user_id": data_from_create_user["user_id"],
            "project_id": create_project_response.json()["project_id"],
        }))

    assert create_project_response.status_code == 200
    assert create_project_response.status_code == 200



