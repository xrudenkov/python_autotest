from pages.global_header import GlobalHeader


class NextStepsPage(GlobalHeader):
    AUTH_FORM_LOGIN_XPATH = {'name': 'email',
                             'xpath': '//input[@name="email"]'}
    AUTH_FORM_PASS_XPATH = {'name': 'password',
                            'xpath': '//input[@name="password"]'}

    PAGE_MENU = {'name': 'Кнопка главного меню "{name_page}"',
                 'xpath': '//*[@id="mobile-frame__scroll"]//*[contains(text(), "{name_page}")]'}

    ITEM_MENU = {'name': 'Кнопка главного меню "{name_item}"',
                 'xpath': '//li/a[contains(text(), "{name_item}")]'}
