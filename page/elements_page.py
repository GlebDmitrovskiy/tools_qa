import allure
from playwright.sync_api import Page
from page.main_page import MainPage
from locators.elements_page_locators import ElementsPageLocators
from locators.elements_page_locators import ElementsPageURL


class ElementsPage(MainPage):
    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step("Проверить, что кнопка 'Text Box' видна на странице")
    def _check_text_box_page_button_visible(self):
        self.check_is_element_visible(ElementsPageLocators.TEXT_BOX_BUTTON_LOCATOR)

    @allure.step("Проверить, что кнопка 'Submit' видна на странице")
    def _check_submit_button_visible(self):
        self.check_is_element_visible(ElementsPageLocators.TEXT_BOX_SUBMIT_BUTTON_LOCATOR)

    @allure.step("Проверить, что кнопка 'Full name' видна на странице")
    def _check_full_name_field_visible(self):
        self.check_is_element_visible(ElementsPageLocators.TEXT_BOX_FULL_NAME_FIELD_INPUT_LOCATOR)

    @allure.step("Проверить, что поле 'Name' видно на странице")
    def _check_name_field_visible(self):
        self.check_is_element_visible(ElementsPageLocators.TEXT_BOX_NAME_FIELD_CHECK_LOCATOR)

    @allure.step("Проверить, что кнопка 'Text Box' активна для клика")
    def _check_text_box_page_button_enabled(self):
        self.check_is_element_enabled(ElementsPageLocators.TEXT_BOX_BUTTON_LOCATOR)

    @allure.step("Проверить, что кнопка 'Submit' активна для клика")
    def _check_submit_button_enabled(self):
        self.check_is_element_enabled(ElementsPageLocators.TEXT_BOX_SUBMIT_BUTTON_LOCATOR)

    @allure.step("Проверить, что открылась страница Text Box по корректному URL")
    def _check_text_box_page_opened(self):
        self.is_page_opened_on_correct_url(ElementsPageURL.TEXT_BOX_URL)

    @allure.step("Проверить, что поле 'Full Name' доступно для ввода текста")
    def _check_is_full_name_field_editable(self):
        self.check_is_element_editable(ElementsPageLocators.TEXT_BOX_FULL_NAME_FIELD_INPUT_LOCATOR)

    def go_to_elements(self):
        self.go_to_elements_page()

    def go_to_text_box(self):
        self._check_text_box_page_button_visible()
        self._check_text_box_page_button_enabled()
        self.click(ElementsPageLocators.TEXT_BOX_BUTTON_LOCATOR)
        self._check_text_box_page_opened()

    @allure.step("Нажать на кнопку 'Submit'")
    def click_submit_button(self):
        self._check_submit_button_visible()
        self._check_submit_button_enabled()
        self.click(ElementsPageLocators.TEXT_BOX_SUBMIT_BUTTON_LOCATOR)
        self._check_name_field_visible()

    @allure.step("Получить введённое значение из поля Full Name")
    def get_full_name_input_value(self) -> str:
        entered_name = self.get_input_value(ElementsPageLocators.TEXT_BOX_FULL_NAME_FIELD_INPUT_LOCATOR)
        return entered_name
        

    @allure.step("Получить отображаемое имя в блоке результата")
    def get_output_full_name_text(self) -> str:
        displayed_name = self.get_element_text(ElementsPageLocators.TEXT_BOX_NAME_FIELD_CHECK_LOCATOR).split(":")[1]
        return displayed_name

    @allure.step("Ввести текст в поле 'Full Name'")
    def input_text_full_name_field(self, text: str):
        self._check_full_name_field_visible()
        self._check_is_full_name_field_editable()
        self.input_text(ElementsPageLocators.TEXT_BOX_FULL_NAME_FIELD_INPUT_LOCATOR, text=text)
