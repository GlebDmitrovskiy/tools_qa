import pytest
import allure
from playwright.sync_api import Page
from page.main_page import MainPage


class TestMainPage:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.main_page = MainPage(page)

    def test_go_to_elements_page(self):
        with allure.step("Открыть главную страницу"):
            self.main_page.go_to_main_page()
        with allure.step("Открыть страницу element"):
            self.main_page.go_to_elements_page()

    def test_go_to_forms_page(self):
        with allure.step("Открыть главную страницу"):
            self.main_page.go_to_main_page()
        with allure.step("Открыть страницу forms"):
            self.main_page.go_to_forms_page()

    def test_go_to_alerts_frame_and_windows_page(self):
        with allure.step("Открыть главную страницу"):
            self.main_page.go_to_main_page()
        with allure.step("Открыть страницу alerts_frame_and_windows"):
            self.main_page.go_to_alerts_frame_and_windows_page()
