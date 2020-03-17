from selenium.webdriver.support.abstract_event_listener import AbstractEventListener


class LoggedListener(AbstractEventListener):

    # Example for listener
    # for full methods list see superclass
    def before_navigate_to(self, url, driver):
        print('\nПопытка перехода на страницу {}'.format(url))

    def after_navigate_to(self, url, driver):
        print('Совершен переход на страницу {}'.format(url))

    def after_find(self, by, value, driver):
        print('Найден элемент By.{0} value:{1}'.format(by, value))

    def before_find(self, by, value, driver):
        print('Попытка найти элемент By.{0} value:{1}'.format(by, value))
