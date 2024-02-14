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



test_get_all_customers_data = [
    ("/customers/get_all", 403, "developer"),
    ("/customers/get_all", 200, "admin"),
    ("/customers/get_all", 200, "manager"),

]


test_get_all_customers_by_id_data = [
    ("/specializations/get_by_id/1", 403, "developer"),
    ("/specializations/get_by_id/1", 200, "admin"),
    ("/specializations/get_by_id/1", 200, "manager"),
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
    ("/customers/soft_delete_api/1", 403, "developer"),
    ("/customers/soft_delete_api/1", 200, "admin"),
    ("/customers/soft_delete_api/1", 200, "manager"),
]


test_get_all_projects_data = [
    ("/project/", 403, "developer"),
    ("/project/", 200, "admin"),
    ("/project/", 200, "manager"),
]

test_create_project = [
    ("/project/", 403, "developer"),
    ("/project/", 200, "admin"),
    ("/project/", 200, "manager"),
]

