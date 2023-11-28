
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
# from selenium.webdriver.support.select import Select


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def wait_for(self, by_locator):
        return self._wait.until(ec.presence_of_element_located(by_locator))

    def find(self, by_locator):
        return self.driver.find_element(*by_locator)

    def exex_script(self, script: str):
        self.driver.execute_script(script=script)

    def func1(self):
        print("1+2+3+4_5")

    # def is_visible(self,by_locator):
    #     element = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(by_locator))
    #     return bool(element)

    # def get_title(self,title):
    #     WebDriverWait(self.driver,5).until(ec.title_is(title))
    #     self.driver.title

    # def select_item(self,by_locator,item):
    #     wait = WebDriverWait(self.driver,5)
    #     wait.until(ec.text_to_be_present_in_element(by_locator,item))
    #     select = Select(self.driver.find_element(by_locator[0],by_locator[1]))
    #     select.select_by_visible_text(item)
