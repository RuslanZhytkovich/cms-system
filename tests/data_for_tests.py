test_check_patch_data = [
    ("admin", {"email": "admin@mail.ru"}, 200),
    ("developer", {"email": "admin@mail.ru"}, 403),
    ("manager", {"email": "admin@mail.ru"}, 403),
]


test_get_all_users_data = [
    ("/users/get_all", 200, "admin"),
    ("/users/get_all", 200, "manager"),
    ("/users/get_all", 403, "developer"),
]

test_get_user_by_id = [
    ("/users/get_by_id/eab93dd2-8d2d-434e-9916-6d8608aca8e6", 200, "admin"),
    ("/users/get_by_id/eab93dd2-8d2d-434e-9916-6d8608aca8e6", 200, "manager"),
    ("/users/get_by_id/eab93dd2-8d2d-434e-9916-6d8608aca8e6", 403, "developer"),
    ("/users/get_by_id/eab94dd2-8d2d-434e-9916-6d8608aca8e6", 404, "admin"),
    ("/users/get_by_id/eab94dd2-8d2d-434e-9916-6d8608aca8e6", 404, "manager"),
    ("/users/get_by_id/eab94dd2-8d2d-434e-9916-6d8608aca8e6", 403, "developer"),
]

test_get_user_by_email = [
    ("/users/get_user_by_email/rzhitkovich@bk.ru", 403, "developer"),
    ("/users/get_user_by_email/rzhitkovich@bk.ru", 200, "admin"),
    ("/users/get_user_by_email/incorrect_email@bk.ru", 404, "admin"),
    ("/users/get_user_by_email/rzhitkovich@bk.ru", 200, "manager"),
    ("/users/get_user_by_email/incorrectemail2@bk.ru", 404, "manager"),
    ("/users/get_user_by_email/incorrectemail2@bk.ru", 403, "manager"),
]

test_soft_delete_data = [
    ("/users/soft_delete/50", 400, "admin"),
    ("/users/soft_delete/101", 200, "admin"),
    ("/users/soft_delete/101", 403, "developer"),
    ("/users/soft_delete/101", 403, "manager"),
]

test_get_specialization_data = [
    ("/specializations/get_all", 200, "admin"),
    ("/specializations/get_all", 200, "manager"),
    ("/specializations/get_all", 403, "developer"),
]

test_soft_delete_specialization_data = [
    ("/specializations/soft_delete/1", 403, "developer"),
    ("/specializations/soft_delete/2", 200, "admin"),
    ("/specializations/soft_delete/2", 200, "manager"),
    ("/specializations/soft_delete/123", 403, "developer"),
    ("/specializations/soft_delete/123", 404, "admin"),
    ("/specializations/soft_delete/123", 404, "manager"),
]

test_soft_delete_developer_data = [
    ("/users/soft_delete/eab16dd2-8d2d-434e-9916-6d8608aca8e6", 403, "developer"),
    ("/users/soft_delete/eab16dd2-8d2d-434e-9916-6d8608aca8e6", 200, "admin"),
    ("/users/soft_delete/eab16dd2-8d2d-434e-9916-6d8608aca8e6", 200, "manager"),
    ("/users/soft_delete/eab18dd2-8d2d-434e-9916-6d8608aca8e6", 403, "developer"),
    ("/users/soft_delete/eab18dd2-8d2d-434e-9916-6d8608aca8e6", 404, "admin"),
    ("/users/soft_delete/eab18dd2-8d2d-434e-9916-6d8608aca8e6", 404, "manager"),
]

test_soft_delete_admin_data = [
    ("/users/soft_delete/eab32dd2-8d2d-434e-9916-6d8608aca8e6", 403, "developer"),
    ("/users/soft_delete/eab32dd2-8d2d-434e-9916-6d8608aca8e6", 403, "admin"),
    ("/users/soft_delete/eab32dd2-8d2d-434e-9916-6d8608aca8e6", 403, "manager"),
    ("/users/soft_delete/eab33dd2-8d2d-434e-9916-6d8608aca8e6", 403, "developer"),
    ("/users/soft_delete/eab33dd2-8d2d-434e-9916-6d8608aca8e6", 404, "admin"),
    ("/users/soft_delete/eab33dd2-8d2d-434e-9916-6d8608aca8e6", 404, "manager"),
]


test_specialization_patch_data = [
    ("admin", {"specialization_name": "FullStack"}, 200),
    ("developer", {"specialization_name": "FullStack"}, 403),
    ("manager", {"specialization_name": "FullStack"}, 200),
]

test_create_specialization = [
    ("/specializations/create", 403, "developer"),
    ("/specializations/create", 200, "admin"),
    ("/specializations/create", 200, "manager"),
]

test_create_customer = [
    ("/customers/create", 403, "developer"),
    ("/customers/create", 200, "admin"),
    ("/customers/create", 200, "manager"),
]

test_create_customer_already_exist = [
    ("/customers/create", 403, "developer"),
    ("/customers/create", 409, "admin"),
    ("/customers/create", 409, "manager"),
]

test_create_project = [
    ("/projects/create", 403, "developer"),
    ("/projects/create", 200, "admin"),
    ("/projects/create", 200, "manager"),
]

test_get_all_customers_data = [
    ("/customers/get_all", 403, "developer"),
    ("/customers/get_all", 200, "admin"),
    ("/customers/get_all", 200, "manager"),
]

test_get_all_customers_by_id_data = [
    ("/customers/get_by_id/1", 403, "developer"),
    ("/customers/get_by_id/1", 200, "admin"),
    ("/customers/get_by_id/1", 200, "manager"),
    ("/customers/get_by_id/124", 403, "developer"),
    ("/customers/get_by_id/124", 404, "admin"),
    ("/customers/get_by_id/124", 404, "manager"),
]


test_get_specialization_by_id_data = [
    ("/specializations/get_by_id/1", 403, "developer"),
    ("/specializations/get_by_id/1", 200, "admin"),
    ("/specializations/get_by_id/1", 200, "manager"),
    ("/specializations/get_by_id/123", 403, "developer"),
    ("/specializations/get_by_id/123", 404, "admin"),
    ("/specializations/get_by_id/123", 404, "manager"),
]

test_customers_patch_data = [
    ("admin", {"customer_name": "CustomerTest1"}, 200),
    ("developer", {"customer_name": "CustomerTest2"}, 403),
    ("manager", {"customer_name": "CustomerTest3"}, 200),
]

test_soft_delete_customers_data = [
    ("/customers/soft_delete/1", 403, "developer"),
    ("/customers/soft_delete/1", 200, "admin"),
    ("/customers/soft_delete/1", 200, "manager"),
    ("/customers/soft_delete/123", 403, "developer"),
    ("/customers/soft_delete/123", 404, "admin"),
    ("/customers/soft_delete/123", 404, "manager"),
]

test_get_all_projects_data = [
    ("/projects/get_all", 403, "developer"),
    ("/projects/get_all", 200, "admin"),
    ("/projects/get_all", 200, "manager"),
]

test_create_project = [
    ("/projects/create", 403, "developer"),
    ("/projects/create", 200, "admin"),
    ("/projects/create", 200, "manager"),
]

test_get_project_by_id_data = [
    ("/projects/get_by_id/1", 403, "developer"),
    ("/projects/get_by_id/1", 200, "admin"),
    ("/projects/get_by_id/1", 200, "manager"),
    ("/projects/get_by_id/123", 403, "developer"),
    ("/projects/get_by_id/123", 404, "admin"),
    ("/projects/get_by_id/123", 404, "manager"),
]

test_projects_patch_data = [
    (
        "admin",
        {
            "project_name": "new_proj_name1",
            "start_date": "2024-02-14",
            "end_date": "2024-02-14",
            "is_finished": False,
            "is_deleted": False,
            "customer_id": 1,
        },
        200,
    ),
    (
        "developer",
        {
            "project_name": "new_proj_name2",
            "start_date": "2024-02-14",
            "end_date": "2024-02-14",
            "is_finished": False,
            "is_deleted": False,
            "customer_id": 1,
        },
        403,
    ),
    (
        "manager",
        {
            "project_name": "new_proj_name3",
            "start_date": "2024-02-14",
            "end_date": "2024-02-14",
            "is_finished": False,
            "is_deleted": False,
            "customer_id": 1,
        },
        200,
    ),
]

test_soft_delete_projects_data = [
    ("/projects/soft_delete/1", 403, "developer"),
    ("/projects/soft_delete/2", 200, "admin"),
    ("/projects/soft_delete/2", 200, "manager"),
    ("/projects/soft_delete/123", 403, "developer"),
    ("/projects/soft_delete/123", 404, "admin"),
    ("/projects/soft_delete/123", 404, "manager"),
]

test_create_report = [
    ("/reports/create", 200, "developer"),
    ("/reports/create", 200, "admin"),
    ("/reports/create", 200, "manager"),
]

test_get_report_by_id_data = [
    ("/reports/get_by_id/1", 403, "developer"),
    ("/reports/get_by_id/1", 200, "admin"),
    ("/reports/get_by_id/1", 200, "manager"),
    ("/reports/get_by_id/123", 403, "developer"),
    ("/reports/get_by_id/123", 404, "admin"),
    ("/reports/get_by_id/123", 404, "manager"),
]

test_get_all_reports_data = [
    ("/reports/get_all", 403, "developer"),
    ("/reports/get_all", 200, "admin"),
    ("/reports/get_all", 200, "manager"),
]

test_soft_delete_report_data = [
    ("/reports/soft_delete/1", 403, "developer"),
    ("/reports/soft_delete/1", 200, "admin"),
    ("/reports/soft_delete/1", 200, "manager"),
    ("/reports/soft_delete/123", 403, "developer"),
    ("/reports/soft_delete/123", 404, "admin"),
    ("/reports/soft_delete/123", 404, "manager"),
]


test_reports_patch_data = [
    (
        "admin",
        {
            "date": "2024-02-20",
            "hours": 5,
            "comment": "string",
            "user_id": "eab73dd2-8d2d-434e-9916-6d8608aca8e6",
            "project_id": 1,
        },
        200,
    ),
    (
        "developer",
        {
            "date": "2024-02-21",
            "hours": 4,
            "comment": "string",
            "user_id": "eab73dd2-8d2d-434e-9916-6d8608aca8e6",
            "project_id": 1,
        },
        403,
    ),
    (
        "manager",
        {
            "date": "2024-02-25",
            "hours": 12,
            "comment": "string",
            "user_id": "eab73dd2-8d2d-434e-9916-6d8608aca8e6",
            "project_id": 1,
        },
        200,
    ),
]


test_create_user = [
    ("/users/create", 403, "developer"),
    ("/users/create", 200, "admin"),
    ("/users/create", 403, "manager"),
]


test_users_patch_data = [
    ("/users/update/eab93dd2-8d2d-434e-9916-6d8608aca8e6", 403, "developer"),
    ("/users/update/eab93dd2-8d2d-434e-9916-6d8608aca8e6", 200, "admin"),
    ("/users/update/eab93dd2-8d2d-434e-9916-6d8608aca8e6", 200, "manager"),
    ("/users/update/eab95dd2-8d2d-434e-9916-6d8608aca8e6", 403, "developer"),
    ("/users/update/eab95dd2-8d2d-434e-9916-6d8608aca8e6", 404, "admin"),
    ("/users/update/eab95dd2-8d2d-434e-9916-6d8608aca8e6", 404, "manager"),
]
