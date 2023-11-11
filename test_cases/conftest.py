
import pytest

from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from utilities.config_reader import read_config


@pytest.fixture(scope='function')
def init_driver(request):

    browser = read_config("Details", "BROWSER")
    if browser == "Chrome":
        web_driver = Chrome()
    elif browser == "Firefox":
        web_driver = Firefox()
    else:
        web_driver = Chrome()
    url = read_config("Details", "APPLICATION_URL")
    web_driver.get(url)
    web_driver.implicitly_wait(2)
    web_driver.maximize_window()
    request.cls.driver = web_driver
    yield
    web_driver.close()
