import os
import platform
import sys
import allure
import tests_data.shared_variables

from pytest import fixture
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from core.logger_listener import LoggedListener
from pyvirtualdisplay import Display

PROJECT_ROOT = os.path.dirname(__file__)
CHROME_DRIVER_DICT = {'linux': os.path.join(PROJECT_ROOT, 'webdrivers/chromedriver_lin'),
                      'darwin': os.path.join(PROJECT_ROOT, 'webdrivers/chromedriver_mac'),
                      'win32': os.path.join(PROJECT_ROOT, 'webdrivers/chromedriver_win.exe'),
                      'win64': os.path.join(PROJECT_ROOT, 'webdrivers/chromedriver_win.exe')}


@fixture
def start_browser():
    if "redhat" in platform.platform():
        display = Display(visible=0, size=(1920, 1080))
        display.start()

    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('lang=ru')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_DICT[sys.platform], options=chrome_options)

    listener = LoggedListener()

    tests_data.shared_variables.DRIVER = EventFiringWebDriver(driver=driver, event_listener=listener)

    yield

    if sys.exc_info():
        driver = tests_data.shared_variables.DRIVER
        allure.attach(body=driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
    tests_data.shared_variables.DRIVER.quit()
