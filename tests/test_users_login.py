import allure
from helper.api_requests import user_authorization

class TestUserLogin:
    @allure.title('Успешный вход в аккаунт под существующим пользователем с корректными данными, ручка - /api/auth/login')
    def test_successful_sign_in_under_existing_user(self, create_and_delete_user):
        _, user_data = create_and_delete_user
        with allure.step('Получение данных созданного пользователя для авторизации'):
            payload = {
                'email': user_data['email'],
                'password': user_data['password']}
        last_response = user_authorization(payload)
        with allure.step('Проверка, что код статуса ответа - 200'):
            assert last_response.status_code == 200
        with allure.step('Проверка, что в теле ответа - ("success": true)'):
            last_response_json = last_response.json()
            assert last_response_json.get('success')
            assert last_response_json.get('user') == {'email': user_data['email'], 'name': user_data['name']}


    @allure.title('Тест, что невозможно войти в аккаунт под существующим пользователем, но с неверным логином и паролем, ручка - /api/auth/login')
    def test_impossible_sign_in_with_false_login_and_password(self, create_and_delete_user):
        _, user_data = create_and_delete_user
        with allure.step('Изменение данных созданного пользователя для авторизации'):
            payload = {
                'email': 'm' + user_data['email'],
                'password': user_data['password'] + '_modified'}
        with allure.step('Авторизация пользователя с измененными логином и паролем'):
            last_response = user_authorization(payload)
        with allure.step('Проверка, что код статуса ответа - 401'):
            assert last_response.status_code == 401
        with allure.step('Проверка, что в теле ответа - ("success": false,"message": "email or password are incorrect")'):
            assert last_response.json() == {"success": False,"message": "email or password are incorrect"}
