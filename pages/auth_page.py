from pages.base_page import BasePage


class AuthPage(BasePage):
    """
    СТраница Авторизации
    """
    LOGIN = {'name': 'Имя пользователя', 'xpath': "//input[@id='username']"}
    PASSWORD = {'name': 'Пароль', 'xpath': "//input[@id='password']"}
    ENTER = {'name': 'Войти', 'xpath': "//input[@value='Войти']"}
    RUSSIAN_LANG = {"name": "ru", "xpath": "//button[text()='Русский']"}
    ENGLISH_LANG = {"name": "en", "xpath": "//button[text()='English']"}
