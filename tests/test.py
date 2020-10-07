from core.driver_action import DriverAction

WEB_NAME = 'https://testing1.alytics.ru/projects'

DICT_XPATH = {
    'Логин': '//input[@name="login"]',
    'Пароль': '//input[@name="password"]',
    'Запомнить меня': '//input[@id="check2"]',
    'Войти': '//input[@value="Войти"]',
    'Добавить проект': '//a[text()="Добавить проект"]',
    'Название проекта': '//input[@class="text-input validate[required, maxSize[100]]"]',
    'Сайт': '//input[@class="text-input validate[required,custom[user_url], maxSize[100]]"]',
    'Выберите страну': '//a/span[text()="Выберите страну"]',
    'Россия': '//ul/li[text()="Россия"]',
    'Далее': '//input[@value="Далее"]',
    'Логин ЯндексДирект': '//input[@class="text-input validate[required,custom[yandex_direct_login], maxSize[100]]"]',
    'Войти[Яндекс]': '//button[@class="Button2 Button2_size_l Button2_view_action Button2_width_max Button2_type_submit"]',
    'Введите пароль': '//input[@type="password"]',
    'Все кампании аккаунта': '//input[@class="campaigns-method all-campaigns"]',
    'Логин[Google]': '//input[@aria-label="Телефон или адрес эл. почты"]',
    'Далее[Google]': '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc"]',
}


def get_xpath(name):
    return DICT_XPATH.get(name)


def test(start_browser):
    driver = DriverAction(driver=start_browser, timeout=15)
    driver.go_to_web(WEB_NAME)
    driver.fill_field(field_xpath=get_xpath("Логин"), value="oleg.rudenko.99992@mail.ru")
    driver.fill_field(field_xpath=get_xpath("Пароль"), value="rvKent13")
    driver.click_button(xpath=get_xpath("Запомнить меня"))
    driver.click_button(xpath=get_xpath("Войти"))
    driver.click_button(get_xpath('Добавить проект'))
    driver.fill_field(field_xpath=get_xpath("Название проекта"), value="Alytics_Test")
    driver.fill_field(field_xpath=get_xpath("Сайт"), value="Test.com")
    driver.click_button(xpath=get_xpath("Выберите страну"))
    driver.click_button(xpath=get_xpath("Россия"))
    driver.click_button(xpath=get_xpath("Далее"))
    driver.fill_field(field_xpath=get_xpath("Логин ЯндексДирект"), value="alytics.test.1")
    driver.click_button(xpath=get_xpath("Далее"))
    driver.switch_window(1)
    driver.click_button(xpath=get_xpath("Войти[Яндекс]"))
    driver.fill_field(field_xpath=get_xpath("Введите пароль"), value="qwertytest123")
    driver.click_button(xpath=get_xpath("Войти[Яндекс]"))
    driver.switch_window(0)
    driver.click_button(xpath=get_xpath("Все кампании аккаунта"))
    driver.click_button(xpath=get_xpath("Далее"))
    driver.click_button(xpath=get_xpath("Далее"))
    driver.switch_window(1)
    driver.fill_field(field_xpath=get_xpath("Логин[Google]"), value="pelmen322228@gmail.com")
    driver.click_button(xpath=get_xpath("Далее[Google]"))
    ### далее гугл всю малину подпортил)
