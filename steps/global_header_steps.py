import allure
import tests_data.shared_variables


@allure.step('Перейти на страницу {name_page} через меню навигации.')
def go_to_page_from_top_menu(name_page, name_item=None):
    """Метод осуществляет переход из меню навигации.

    Метод осуществляет переход из меню навигации по названию страницы.

    Args:
        name_page: название страницы для перехода.
        name_item: пункт меню для перехода.
    """
    page = tests_data.shared_variables.PAGE
    page.go_to_page_from_top_menu(name_page=name_page, name_item=name_item)
    page.wait_dom_not_changed()
    if name_item == 'Coursera' or name_item == 'SberStart':
        label_locator = page.COURSERA_LABEL if 'Coursera' else page.SBERSTART_LABEL
        page.switch_window(1)
        page.wait_element(locator=label_locator)
        page.switch_window(0)
    page.wait_dom_not_changed()

