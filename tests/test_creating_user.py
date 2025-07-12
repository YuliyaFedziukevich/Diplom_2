import allure
import pytest
from helper.api_requests import user_creating
from data.responses import user_already_exists, required_fields

class TestCreatingUser:
    @allure.title('Успешная регистрация пользователя, ручка - /api/auth/register')
    def test_successful_creating_user(self, create_and_delete_user):
        last_response, _ = create_and_delete_user
        with allure.step('Проверка, что код статуса ответа - 200'):
            assert last_response.status_code == 200
        with allure.step('Проверка, что в теле ответа - ("success": true)'):
            assert last_response.json().get('success')


    @allure.title('Тест на проверку невозможности создания двух идентичных пользователей, ручка - /api/auth/register')
    def test_impossible_to_create_two_identical_users(self, create_and_delete_user):
        last_response, created_user = create_and_delete_user
        with allure.step('В случае успешного создания первого пользователя, попытка создания второго идентичного пользователя'):
            last_response_2 = user_creating(created_user)
        with allure.step('Проверка, что код статуса ответа - 403'):
            assert last_response_2.status_code == 403
        with allure.step('Проверка, что тело ответа - {"success": False, "message": "User already exists"}'):
            assert last_response_2.json() == user_already_exists


    @allure.title('Тест на проверку невозможности создания пользователя без одного из обязательных полей (email, password, name), ручка - ручка - /api/auth/register')
    @pytest.mark.parametrize(
        'missing_field', ['email', 'password', 'name'])
    def test_impossible_to_create_courier_without_one_of_required_fields(self, missing_field, generator_user_data):
        with allure.step('Генерирование данных пользователя'):
            user_data = {
            'email': generator_user_data['email'],
            'password': generator_user_data['password'],
            'name': generator_user_data['name']}
        with allure.step('Удаление одного из полей в данных пользователя'):
           user_data[missing_field] = ''
        with allure.step('Создание пользователя'):
            last_response = user_creating(user_data)
        with allure.step('Проверка, что код статуса ответа - 403'):
            assert last_response.status_code == 403
        with allure.step('Проверка, что тело ответа - {"success": False, "message": "Email, password and name are required fields"}'):
            assert last_response.json() == required_fields

    @allure.title('Тест на проверку невозможности создания пользователя без обязательных полей, ручка - ручка - /api/auth/register')
    def test_impossible_to_create_courier_without_required_fields(self):
        with allure.step('Удаление всех полей в данных пользователя'):
            user_data = {'email': '', 'password': '', 'name': ''}
        with allure.step('Создание пользователя'):
            last_response = user_creating(user_data)
        with allure.step('Проверка, что код статуса ответа - 403'):
            assert last_response.status_code == 403
        with allure.step(
                'Проверка, что тело ответа - {"success": False, "message": "Email, password and name are required fields"}'):
            assert last_response.json() == required_fields
