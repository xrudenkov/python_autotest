import allure

import shared_vars

"""
Общие шаги, которые часто используются в тестах
"""


def auth():
    """Авторизация на сайте
    """
    with allure.step("Авторизация на странице"):
        url = shared_vars.APPLICATION_PROPERTIES.get("url")
        login = shared_vars.APPLICATION_PROPERTIES.get("login")
        password = shared_vars.APPLICATION_PROPERTIES.get("password")
        page = shared_vars.set_page("Форма авторизации")
        page.go_to_url(url=url)
        page.fill_field(locator=page.get_locator_by_name("Имя пользователя"), value=login)
        page.fill_field(locator=page.get_locator_by_name("Пароль"), value=password)
        page.click_button(locator=page.get_locator_by_name("Войти"))
