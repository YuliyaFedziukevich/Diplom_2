import allure
import requests
from data.api import API

@allure.step('Создание пользователя')
def user_creating(payload):
    return requests.post(API.creating_user, json=payload)

@allure.step('Авторизация пользователя')
def user_authorization(payload_authorize):
    return requests.post(API.user_login, json=payload_authorize)

@allure.step('Получение токена accessToken')
def get_token(response):
    return response.json().get('accessToken')

@allure.step('Удаление пользователя')
def user_delete(token):
    return requests.delete(API.delete_user, headers={'Authorization': token})

@allure.step('Получение списка ингредиентов')
def get_ingredients_data():
    return requests.get(API.get_ingredients_data)

@allure.step('Создание заказа')
def order_creating(header, id):
    return requests.post(API.creating_order,
                         headers = {'Authorization': header},
                         json = {'ingredients': id})