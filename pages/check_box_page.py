from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckBoxPage(BasePage):

    CHECK_BOX_BUTTON = (By.XPATH, "//span[text()='Check Box']")
    CHECK_BOX_HEADER = (By.XPATH, "//div[text()='Check Box']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def navigate_to_check_box_page(self):
        self.find(self.CHECK_BOX_BUTTON).click()

    def get_check_box_header(self):
        return self.find(self.CHECK_BOX_HEADER).text

    def some_func(self):
        pass
