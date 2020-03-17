import allure

from pages.base_page import BasePage


class GlobalHeader(BasePage):
    """Шапка сайта."""

    PAGE_MENU = {'name': 'Кнопка главного меню "{name_page}"',
                 'xpath': '//*[@id="menu__navigation"]/li/*[text()="{name_page}"]'}

    ITEM_MENU = {'name': 'Кнопка главного меню "{name_item}"',
                 'xpath': '//li/a[text()="{name_item}"]'}

    COURSERA_LABEL = {'name': 'Лэйбл на странице Coursera', 'xpath': '//h1//img[@alt="Coursera"]'}
    SBERSTART_LABEL = {'name': 'Текст на странице SberStart', 'xpath': '//div[text="SberStart"]'}

    def go_to_page_from_top_menu(self, name_page, name_item=None):
        """Переход из меню навигации в любой раздел.

        Args:
            name_page: название страницы на которую надо перейти.
        """
        with allure.step(f'Переход из меню навигации в пункт "{name_page}"'):
            locator = self.format_locator(locator=self.PAGE_MENU, name_page=name_page)
            if name_item is not None:
                self.click_button(locator=locator)
                self.scroll_to(locator=locator)
                locator_item = self.format_locator(locator=self.ITEM_MENU, name_item=name_item)
                self.click_button(locator=locator_item)
            else:
                self.click_button(locator=locator)
