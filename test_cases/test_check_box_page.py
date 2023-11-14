import pytest
from test_cases.test_base import BaseTest
from pages.elements_page import ElementsPage
from pages.check_box_page import CheckBoxPage
from utilities.config_reader import get_data


class TestCheckBox(BaseTest):

    def test_header(self):
        self.elements_page = ElementsPage(self.driver)
        self.elements_page.navigate_to_elements_page()

        self.check_box_page = CheckBoxPage(self.driver)
        self.check_box_page.navigate_to_check_box_page()
        header = self.check_box_page.get_check_box_header()
        assert header == get_data("Headers", "CHECK_BOX_HEADER")
