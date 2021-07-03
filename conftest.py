import os
import sys
import allure
import shared_vars
import logging

from selenium.webdriver.remote.remote_connection import LOGGER
from allure_commons.types import AttachmentType
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from core.logger_listener import LoggedListener

PROJECT_ROOT = os.path.dirname(__file__)

CHROME_DRIVER_DICT = {
    'linux': os.path.join(PROJECT_ROOT, 'webdrivers/chrome/chromedriver_linux64'),
    'darwin': os.path.join(PROJECT_ROOT, 'webdrivers/chrome/chromedriver_mac'),
    'win32': os.path.join(PROJECT_ROOT, 'webdrivers/chrome/chromedriver_win32_64.exe'),
    'win64': os.path.join(PROJECT_ROOT, 'webdrivers/chrome/chromedriver_win32_64.exe')
}

OPERA_DRIVER_DICT = {
    'linux': os.path.join(PROJECT_ROOT, 'webdrivers/opera/operadriver_linux64'),
    'darwin': os.path.join(PROJECT_ROOT, 'webdrivers/opera/operadriver_mac64'),
    'win32': os.path.join(PROJECT_ROOT, 'webdrivers/opera/operadriver_win32.exe'),
    'win64': os.path.join(PROJECT_ROOT, 'webdrivers/opera/operadriver_win64.exe'),
}

YANDEX_DRIVER_DICT = {
    'linux': os.path.join(PROJECT_ROOT, 'webdrivers/yandex/yandexdriver-21.2.1.94-linux'),
    'darwin': os.path.join(PROJECT_ROOT, 'webdrivers/chrome/chromedriver_mac'),
    'win32': os.path.join(PROJECT_ROOT, 'webdrivers/yandex/yandexdriver-21.3.0.673-win.exe'),
    'win64': os.path.join(PROJECT_ROOT, 'webdrivers/yandex/yandexdriver-21.3.0.673-win.exe'),
}


@fixture()
def start_browser():

    with open(os.path.join(PROJECT_ROOT, 'app.properties')) as properties:
        for line in properties:
            key, value = line.split("=", 1)
            shared_vars.APPLICATION_PROPERTIES[key.strip()] = value.strip()

    browser_name = shared_vars.APPLICATION_PROPERTIES.get('browser')

    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('lang=ru')

    if browser_name == 'chrome':
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_DICT[sys.platform], options=options)
    elif browser_name == 'opera':
        driver = webdriver.Opera(executable_path=OPERA_DRIVER_DICT[sys.platform], options=options)
        driver.maximize_window()
    elif browser_name == 'yandex':
        driver = webdriver.Opera(executable_path=YANDEX_DRIVER_DICT[sys.platform], options=options)
        driver.maximize_window()
    else:
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_DICT[sys.platform], options=options)

    listener = LoggedListener()
    shared_vars.DRIVER = EventFiringWebDriver(driver=driver, event_listener=listener)

    LOGGER.setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    yield

    if sys.exc_info():
        allure.attach(body=shared_vars.DRIVER.get_screenshot_as_png(),
                      name='screenshot',
                      attachment_type=AttachmentType.PNG)

    shared_vars.DRIVER.quit()
