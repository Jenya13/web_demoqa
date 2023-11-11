from test_cases.test_base import BaseTest
from pages.elements_page import ElementsPage
from utilities.config_reader import get_data


class TestElements(BaseTest):

    def test_elements_page(self):
        pass
        # self.elements_page = ElementsPage(self.driver)
        # self.elements_page.navigate_to_elements_page()

        # header = self.elements_page.get_elements_header()
        # assert header == get_data("Headers", "ELEMENTS_HEADER")
