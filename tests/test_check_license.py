import allure
import pytest
import shared_vars

from allure_commons.types import Severity
from steps import common_steps


LICENSE = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJPT08gwqvQndCY0Jgg0KHQntCa0JHCuyIsImF1ZCI6Ik9PTyDCq9Cd0Jj" \
          "QmCDQodCe0JrQkcK7IiwibmJmIjoxNjA5NDU5MjAwLCJtY2MtbGltaXQiOjEwMDAsImlzcyI6Ik9PTyDCq9Cd0JjQmCDQodCe0JrQkcK" \
          "7IiwiZXhwIjoxNjQwOTk1MjAwLCJpYXQiOjE2MDk3NjkxMzQsImp0aSI6IjIzMDBjNDBmLWRiZGMtNDRjOC05MWVmLTI1NGY3YTc3YzE" \
          "2YiJ9.LQ2pio4_-oJIS7UrhQQziFUq8giRaxWZyjl3bvJgx8nBiHaUq2viVaiZyX5x0BObvAIiZpoKGL9Tds_hcI_yG56QzqGAfvW3lp" \
          "jyJeaEGaeMcUM1L5vDRL051Ku1D48dbwHnqx2e2cG6Dh2H4yzhII3lxZeeRkmXzq9aacyoYZNouVS-3912ZQG7pbblWg39V2n4erh7wV" \
          "46gFn4V3EyJaMhcledtNtkXswGxVU40ipWTtaKvqw9aUA15IaVmJk580XXw8rpNemTF4grZpxn9c6QV3AopVBidi6yRuYNLJ-CsXXuqm" \
          "m_hSFVTbNw3QLYIyb4jUmrbWGYUz8DIeIkFA"


@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.usefixtures("start_browser")
@allure.title('Проверка лицензии')
@allure.severity(Severity.MINOR)
@allure.feature('License')
def test_check_license():
    common_steps.auth()
    page = shared_vars.set_page("Главная страница")
    page.click_button(locator=page.get_locator_by_name("Лицензия"))
    page = shared_vars.set_page("Лицензия")
    page.fill_field(locator=page.get_locator_by_name("Поле ввода лицензии"), value=LICENSE)
    page.click_button(locator=page.get_locator_by_name("Сохранить"))
    page.get_element(locator=page.get_locator_by_name("Срок действия лицензии"))
