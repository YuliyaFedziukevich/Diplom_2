import allure
from helper.api_requests import order_creating

class TestCreatingOrder:
    @allure.title('Успешное создание заказа авторизованным пользователем, ручка - /api/orders')
    def test_successful_creating_order_with_authorization(self, create_authorize_and_delete_user, get_ingredients_list):
        with allure.step('Получение id ингредиентов, которые будут использованы при создании заказа'):
            ingredient_id_0 = get_ingredients_list[0]['_id']
            ingredient_id_1 = get_ingredients_list[3]['_id']
            order_id = [ingredient_id_0, ingredient_id_1]
        # Создание заказа
        response = order_creating(create_authorize_and_delete_user, order_id)
        with allure.step('Проверка, что код статуса ответа - 200'):
            assert response.status_code == 200
        with allure.step('Проверка, что в теле ответа - ("success": true)'):
            assert response.json().get('success')


    @allure.title('Успешное создание заказа неавторизованным пользователем, ручка - /api/orders')
    def test_successful_creating_order_without_authorization(self, get_ingredients_list):
        with allure.step('Получение id ингредиентов, которые будут использованы при создании заказа'):
            ingredient_id_0 = get_ingredients_list[0]['_id']
            ingredient_id_1 = get_ingredients_list[3]['_id']
            order_id = [ingredient_id_0, ingredient_id_1]
        with allure.step('Создание заказа'):
            response = order_creating(None, order_id)
        with allure.step('Проверка, что код статуса ответа - 200'):
            assert response.status_code == 200
        with allure.step('Проверка, что в теле ответа - ("success": true)'):
            assert response.json().get('success')


    @allure.title('Успешное создание заказа с ингредиентами, ручка - /api/orders')
    def test_successful_creating_order_with_ingredients(self, create_authorize_and_delete_user, get_ingredients_list):
        with allure.step('Получение id ингредиентов, которые будут использованы при создании заказа'):
            order_id = [get_ingredients_list[0]['_id'], get_ingredients_list[1]['_id'], get_ingredients_list[2]['_id'],
                get_ingredients_list[3]['_id'], get_ingredients_list[4]['_id'], get_ingredients_list[5]['_id']]
        with allure.step('Создание заказа'):
            response = order_creating(create_authorize_and_delete_user, order_id)
        with allure.step('Проверка, что код статуса ответа - 200'):
            assert response.status_code == 200
        with allure.step('Проверка, что в теле ответа - ("success": true)'):
            assert response.json().get('success')


    @allure.title('Невозможно создание заказа без ингредиентов , ручка - /api/orders')
    def test_impossible_creating_order_without_ingredients(self, create_authorize_and_delete_user):
        order_id = []
        with allure.step('Создание заказа авторизованным пользователем без ингредиентов'):
            response = order_creating(create_authorize_and_delete_user, order_id)
        with allure.step('Проверка, что код статуса ответа - 400'):
            assert response.status_code == 400
        with allure.step('Проверка, что в теле ответа - {"success": false, "message": "Ingredient ids must be provided"}'):
            assert response.json() == {'success': False, 'message': 'Ingredient ids must be provided'}


    @allure.title('Невозможно создание заказа с неверным хешем ингредиентов, ручка - /api/orders')
    def test_impossible_creating_order_with_invalid_hash_of_ingredients(self, create_authorize_and_delete_user, get_ingredients_list):
        with allure.step('Получение id ингредиентов, которые будут использованы при создании заказа'):
            ingredient_id_0 = get_ingredients_list[0]['_id']
            ingredient_id_1 = get_ingredients_list[1]['_id']
            order_id_changed = [f'{ingredient_id_0}1', f'{ingredient_id_1}a']
        with allure.step('Создание заказа'):
            response = order_creating(create_authorize_and_delete_user, order_id_changed)
        with allure.step('Проверка, что код статуса ответа - 500'):
            assert response.status_code == 500
