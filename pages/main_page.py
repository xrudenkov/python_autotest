from pages.base_page import BasePage


class MainPage(BasePage):
    """
    Главная страница
    """

    # меню
    # Информация об устройствах
    BUTTON_1 = {"name": "Информация об устройствах", "xpath": "//span[text()='Информация об устройствах']"}
    BUTTON_2 = {"name": "Данные об устройстве", "xpath": "//span[text()='Данные об устройстве']"}
    BUTTON_3 = {"name": "Сообщения", "xpath": "//span[text()='Сообщения']"}
    BUTTON_4 = {"name": "Звонки", "xpath": "//span[text()='Звонки']"}
    BUTTON_5 = {"name": "Местоположения", "xpath": "//span[text()='Местоположения']"}
    BUTTON_6 = {"name": "Действия", "xpath": "//span[text()='Действия']"}
    BUTTON_7 = {"name": "События", "xpath": "//span[text()='События']"}

    # Управление устройствами
    BUTTON_8 = {"name": "Управление устройствами", "xpath": "//span[text()='Управление устройствами']"}
    BUTTON_9 = {"name": "Команды", "xpath": "//span[text()='Команды']"}
    BUTTON_10 = {"name": "Профили", "xpath": "//span[text()='Профили']"}

    # Приложения
    BUTTON_11 = {"name": "Приложения", "xpath": "//span[text()='Приложения']"}
    BUTTON_12 = {"name": "Установленные приложения", "xpath": "//span[text()='Установленные приложения']"}
    BUTTON_13 = {"name": "Правила управления", "xpath": "//span[text()='Правила управления']"}
    BUTTON_14 = {"name": "Конфигурации", "xpath": "//span[text()='Конфигурации']"}

    # Лицензия
    BUTTON_15 = {"name": "Лицензия", "xpath": "//span[text()='Лицензия']"}
