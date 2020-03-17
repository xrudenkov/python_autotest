import pytest
from steps import authorization_steps, global_header_steps, common_steps


@pytest.mark.smoke
def test_smoke(start_browser):

    # Переход на сайт NextSteps
    authorization_steps.authorization(website_name='NextSteps')

    # Переход в форму авторизации
    common_steps.click_button_by_name(button_name='Войти')
    common_steps.go_to_page(page_name='Форма авторизации')

    # Заполнение формы авторизации
    common_steps.fill_field_by_name(field_name='email', value="puti_1960@mail.ru")
    common_steps.fill_field_by_name(field_name='password', value="123456qwe")
    common_steps.click_button_by_name(button_name='Войти на портал')

    # Переход по всем страницам из меню сайта
    global_header_steps.go_to_page_from_top_menu(name_page='Возможности',
                                                 name_item='Продолжить работу в группе Сбербанк')
    global_header_steps.go_to_page_from_top_menu(name_page='Возможности',
                                                 name_item='Найти работу у партнеров')
    global_header_steps.go_to_page_from_top_menu(name_page='Возможности',
                                                 name_item='Получить денежную компенсацию')
    global_header_steps.go_to_page_from_top_menu(name_page='Возможности',
                                                 name_item='Открыть свой бизнес')
    global_header_steps.go_to_page_from_top_menu(name_page='Вакансии')
    global_header_steps.go_to_page_from_top_menu(name_page='Отклики и резюме',
                                                 name_item='Мои резюме')
    global_header_steps.go_to_page_from_top_menu(name_page='Отклики и резюме',
                                                 name_item='Мои отклики')
    global_header_steps.go_to_page_from_top_menu(name_page='Отклики и резюме',
                                                 name_item='Сохраненные вакансии')
    global_header_steps.go_to_page_from_top_menu(name_page='Отклики и резюме',
                                                 name_item='Добавить резюме')
    global_header_steps.go_to_page_from_top_menu(name_page='Отклики и резюме',
                                                 name_item='Импорт резюме из .doc')
    global_header_steps.go_to_page_from_top_menu(name_page='Статьи')
    global_header_steps.go_to_page_from_top_menu(name_page='Помощь')
    global_header_steps.go_to_page_from_top_menu(name_page='Контакты')
    global_header_steps.go_to_page_from_top_menu(name_page='Владимир',
                                                 name_item='Настройки')
    global_header_steps.go_to_page_from_top_menu(name_page='Владимир',
                                                 name_item='Выход')
