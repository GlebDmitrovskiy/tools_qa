from playwright.sync_api import Page, expect


class TestBasePage:

    def test_go_to_element(self, base_page):
        base_page.go_to_main_page()
        base_page.go_to_elements_page()
        menu = base_page.find(base_page.locators.elements_menu_locator)
        menu.wait_for(state="visible", timeout=5000)
        assert menu.is_visible()
