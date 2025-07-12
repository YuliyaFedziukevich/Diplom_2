main_url = 'https://stellarburgers.nomoreparties.site'

class API:
    creating_user = f'{main_url}/api/auth/register'
    user_login = f'{main_url}/api/auth/login'
    delete_user = f'{main_url}/api/auth/user'
    get_ingredients_data = f'{main_url}/api/ingredients'
    creating_order = f'{main_url}/api/orders'