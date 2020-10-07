import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


class DriverAction:

    def __init__(self, driver, timeout=None):
        self.driver = driver
        if timeout == None:
            self.timeout = 30
        else:
            self.timeout = timeout

    def wait(self, method, timeout=None):
        global e
        if(timeout==None):
            timeout = self.timeout

        end = time.time()+ timeout

        while(end > time.time()):
            try:
                return method()
            except Exception as e:
                pass
        raise TimeoutException(e)

    def _silent_scroll_to(self, element):
        try:
            action_chains = ActionChains(self.driver)
            action_chains.move_to_element(element).perform()
        except Exception:
            pass
        return element

    def click_button(self, xpath, timeout=None):
        def method():
            self._silent_scroll_to(self.driver.find_element_by_xpath(xpath=xpath)).click()

        self.wait(method=method, timeout=timeout)

    def fill_field(self, field_xpath, value, timeout=None):
        def input_in_field():
            field = self.driver.find_element_by_xpath(field_xpath)
            field.clear()
            field.send_keys(value)

        return self.wait(method=input_in_field, timeout=timeout)

    def go_to_web(self, web):
        self.driver.get(web)

    def switch_window(self, i=1):
        self.wait(lambda: len(self.driver.wrapped_driver.window_handles) > i)
        self.driver.wrapped_driver.switch_to.window(self.driver.wrapped_driver.window_handles[i])
