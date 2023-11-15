# import pytest
from test_cases.test_base import BaseTest
from pages.elements_page import ElementsPage
from pages.check_box_page import CheckBoxPage
from utilities.config_reader import get_data
import time


class TestCheckBox(BaseTest):

    def test_header(self):
        self.elements_page = ElementsPage(self.driver)
        self.elements_page.navigate_to_elements_page()
        self.check_box_page = CheckBoxPage(self.driver)
        self.check_box_page.navigate_to_check_box_page()
        header = self.check_box_page.get_check_box_header()
        assert header == get_data("Headers", "CHECK_BOX_HEADER")

    def test_all_check_boxes_checked(self):
        self.elements_page = ElementsPage(self.driver)
        self.elements_page.navigate_to_elements_page()
        self.check_box_page = CheckBoxPage(self.driver)
        self.check_box_page.navigate_to_check_box_page()
        self.check_box_page.click_home_check_box()
        self.check_box_page.click_expand_all_button()
        assert self.check_box_page.result_div_exist() == True

    def test_all_check_boxes_unchecked(self):
        self.elements_page = ElementsPage(self.driver)
        self.elements_page.navigate_to_elements_page()
        self.check_box_page = CheckBoxPage(self.driver)
        self.check_box_page.navigate_to_check_box_page()
        assert self.check_box_page.result_div_exist() == False
