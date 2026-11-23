import allure
from playwright.sync_api import Page, expect, Locator
from locators.main_page_locators import MainPageUsersLocators
from locators.main_page_locators import MainPageURL
from page.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Проверить, что кнопка 'Elements' видна на странице")
    def _check_elements_page_button_visible(self):
        self.check_is_element_visible(MainPageUsersLocators.ELEMENTS_PAGE_BUTTON_LOCATOR)

    @allure.step("Проверить, что кнопка 'Forms' видна на странице")
    def _check_forms_page_button_visible(self):
        self.check_is_element_visible(MainPageUsersLocators.FORMS_PAGE_BUTTON_LOCATOR)

    @allure.step("Проверить, что кнопка Alerts, Frame & Windows видна на странице")
    def _check_alerts_frame_and_windows_page_button_visible(self):
        self.check_is_element_visible(MainPageUsersLocators.ALERTS_PAGE_BUTTON_FRAME_AND_WINDOWS)

    @allure.step("Проверить, что кнопка 'Elements' активна для клика")
    def _check_elements_page_button_enabled(self):
        self.check_is_element_enabled(MainPageUsersLocators.ELEMENTS_PAGE_BUTTON_LOCATOR)

    @allure.step("Проверить, что кнопка 'Forms' активна для клика")
    def _check_forms_page_button_enabled(self):
        self.check_is_element_enabled(MainPageUsersLocators.FORMS_PAGE_BUTTON_LOCATOR)

    @allure.step("Проверить, что кнопка Alerts, Frame & Windows активна для клика")
    def _check_alerts_frame_and_windows_button_enabled(self):
        self.check_is_element_enabled(MainPageUsersLocators.ALERTS_PAGE_BUTTON_FRAME_AND_WINDOWS)

    @allure.step("Проверить, что открылась страница Elements по корректному URL")
    def _check_elements_page_opened(self):
        self.is_page_opened_on_correct_url(MainPageURL.ELEMENTS_PAGE_URL)

    @allure.step("Проверить, что открылась страница Forms по корректному URL")
    def _check_forms_page_opened(self):
        self.is_page_opened_on_correct_url(MainPageURL.FORMS_PAGE_URL)
        
    @allure.step("Проверить, что открылась страница Alerts, Frame & Windows по корректному URL")
    def _check_alerts_frame_and_windows_page_opened(self):
        self.is_page_opened_on_correct_url(MainPageURL.ALERT_FRAME_URl)

    @allure.step("Перейти на страницу 'Elements'")
    def go_to_elements_page(self):
        self._check_elements_page_button_visible()
        self._check_elements_page_button_enabled()
        self.click(MainPageUsersLocators.ELEMENTS_PAGE_BUTTON_LOCATOR)
        self._check_elements_page_opened()

    @allure.step("Перейти на страницу 'Forms'")
    def go_to_forms_page(self):
        self._check_forms_page_button_visible()
        self._check_alerts_frame_and_windows_button_enabled()
        self.click(MainPageUsersLocators.FORMS_PAGE_BUTTON_LOCATOR)
        self._check_forms_page_opened()

    @allure.step("Перейти на страницу 'Alerts, Frame & Windows'")
    def go_to_alerts_frame_and_windows_page(self):
        self._check_alerts_frame_and_windows_page_button_visible()
        self._check_alerts_frame_and_windows_button_enabled()
        self.click(MainPageUsersLocators.ALERTS_PAGE_BUTTON_FRAME_AND_WINDOWS)
        self._check_alerts_frame_and_windows_page_opened()

    @allure.step("Открыть главную страницу DemoQA")
    def go_to_main_page(self):
        self.page.goto("https://demoqa.com/")
