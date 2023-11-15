from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckBoxPage(BasePage):

    CHECK_BOX_BUTTON = (By.XPATH, "//span[text()='Check Box']")
    CHECK_BOX_HEADER = (By.XPATH, "//div[text()='Check Box']")
    EXPAND_BUTTON = (By.XPATH, "//button[@title='Expand all']")
    COLLAPSE_BUTTON = (By.XPATH, "//button[@title='Collapse all']")
    HOME_CHECK_BOX = (
        By.XPATH, "//span[@class='rct-checkbox']/parent::label[@for='tree-node-home']")
    RESULT_DIV = (By.XPATH, "//div[@id='result']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def navigate_to_check_box_page(self):
        self.find(self.CHECK_BOX_BUTTON).click()

    def get_check_box_header(self):
        return self.find(self.CHECK_BOX_HEADER).text

    def click_expand_all_button(self):
        self.find(self.EXPAND_BUTTON).click()

    def click_collapse_all_button(self):
        self.find(self.COLLAPSE_BUTTON).click()

    def click_home_check_box(self):
        self.find(self.HOME_CHECK_BOX).click()

    def result_div_exist(self):
        try:
            self.find(self.RESULT_DIV)
            return True
        except NoSuchElementException:
            return False
