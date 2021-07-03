from pages.base_page import BasePage


class LicensePage(BasePage):
    """
    Страница Лицензия
    """
    BUTTON_1 = {"name": "Поле ввода лицензии", "xpath": "//textarea[@name='token']"}
    BUTTON_2 = {"name": "Сохранить", "xpath": "//span[text()='Сохранить' and @id='sp-savebutton-3091-btnInnerEl']"}
    BUTTON_3 = {"name": "Срок действия лицензии",
                "xpath": "//*[contains(text(), 'Лицензия для OOO «НИИ СОКБ»') and "
                         "contains(text(), 'действует с 01.01.2021 по 01.01.2022')]"}
