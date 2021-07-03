from typing import Dict

from core.driver_action import DriverAction


class BasePage(DriverAction):
    """
    Основная страница
    """
    UNIVERSAL_INPUT_XPATH = {'name': 'Универсальный локатор для полей ввода',
                             'xpath': '(//*[@placeholder="{field_name}"])[last()]'}
    UNIVERSAL_BUTTON_XPATH = {'name': 'Универсальный локатор для кнопок',
                              'xpath': '//*[text()="{button_name}"]'}
    UNIVERSAL_SELECT_XPATH = {'name': 'Универсальный локатор для поля выбора',
                              'xpath': '(//div/span[text()="{select_name}"])[last()]'}
    UNIVERSAL_ELEMENT_WITH_TEXT = {
        'name': 'Элемент с текстом "{text}"',
        'xpath': '//*[contains(normalize-space(translate(text(), "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRS'
                 'TUVWXYZ", "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz")), "{text}")]'}
    UNIVERSAL_DROP_DOWN_XPATH = {'name': 'Универсальный локатор для всплывающего поля',
                                 'xpath': './/li[contains(.,"{value}")]'}

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
