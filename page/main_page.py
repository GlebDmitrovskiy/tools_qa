from playwright.sync_api import Page, expect, Locator
from locators.main_page_locators import MainPageUsersLocators
from page.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
    locators = MainPageUsersLocators()

    def _check_elements_page_button_visible(self):
        self.check_is_element_visible(self.locators.elements_page_button_locator)

    def _check_elements_page_button_enabled(self):
        self.check_is_element_enabled(self.locators.elements_page_button_locator)

    def _check_elements_page_opened(self):
        self.is_page_opened_on_correct_url(self.locators.elements_page_url)

    def go_to_elements_page(self):
        self._check_elements_page_button_visible()
        self._check_elements_page_button_enabled()
        self.click(self.locators.elements_page_button_locator)
        self._check_elements_page_opened()

    def go_to_forms_page(self):
        self.click(self.locators.forms_page_button_locator)

    def go_to_frame_and_windows_page(self):
        self.click(self.locators.alerts_page_button_frame_and_windows)

    def go_to_main_page(self):
        self.page.goto("https://demoqa.com/")
