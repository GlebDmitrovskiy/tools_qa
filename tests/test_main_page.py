from playwright.sync_api import Page, expect
from page.main_page import MainPage
import pytest

class TestMainPage:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.main_page = MainPage(page)

    def test_go_to_elements_page(self):
        self.main_page.go_to_main_page()
        self.main_page.go_to_elements_page()

