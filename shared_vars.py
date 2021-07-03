import allure

from pages.auth_page import AuthPage
from pages.base_page import BasePage
from pages.license_page import LicensePage
from pages.main_page import MainPage

DRIVER = None
PAGE = None

APPLICATION_PROPERTIES = {}

PAGES = {
    'Базовая страница': BasePage,
    'Форма авторизации': AuthPage,
    'Главная страница': MainPage,
    'Лицензия': LicensePage,
}


def set_page(name):
    PAGE = PAGES[name]()
    with allure.step(f"Установлена страница - {name}"):
        return PAGE
