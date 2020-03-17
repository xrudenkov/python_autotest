import allure
import tests_data.shared_variables

from linked_list import linked_list


def go_to_page(page_name):
    tests_data.shared_variables.PAGE = linked_list.get(page_name)()


@allure.step('Нажать на кнопку попап {button_name} на странице.')
def click_button_by_name(button_name):
    """Клик по названию кнопки.

    Args:
        button_name: название кнопки.
    """
    page = tests_data.shared_variables.PAGE
    button_locator = page.get_locator_by_name(element_name=button_name)
    if button_locator is None:
        button_locator = page.UNIVERSAL_BUTTON_XPATH
    button_locator = page.format_locator(locator=button_locator, button_name=button_name)
    page.click_button(locator=button_locator)


@allure.step('Согласие на обработку персональных данных.')
def click_processing_of_my_personal_data():
    java_script = "document.getElementsByClassName('form__row nice-checkbox').item(0).click();"
    tests_data.shared_variables.DRIVER.execute_script(java_script)


@allure.step('Согласие на обработку персональных данных для резерва.')
def click_processing_of_personal_data_for_the_reserve():
    java_script = "document.getElementsByClassName('form__row nice-checkbox').item(1).click();"
    tests_data.shared_variables.DRIVER.execute_script(java_script)


@allure.step('Выбор значения {value} из выпдающего списка select\'а {select_name}.')
def select_item_by_name(select_name, value):
    """Выбор значения выпадающего списка select.

   Args:
       select_name: название select,
       value: вводимое значение.
    """
    page = tests_data.shared_variables.PAGE
    select_locator = page.get_locator_by_name(element_name=select_name)
    if select_locator is None:
        select_locator = page.UNIVERSAL_SELECT_XPATH
    select_locator = page.format_locator(locator=select_locator, select_name=select_name)
    page.select_drop_down_and_click(select_locator=select_locator, value=value)


@allure.step('Заполнить поле формы {field_name} значением {value}.')
def fill_field_by_name(field_name, value):
    """Ввод значения в поле формы.

    Args:
        field_name: название поля,
        value: вводимое значение.
    """
    page = tests_data.shared_variables.PAGE
    field_locator = page.get_locator_by_name(element_name=field_name)
    if field_locator is None:
        field_locator = page.UNIVERSAL_INPUT_XPATH
    field_locator = page.format_locator(locator=field_locator, field_name=field_name)
    page.fill_field(field_locator=field_locator, value=value)
