from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from .base_page import BasePage


class ElementsPage(BasePage):

    ELEMENTS_BUTTON = (By.XPATH, "//h5[text()='Elements']/../../..")
    ELEMENTS_HEADER = (By.XPATH, "//div[text()='Elements']")

    # CHECK_BOX_BUTTON = (By.XPATH,"//span[text()='Check Box']")
    # RADIO_BUTTON = (By.XPATH,"//span[text()='Radio Button']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def navigate_to_elements_page(self):
        self.find(self.ELEMENTS_BUTTON).click()

    def get_elements_header(self):
        return self.find(self.ELEMENTS_HEADER).text
