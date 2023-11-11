import pytest
from test_cases.test_base import BaseTest
from pages.elements_page import ElementsPage
from pages.text_box_page import TextBoxPage
from utilities.config_reader import get_data
import time


class TestTextBox(BaseTest):

    def test_header(self):
        self.elements_page = ElementsPage(self.driver)
        self.elements_page.navigate_to_elements_page()
        self.text_box_page = TextBoxPage(self.driver)
        self.text_box_page.navigate_to_text_box_page()
        header = self.text_box_page.get_text_box_header()
        assert header == get_data("Headers", "TEXT_BOX_HEADER")

    def test_form_submission(self):
        self.elements_page = ElementsPage(self.driver)
        self.elements_page.navigate_to_elements_page()
        self.text_box_page = TextBoxPage(self.driver)
        self.text_box_page.navigate_to_text_box_page()

        full_name = get_data("UserData", "FULL_NAME")
        email = get_data("UserData", "EMAIL")
        current_addr = get_data("UserData", "CURRNET_ADDRESS")
        permanent_addr = get_data("UserData", "PERMANENT_ADDRESS")

        self.text_box_page.enter_name(full_name)
        self.text_box_page.enter_email(email)
        self.text_box_page.enter_current_address(current_addr)
        self.text_box_page.enter_permanent_address(permanent_addr)
        self.text_box_page.click_submit_button()

        assert self.text_box_page.get_paragraph_name() == "Name:{}".format(
            full_name)
        assert "Email:{}".format(
            email) == self.text_box_page.get_paragraph_email()
        assert "Current Address :{}".format(
            current_addr) == self.text_box_page.get_paragraph_current_address()
        assert "Permananet Address :{}".format(
            permanent_addr) == self.text_box_page.get_paragraph_permanent_address()
        time.sleep(3)

    def test_empty_form_submission(self):
        self.elements_page = ElementsPage(self.driver)
        self.elements_page.navigate_to_elements_page()
        self.text_box_page = TextBoxPage(self.driver)
        self.text_box_page.navigate_to_text_box_page()

        self.text_box_page.click_submit_button()
        assert self.text_box_page.get_output_div_text() == ''
        time.sleep(3)
