import pytest
import allure
from playwright.sync_api import Page
from page.elements_page import ElementsPage


class TestElementsPage:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.elements_page = ElementsPage(page)

    def test_fill_text_box_form(self, user_data):
        with allure.step("Открыть главную страницу"):
            self.elements_page.go_to_main_page()
        with allure.step("Открыть страницу element"):
            self.elements_page.go_to_elements_page()
        with allure.step("Открыть страницу Text Box"):
            self.elements_page.go_to_text_box()
        self.elements_page.input_text_full_name_field(user_data.get("fullname"))
        self.elements_page.input_text_email_field(user_data.get("email"))
        self.elements_page.input_text_current_address_field(user_data.get("address"))
        self.elements_page.input_text_permanent_address_field(user_data.get("address"))
        self.elements_page.click_submit_button()
        self.elements_page.check_submitted_data()
        
