import allure
import tests_data.shared_variables

from pages.global_header import GlobalHeader
from tests_data.constants import get_url_data


def authorization(website_name):
    """Авторизация пользователя.

    Args:
        website_name: переменная для определения url. url возвращается методом get_url_data из constants.
    """
    with allure.step('Авторизоваться в системе'):
        tests_data.shared_variables.DRIVER.get(get_url_data(website_name=website_name))
        tests_data.shared_variables.PAGE = GlobalHeader()
