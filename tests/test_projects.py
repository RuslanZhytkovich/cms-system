import json

import pytest


@pytest.mark.asyncio
async def test_get_all_projects(client):
    response = await client.get("/projects/get_all")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_project(client):
    customer_data = {
        "customer_name": "project2",
        "is_deleted": False,
    }

    create_customer_resp = await client.post(
        "/customers/create", data=json.dumps(customer_data)
    )

    project_data = {
        "project_name": "string",
        "start_date": "2024-02-08",
        "end_date": "2024-02-08",
        "is_finished": False,
        "is_deleted": False,
        "customer_id": create_customer_resp.json()["customer_id"],
    }

    create_project_response = await client.post(
        "/projects/create", data=json.dumps(project_data)
    )

    assert create_project_response.status_code == 200


@pytest.mark.asyncio
async def test_soft_delete_project(client):
    create_customer_response = await client.post(
        "/customers/create",
        data=json.dumps(
            {
                "customer_name": "customer2",
                "is_deleted": False,
            }
        ),
    )

    create_project_response = await client.post(
        "/projects/create",
        data=json.dumps(
            {
                "project_name": "Project2",
                "start_date": "2024-02-08",
                "end_date": "2024-02-08",
                "is_finished": False,
                "is_deleted": False,
                "customer_id": create_customer_response.json()["customer_id"],
            }
        ),
    )

    soft_delete_project = await client.patch(
        f"/projects/soft_delete/{create_project_response.json()['project_id']}"
    )

    assert soft_delete_project.status_code == 200
    assert create_project_response.status_code == 200


@pytest.mark.asyncio
async def test_get_project_by_id(client):
    create_customer_response = await client.post(
        "/customers/create",
        data=json.dumps(
            {
                "customer_name": "customer5",
                "is_deleted": False,
            }
        ),
    )

    create_project_response = await client.post(
        "/projects/create",
        data=json.dumps(
            {
                "project_name": "Project3",
                "start_date": "2024-02-08",
                "end_date": "2024-02-08",
                "is_finished": False,
                "is_deleted": False,
                "customer_id": create_customer_response.json()["customer_id"],
            }
        ),
    )

    get_project_by_id_response = await client.get(
        f"/projects/get_by_id/{create_project_response.json()['project_id']}"
    )

    assert get_project_by_id_response.status_code == 200


@pytest.mark.asyncio
async def test_update_project_by_id(client):
    create_customer_response = await client.post(
        "/customers/create",
        data=json.dumps(
            {
                "customer_name": "customer6",
                "is_deleted": False,
            }
        ),
    )

    create_project_response = await client.post(
        "/projects/create",
        data=json.dumps(
            {
                "project_name": "Project4",
                "start_date": "2024-02-08",
                "end_date": "2024-02-08",
                "is_finished": False,
                "is_deleted": False,
                "customer_id": create_customer_response.json()["customer_id"],
            }
        ),
    )

    update_project_response = await client.patch(
        f"/projects/update_by_id/{create_project_response.json()['project_id']}",
        json={
            "project_name": "Project5",
            "start_date": "2024-02-08",
            "end_date": "2024-02-08",
            "is_finished": False,
            "is_deleted": False,
            "customer_id": create_customer_response.json()["customer_id"],
        },
    )

    assert update_project_response.status_code == 200
