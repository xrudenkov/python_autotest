import logging
import allure
import shared_vars

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from core.decorators import retry


class DriverAction:

    def __init__(self):
        self.driver = shared_vars.DRIVER

    def _silent_scroll_to(self, element):
        """Перемещение к элементу
        В случае ошибки она игнорируется

        :param element: элемент на странице
        :return: возвращает этот же элемент
        """
        try:
            action_chains = ActionChains(self.driver)
            action_chains.move_to_element(element).perform()
        except Exception as exc:
            logging.getLogger().debug(f"Перемещение к элементу не произошло - {exc}")
        return element

    @retry
    def click_button(self, locator):
        """Клик по элементу на странице

        :param locator: элемент на странице в виде имени(name) и расположения(xpath)
        """
        with allure.step(f'нажать на элемент "{locator["name"]}:{locator["xpath"]}"'):
            self._silent_scroll_to(element=self.driver.find_element_by_xpath(xpath=locator["xpath"])).click()

    @retry
    def fill_field(self, locator, value):
        """Заполнение значения в поле

        :param locator: элемент на странице в виде имени(name) и расположения(xpath)
        :param value: значение
        """
        with allure.step(f'ввести значение "{value}" в поле "{locator["name"]}:{locator["xpath"]}"'):
            field = self.driver.find_element_by_xpath(locator["xpath"])
            field.clear()
            field.send_keys(value)
            field.send_keys(Keys.TAB)

    @retry
    def get_element(self, locator):
        """Найти и вернуть элемент

        :param locator: элемент на странице в виде имени(name) и расположения(xpath)
        :return: элемент
        """
        with allure.step(f'получить элемент "{locator["name"]}:{locator["xpath"]}"'):
            return self._silent_scroll_to(self.driver.find_element_by_xpath(locator["xpath"]))

    def go_to_url(self, url):
        """Перейти на страницу по адресу
        
        :param url: адрес
        """
        with allure.step(f'перейти на страницу "{url}"'):
            self.driver.get(url)

    @retry
    def switch_window(self, i=1):
        """Переход на вкладку по номеру

        :param i: номер новой вкладки
        """
        with allure.step(f'перейти на вкладку под номером {i}'):
            self.driver.wrapped_driver.switch_to.window(self.driver.wrapped_driver.window_handles[i])

    @retry
    def switch_frame(self, locator):
        with allure.step(f'перейти на фрейм "{locator["name"]}: {locator["xpath"]}"'):
            it = expected_conditions.frame_to_be_available_and_switch_to_it(locator['xpath'])
            it(self.driver)

    @retry
    def switch_to_default_content(self):
        with allure.step('перейти на контент по умолчанию'):
            self.driver.wrapped_driver.switch_to_default_content()
