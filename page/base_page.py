from playwright.sync_api import Page, expect, Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def input_text(self, locator, text: str):
        self.page.locator(locator).fill(text)

    def click(self, locator):
        self.page.locator(locator).click()

    def check_is_element_editable(self, locator):
        expect(self.page.locator(locator)).to_be_editable()

    def check_is_element_visible(self, locator):
        expect(self.page.locator(locator)).to_be_visible()

    def get_element_text(self, locator) -> str:
        return self.page.locator(locator).inner_text()

    def get_input_value(self, locator) -> str:
        return self.page.locator(locator).input_value()

    def is_element_not_visible(self, locator):
        expect(self.page.locator(locator)).to_be_hidden()

    def check_is_element_enabled(self, locator):
        expect(self.page.locator(locator)).to_be_enabled()

    def is_page_opened_on_correct_url(self, url):
        expect(self.page).to_have_url(url)
