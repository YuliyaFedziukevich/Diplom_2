**Тестовые сценарии**:
* 1 "Создание пользователя"
* 2 "Логин пользователя"
* 3 "Создание заказа"

**Перечень папок и файлов**:
* 1 **data**:
* - api.py - перечень используемых при тестировании api;
* 2 **helper**:
* - api_requests - перечень запросов API;
* - data_generator.py - содержит методы для генерирования данных;
* 3 **tests**:
* 3.1 **test_creating_user** - содержит тесты по созданию пользователя:
* - test_successful_creating_user;
* - test_impossible_to_create_two_identical_users;
* - test_impossible_to_create_courier_without_one_of_required_fields; 
* - test_impossible_to_create_courier_without_required_fields
* 3.2 **test_users_login** - содержит тесты касательно авторизации пользователя:
* - test_successful_sign_in_under_existing_user;
* - test_impossible_sign_in_with_false_login_and_password;
* 3.3 **test_creating_order** - содержит тесты по созданию заказа:
* - test_successful_creating_order_with_authorization;
* - test_impossible_creating_order_without_authorization; 
* - test_successful_creating_order_with_ingredients
* - test_impossible_creating_order_without_ingredients;
* - test_impossible_creating_order_with_invalid_hash_of_ingredients. 
* 4 **conftest.py** - содержит фикстуры; 
* 5 **requirements.txt** - файл с внешними зависимостями;
* 6 **allure_report** - сгенерированный Allure-отчёт