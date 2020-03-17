import time
import allure
import tests_data.constants
import tests_data.shared_variables

from typing import List, Dict
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebElement
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from core.utils_functions import wait_until


class BasePage:

    UNIVERSAL_INPUT_XPATH = {'name': 'Универсальный локатор для полей ввода',
                             'xpath': '(//*[@placeholder="{field_name}"])[last()]'}
    UNIVERSAL_BUTTON_XPATH = {'name': 'Универсальный локатор для кнопок', 'xpath': '//*[text()="{button_name}"]'}
    UNIVERSAL_SELECT_XPATH = {'name': 'Универсальный локатор для поля выбора',
                              'xpath': '(//div/span[text()="{select_name}"])[last()]'}
    UNIVERSAL_ELEMENT_WITH_TEXT = {
        'name': 'Элемент с текстом "{text}"',
        'xpath': '//*[contains(normalize-space(translate(text(), "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRS'
                 'TUVWXYZ", "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz")), "{text}")]'}
    UNIVERSAL_DROP_DOWN_XPATH = {'name': 'Универсальный локатор для всплывающего поля',
                                 'xpath': './/li[contains(.,"{value}")]'}

    def __init__(self):
        self.driver = tests_data.shared_variables.DRIVER
        self.timeout = tests_data.constants.TIMEOUT

    def wait_driver_until(self, method, message, timeout=None):
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(method, message)

    def get_locator_by_name(self, element_name):
        """Получение locator'а по ключу в словаре класса страницы.

        Args:
            element_name: ключ для поиска xpath'а среди словарей класса.

        Returns:
            locator: locator вэб-элемента.
        """
        locator_dict = []
        for attribute_name in dir(self):
            attribute = getattr(self, attribute_name)

            if isinstance(attribute, dict) and attribute:
                attr_name = attribute.get('name')

                if attr_name == element_name:
                    locator_dict.append(attribute)

        assert len(locator_dict) <= 1, f'В классе "{self}" более одного локатора "{element_name}"'
        return locator_dict[0] if locator_dict else None

    def _silent_scroll_to(self, element: WebElement):
        """Метод пытается переместиться к элементу, в случае ошибка она игнорируется

        Args:
            element: объект элемента
        """
        try:
            action_chains = ActionChains(self.driver)
            action_chains.move_to_element(element).perform()
        except Exception as exc:
            print(exc)
            pass
        return element

    def get_element(self, locator) -> WebElement:
        with allure.step(f'получить элемент {locator["name"]}:{locator["xpath"]}'):
            return self._silent_scroll_to(self.driver.find_element_by_xpath(locator["xpath"]))

    def get_elements(self, locator) -> List[WebElement]:
        with allure.step(f'получение элементы {locator["xpath"]}:{locator["xpath"]}'):
            return self.driver.find_elements_by_xpath(locator['xpath'])

    def wait_element(self, locator, timeout=None) -> WebElement:
        with allure.step(f'ждать элемент {locator["name"]}:{locator["xpath"]}'):
            return self._silent_scroll_to(
                self.wait_driver_until(
                    method=expected_conditions.presence_of_element_located((By.XPATH, locator['xpath'])),
                    message=f'Элемент {locator["name"]}:{locator["xpath"]} отсутствует на странице',
                    timeout=timeout))

    def wait_elements(self, locator, timeout=None) -> WebElement:
        with allure.step(f'ждать элементы {locator["xpath"]}:{locator["xpath"]}'):
            return self.wait_driver_until(
                method=expected_conditions.presence_of_all_elements_located((By.XPATH, locator['xpath'])),
                message=f'Элементы {locator["xpath"]}:{locator["xpath"]} отсутствуют на странице',
                timeout=timeout)

    def wait_visibility_of_any_elements(self, locator, timeout=None):
        with allure.step(f'ждать видимости любого из элементов {locator["name"]}:{locator["xpath"]}'):
            return self.wait_driver_until(
                method=expected_conditions.visibility_of_any_elements_located((By.XPATH, locator['xpath'])),
                message=f'Элемент {locator["xpath"]}:{locator["xpath"]} не отображается на странице',
                timeout=timeout)

    def wait_invisibility_of_element(self, locator, timeout=None) -> WebElement:
        with allure.step(f'ждать невидимости элемента {locator["name"]}:{locator["xpath"]}'):
            return self.wait_driver_until(
                method=expected_conditions.invisibility_of_element_located(locator['xpath']),
                message=f'Элемент {locator["name"]}:{locator["xpath"]} не исчез',
                timeout=timeout)

    def wait_visibility_of_all_elements(self, locator, timeout=None) -> List[WebElement]:
        with allure.step(f'ждать видимости элементов {locator["name"]}:{locator["xpath"]}'):
            return self.wait_driver_until(
                method=expected_conditions.visibility_of_all_elements_located((By.XPATH, locator['xpath'])),
                message=f'Элементы {locator["name"]}:{locator["xpath"]} не появились на странице',
                timeout=timeout)

    def wait_text_to_be_present_in_element(self, locator, text, timeout=None):
        return self.wait_driver_until(
            method=expected_conditions.text_to_be_present_in_element((By.XPATH, locator['xpath']), text),
            message=f'Текст "{text}" отсутствует в элементе "{locator["name"]}":{locator["xpath"]}',
            timeout=timeout)

    def wait_text_not_to_be_present_in_element(self, locator, text, timeout=None):
        return self.wait_driver_until(
            method=expected_conditions.text_to_be_present_in_element((By.XPATH, locator['xpath']), text),
            message=f'Текст "{text}" присутсвует в элементе "{locator["name"]}":{locator["xpath"]}',
            timeout=timeout)

    def wait_text_to_be_present_in_element_value(self, locator, text, timeout=None):
        return self.wait_driver_until(
            method=expected_conditions.text_to_be_present_in_element_value((By.XPATH, locator['xpath']), text),
            message=f'Текст "{text}" отсутствует в свойстве value элемента "{locator["name"]}":{locator["xpath"]}',
            timeout=timeout)

    def wait_element_to_be_clickable(self, locator, timeout=None):
        return self.wait_driver_until(method=expected_conditions.element_to_be_clickable((By.XPATH, locator['xpath'])),
                                      timeout=timeout,
                                      message=f'Элемент "{locator["name"]}":{locator["xpath"]} не доступен для клика')

    def click_button(self, locator, timeout=None):
        def custom_waiter():
            self._silent_scroll_to(element=self.wait_element_to_be_clickable(locator=locator, timeout=timeout)).click()
            return True

        with allure.step(f'нажать кнопку "{locator["name"]}" с локатором "{locator["xpath"]}"'):
            wait_until(method=custom_waiter, message=f'"{locator["name"]}":{locator["xpath"]} не обнаружена',
                       timeout=timeout)

    def scroll_to(self, locator, timeout=None):
        with allure.step(f'Scroll до элемента "{locator["name"]}":{locator["xpath"]}'):
            def custom_wait():
                try:
                    action_chains = ActionChains(self.driver)
                    element = self.driver.wrapped_driver.find_element_by_xpath(locator['xpath'])
                    if not isinstance(element, (WebElement, EventFiringWebElement)):
                        raise AttributeError("move_to requires a WebElement")
                    action_chains.move_to_element(element).perform()
                    return True
                except Exception as exc:
                    print(type(exc), exc)
                    return False

            wait_until(method=custom_wait, message=f'Проскроллиться к элементу "{locator["name"]}" не удалось.',
                       timeout=timeout)

    def fill_field(self, field_locator, value, timeout=None):
        with allure.step(f'Заполнение поля "{field_locator["name"]}":"{field_locator["xpath"]}" Значением {value}'):

            def input_in_field():
                field = self.driver.find_element_by_xpath(field_locator['xpath'])
                field.clear()
                field.send_keys(value)
                field.send_keys(Keys.TAB)
                wait_until(lambda: field.find_element_by_xpath('//input[@class="is-valid"]'), timeout=2)
                return True

            return wait_until(method=input_in_field, timeout=timeout,
                              message=f'Поле "{field_locator["name"]}":{field_locator["xpath"]} не было заполнено')

    def fill_field_drop_down_and_click(self, field_locator, value, timeout=None):
        with allure.step('Заполнить поле и нажать на появившийся элемент'):
            drop_down_xpath = self.format_locator(locator=self.UNIVERSAL_DROP_DOWN_XPATH, value=value)

            def custom_wait():
                try:
                    self.fill_field(field_locator=field_locator, value=value, timeout=2)
                    self.wait_visibility_of_any_elements((By.XPATH, drop_down_xpath['xpath']), timeout=2)[0].click()
                    self.wait_text_to_be_present_in_element_value(locator=field_locator, text=value, timeout=2)
                    return True
                except Exception as exc:
                    print(exc)
                    return False
            wait_until(method=custom_wait, message='Не удалось заполнить поле.', timeout=timeout)

    def select_drop_down_and_click(self, select_locator, value, timeout=None):
        with allure.step('Заполнить поле и нажать на появившийся элемент'):
            drop_down_locator = self.format_locator(locator=self.UNIVERSAL_DROP_DOWN_XPATH, value=value)

            def custom_wait():
                try:
                    element = self.wait_element(locator=select_locator, timeout=2)
                    self.click_button(locator=select_locator, timeout=2)
                    self.click_button(locator=drop_down_locator, timeout=2)
                    return True if element.text == value else False
                except Exception as exc:
                    print(exc)
                    return False
            wait_until(method=custom_wait, message='Не выбрать значение.', timeout=timeout)

    def fill_field_and_send_enter(self, field_locator, value, timeout=None):
        self.fill_field(field_locator, value, timeout)
        self.get_element(field_locator).send_keys(Keys.ENTER)

    def fill_field_and_send_tab(self, field_locator, value, timeout=None):
        self.fill_field(field_locator, value, timeout)
        self.get_element(field_locator).send_keys(Keys.TAB)

    def wait_dom_not_changed(self):
        """Ожидание загрузки DOM модели, и проверка, что количество элементов не меняется на отрезке времени.
        """
        def check_equals():
            all_elements1 = self.driver.find_elements_by_xpath(xpath='//*')
            time.sleep(0.5)
            all_elements2 = self.driver.find_elements_by_xpath(xpath='//*')
            if len(all_elements1) == len(all_elements2):
                dom_load = True
            else:
                dom_load = False

            return dom_load

        wait_until(method=check_equals)

    # Проверяет на наличие текста на главной странице
    def wait_text_visibility(self, *text):
        for text in text:
            text_xpath = self.format_locator(locator=self.UNIVERSAL_ELEMENT_WITH_TEXT, text=text)
            self.wait_visibility_of_any_elements((By.XPATH, text_xpath['xpath']))

    # Проверяет на отсутствие текста на главной странице
    def wait_text_invisibility(self, *text):
        for text in text:
            text_xpath = self.format_locator(locator=self.UNIVERSAL_ELEMENT_WITH_TEXT, text=text)
            self.wait_invisibility_of_element((By.XPATH, text_xpath['xpath']))

    @staticmethod
    def accept_alert(decision, timeout=None):
        alert = wait_until(method=alert_is_present, message="Не обнаружено окно с уведомлением", timeout=timeout)
        alert.accept() if decision is True else alert.dismiss()

    def check_alert_message(self, msg):
        alert = self.driver.switch_to.alert
        assert alert.text == msg, 'Ожидаемое сообщение: ' + msg + 'Действительное сообщение: ' + alert.text

    def wait_frame(self, locator, timeout=None):
        self.wait_driver_until(
            method=expected_conditions.frame_to_be_available_and_switch_to_it(locator['xpath']),
            message=f'Фрейм "{locator["name"]}:{locator["xpath"]} не доступен для переключения на него',
            timeout=timeout)

    def switch_to_default_content(self):
        self.driver.wrapped_driver.switch_to_default_content()

    def switch_window(self, i=1):
        wait_until(lambda: len(self.driver.wrapped_driver.window_handles) > i)
        self.driver.wrapped_driver.switch_to.window(self.driver.wrapped_driver.window_handles[i])

    def check_value(self, element_locator, value: str = None, contains_value: str = None):
        """Проверить значение элемента на соответсвие ожидаемому.

        Args:
            element_locator: локатор.
            value: ожидаемое значение.
            contains_value: частичное соответствие значения элемента ожидаемому.
        """
        element = self.get_element(element_locator)
        error_message = ''
        if value:
            error_message = 'Полученное значение не соответсвует ожидаемому. Полученное: "{received_value}", ' \
                            'ожидаемое: "{expected_value}"'.format(received_value=element.get_attribute('value'),
                                                                   expected_value=value)
            assert value == element.get_attribute('value')
        elif contains_value:
            error_message = 'Полученное значение не содержит ожидаемое. Полученное: "{received_value}", ' \
                            'ожидаемое: "{expected_value}"'.format(received_value=element.get_attribute('value'),
                                                                   expected_value=contains_value)

        assert contains_value in element.get_attribute('value'), error_message

    def check_attribute(self, locator, attribute, expected_result='true'):
        """Проверка атрибута web-элемента.

        Args:
            locator: локатор.
            attribute: наименование аттрибута.
            expected_result: ожидаемый результат.
        """
        result = self.get_element(locator['xpath']).get_attribute(attribute)
        assert expected_result == result, "Элемент активен"

    def set_checkbox(self, checkbox_locator, value):
        with allure.step(f'установить checkbox "{checkbox_locator["name"]}" {checkbox_locator["xpath"]}:{value}'):
            self._silent_scroll_to(self.wait_element(checkbox_locator))
            checkbox = self.driver.find_element_by_xpath(checkbox_locator['xpath'])
            if not checkbox.is_selected() and value is True:
                checkbox.click()
            elif checkbox.is_selected() and value is False:
                checkbox.click()

    def select_by_value(self, select_locator, value):
        """Метод проставляет значение в выпадающем списке по значению - value вэб элемента

        Args:
            select_locator: локатор вэб элемента
            value: текстовое значение
        """
        with allure.step(f'установить select "{select_locator["name"]}" {select_locator["xpath"]}:{value}'):
            select_element = self._silent_scroll_to(self.wait_element(select_locator["xpath"]))
            Select(select_element).select_by_value(value)

    @staticmethod
    def format_locator(locator, **params):
        """Форматирование локатора

        Args:
            locator: Локатор вида:
            **params: Параметры для форматирования локатора.(Пример: {btn_name}="Имя кнопки")

        Returns:
            locator[0], locator_str: Форматированный локатор вида (By.XPATH, '//div[text()="Имя блока"]/..')
        """
        if isinstance(locator, Dict):
            new_locator = locator.copy()
            name = new_locator['name'].format(**params)
            new_locator['name'] = name
            xpath = new_locator['xpath'].format(**params)
            new_locator['xpath'] = xpath
            return new_locator

    def scroll_until_appearing_new_element(self, scroll_locator, new_locator):
        """Метод скроллится к элементу и смотрит появление нового элемента.

        Args:
            scroll_locator: локатор базового элемента.
            new_locator: локатор нового элемента.

        Returns:
            appeared_element: возвращает True, если элемент появился, иначе False.
        """
        with allure.step(f'Скролл к элементу"{scroll_locator["name"]}" и '
                         f'ожидание появления элемента "{new_locator["name"]}"'):
            self.scroll_to(locator=scroll_locator)
            if len(self.get_elements(locator=new_locator)) == 0:
                appeared_element = False
            else:
                self.click_button(locator=new_locator)
                appeared_element = True

            return appeared_element

    def click_until_appearing_new_element(self, button_locator, new_element, name=None):
        """Метод кликает по элементу и смотрит появление нового элемента.

        Args:
            button_locator: локатор базового элемента.
            new_element: локатор нового элемента.
            name: название локаторов.

        Returns:
            appeared_element: возвращает True, если элемент появился, иначе False.
        """
        with allure.step(f'Клик по элементу"{name[0]}" и ожидание появления элемента "{name[1]}"'):
            try:
                self.get_element(locator=button_locator).click()
            except Exception as e:
                print(e)
                pass
            if len(self.get_elements(locator=new_element)) == 0:
                appeared_element = False
            else:
                appeared_element = True

            return appeared_element

    def click_old_and_new_element(self, old_button, new_button):
        def custom_wait():
            if self.click_until_appearing_new_element(button_locator=old_button, new_element=new_button):
                time.sleep(1)
                try:
                    self.get_element(locator=new_button).click()
                    return True
                except Exception as e:
                    print(e)
                    return False
            else:
                return False

        wait_until(method=custom_wait, message='Не удалось кликнуть по новому элементу.', timeout=7)

    def click_until_disappearing(self, button_locator):
        try:
            self.get_element(locator=button_locator).click()
            return False
        except StaleElementReferenceException and NoSuchElementException:
            return True
