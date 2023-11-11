from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TextBoxPage(BasePage):

    TEXT_BOX_BUTTON = (By.XPATH, "//span[text()='Text Box']")
    TEXT_BOX_HEADER = (By.XPATH, "//div[text()='Text Box']")
    FULL_NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (
        By.XPATH, "//button[@id='submit'][contains(text(), 'Submit')]")
    P_FULL_NAME = (
        By.XPATH, "//div[@id='output']//div[contains(@class, 'border col-md-12 col-sm-12')]//p[@id='name']")
    P_EMAIL = (
        By.XPATH, "//div[@id='output']//div[contains(@class, 'border col-md-12 col-sm-12')]//p[@id='email']")
    P_CURRENT_ADDRESS = (
        By.XPATH, "//div[@id='output']//div[contains(@class, 'border col-md-12 col-sm-12')]//p[@id='currentAddress']")
    P_PERMANENT_ADDRESS = (
        By.XPATH, "//div[@id='output']//div[contains(@class, 'border col-md-12 col-sm-12')]//p[@id='permanentAddress']")
    OUTPUT_DIV = (
        By.XPATH, "//div[@id='output']//div[contains(@class, 'col-md-12 col-sm-12')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def navigate_to_text_box_page(self):
        self.find(self.TEXT_BOX_BUTTON).click()

    def get_text_box_header(self):
        return self.find(self.TEXT_BOX_HEADER).text

    def enter_name(self, full_name):
        self.wait_for(self.FULL_NAME)
        self.find(self.FULL_NAME).send_keys(full_name)

    def enter_email(self, email):
        self.find(self.EMAIL).send_keys(email)

    def enter_current_address(self, current_addr):
        self.find(self.CURRENT_ADDRESS).send_keys(current_addr)

    def enter_permanent_address(self, permanent_addr):
        self.find(self.PERMANENT_ADDRESS).send_keys(permanent_addr)

    def click_submit_button(self):
        script = "window.scrollTo(0,350);"
        self.exex_script(script)
        self.find(self.SUBMIT_BUTTON).click()

    def get_paragraph_name(self):
        self.wait_for(self.P_FULL_NAME)
        return self.find(self.P_FULL_NAME).text

    def get_paragraph_email(self):
        self.wait_for(self.P_EMAIL)
        return self.find(self.P_EMAIL).text

    def get_paragraph_current_address(self):
        self.wait_for(self.P_CURRENT_ADDRESS)
        return self.find(self.P_CURRENT_ADDRESS).text

    def get_paragraph_permanent_address(self):
        self.wait_for(self.P_PERMANENT_ADDRESS)
        return self.find(self.P_PERMANENT_ADDRESS).text

    def get_output_div_text(self):
        self.wait_for(self.OUTPUT_DIV)
        return self.find(self.OUTPUT_DIV).text
