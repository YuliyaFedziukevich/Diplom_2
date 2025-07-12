import allure
import pytest
from helper.data_generator import DataGenerator
from helper.api_requests import user_creating, user_authorization, get_token, user_delete, get_ingredients_data

# Генерирование валидных данных для регистрации пользователя
@pytest.fixture(scope='function')
def generator_user_data():
    email = DataGenerator.email_generator()
    password= DataGenerator.password_generator()
    name = DataGenerator.name_generator()

    return {
        'email': email,
        'password': password,
        'name': name}

# Создание пользователя и его удаление
@pytest.fixture(scope='function')
def create_and_delete_user():
    with allure.step('Генерирование данных пользователя'):
        payload = {
            'email': DataGenerator.email_generator(),
            'password': DataGenerator.password_generator(),
            'name': DataGenerator.name_generator()}
    last_response = user_creating(payload)
    token = get_token(last_response)
    yield last_response, payload
    user_delete(token)

# Создание пользователя с авторизацией и его удаление
@pytest.fixture(scope='function')
def create_authorize_and_delete_user():
    with allure.step('Генерирование данных пользователя для регистрации'):
        payload_create = {
            'email': DataGenerator.email_generator(),
            'password' : DataGenerator.password_generator(),
            'name' : DataGenerator.name_generator()}
    with allure.step('Выделение данных пользователя для авторизации'):
        payload_authorize = {
            'email': payload_create['email'],
            'password': payload_create['password']}
    last_response = user_creating(payload_create)
    token = get_token(last_response)
    user_authorization(payload_authorize)
    yield token
    user_delete(token)

# Получение списка ингредиентов
@pytest.fixture(scope='session')
def get_ingredients_list():
    ingredients_list = get_ingredients_data()
    return ingredients_list.json()['data']
