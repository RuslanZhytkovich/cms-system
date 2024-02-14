test_check_patch_data = [
    ("admin", {"email": "admin@mail.ru"}, 200),
    ("developer", {"email": "admin@mail.ru"}, 403),
    ("manager", {"email": "admin@mail.ru"}, 403),
]

test_change_bench_status_data = [
    ("/users/change_bench_status_api/1600", 400, "admin"),
    ("/users/change_bench_status_api/100", 403, "admin"),
    ("/users/change_bench_status_api/100", 403, "developer"),
    ("/users/change_bench_status_api/101", 200, "admin"),
    ("/users/change_bench_status_api/101", 403, "manager"),
]

test_get_all_users_data = [
    ("/users/get_all_users", 200, "admin"),
    ("/users/get_all_users", 200, "manager"),
    ("/users/get_all_users", 403, "developer"),
]

test_get_user_by_id = [
    ("/users/get_by_id/100", 200, "admin"),
    ("/users/get_by_id/100", 200, "manager"),
    ("/users/get_by_id/100", 403, "developer"),
    ("/users/get_by_id/228", 404, "admin"),
]

test_get_user_by_email = [
    ("/users/get_user_by_email/rzhitkovich@bk.ru", 403, "developer"),
    ("/users/get_user_by_email/rzhitkovich@bk.ru", 200, "admin"),
    ("/users/get_user_by_email/incorrect_email", 404, "admin"),
    ("/users/get_user_by_email/rzhitkovich@bk.ru", 200, "manager"),
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
]

test_get_specialization_by_id_data = [
    ("/specializations/get_by_id/1", 403, "developer"),
    ("/specializations/get_by_id/1", 200, "admin"),
    ("/specializations/get_by_id/1", 200, "manager"),
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
]

test_create_report = [
    ("/reports/create", 403, "developer"),
    ("/reports/create", 200, "admin"),
    ("/reports/create", 200, "manager"),
]
