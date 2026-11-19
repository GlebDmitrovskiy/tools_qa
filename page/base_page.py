from playwright.sync_api import Page, expect, Locator
from locators.base_page_locators import BasePageUsersLocators


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = BasePageUsersLocators()

    def go_to_main_page(self):
        self.page.goto("https://demoqa.com/")

    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    def go_to_elements_page(self):
        self.find(self.locators.elements_page_button_locator).click()

    def go_to_forms_page(self):
        self.find(self.locators.forms_page_button_locator).click()

    def go_to_frame_and_windows_page(self):
        self.find(self.locators.alerts_page_button_frame_and_windows).click()
