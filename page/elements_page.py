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
        self.check_is_element_visible(ElementsPageLocators.TEXT_BOX_FULL_NAME_FIELD_INPUT_FIELD_LOCATOR)

    @allure.step("Проверить, что поле 'Email' видно на странице")
    def _check_email_field_visible(self):
        self.check_is_element_visible(ElementsPageLocators.TEXT_BOX_EMAIL_FIELD_INPUT_FIELD_LOCATOR)

    @allure.step("Проверить, что поле 'Current Address' видно на странице")
    def _check_current_address_field_visible(self):
        self.check_is_element_visible(ElementsPageLocators.TEXT_BOX_CURRENT_ADDRESS_INPUT_FIELD_LOCATOR)

    @allure.step("Проверить, что поле 'Permanent Address' видно на странице")
    def _check_permanent_address_field_visible(self):
        self.check_is_element_visible(ElementsPageLocators.TEXT_BOX_PERMANENT_ADDRESS_INPUT_FIELD_LOCATOR)

    @allure.step("Проверить, что кнопка 'Text Box' активна для клика")
    def _check_text_box_page_button_enabled(self):
        self.check_is_element_enabled(ElementsPageLocators.TEXT_BOX_BUTTON_LOCATOR)

    @allure.step("Проверить, что кнопка 'Submit' активна для клика")
    def _check_submit_button_enabled(self):
        self.check_is_element_enabled(ElementsPageLocators.TEXT_BOX_SUBMIT_BUTTON_LOCATOR)

    @allure.step("Проверить, что открылась страница Text Box по корректному URL")
    def _check_text_box_page_opened(self):
        self.is_page_opened_on_correct_url(ElementsPageURL.TEXT_BOX_URL)

    @allure.step("Проверить, что поле 'Name' доступно для ввода текста")
    def _check_is_full_name_field_editable(self):
        self.check_is_element_editable(ElementsPageLocators.TEXT_BOX_FULL_NAME_FIELD_INPUT_FIELD_LOCATOR)

    @allure.step("Проверить, что поле 'Email' доступно для ввода текста")
    def _check_is_email_field_editable(self):
        self.check_is_element_editable(ElementsPageLocators.TEXT_BOX_EMAIL_FIELD_INPUT_FIELD_LOCATOR)

    @allure.step("Проверить, что поле 'Current Address' доступно для ввода текста")
    def _check_is_current_address_field_editable(self):
        self.check_is_element_editable(ElementsPageLocators.TEXT_BOX_CURRENT_ADDRESS_INPUT_FIELD_LOCATOR)

    @allure.step("Проверить, что поле 'Permanent Address' доступно для ввода текста")
    def _check_is_permanent_address_field_editable(self):
        self.check_is_element_editable(ElementsPageLocators.TEXT_BOX_PERMANENT_ADDRESS_INPUT_FIELD_LOCATOR)

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

    @allure.step("Получить введённое значение из поля 'Full Name'")
    def get_full_name_input_value(self) -> str:
        entered_name = self.get_input_value(
            ElementsPageLocators.TEXT_BOX_FULL_NAME_FIELD_INPUT_FIELD_LOCATOR
        )
        return entered_name

    @allure.step("Получить введённое значение из поля 'Email'")
    def get_email_input_value(self) -> str:
        entered_email = self.get_input_value(
            ElementsPageLocators.TEXT_BOX_EMAIL_FIELD_INPUT_FIELD_LOCATOR
        )
        return entered_email

    @allure.step("Получить введённое значение из поля 'Permanent Address'")
    def get_permanent_address_input_value(self) -> str:
        entered_permanent_address = self.get_input_value(
            ElementsPageLocators.TEXT_BOX_PERMANENT_ADDRESS_INPUT_FIELD_LOCATOR
        )
        return entered_permanent_address

    @allure.step("Получить введённое значение из поля 'Current Address'")
    def get_current_address_input_value(self) -> str:
        entered_current_address = self.get_input_value(
            ElementsPageLocators.TEXT_BOX_CURRENT_ADDRESS_INPUT_FIELD_LOCATOR
        )
        return entered_current_address

    @allure.step("Получить отображаемый 'Name' в блоке результата")
    def get_output_full_name_text(self) -> str:
        displayed_name = self.get_element_text(
            ElementsPageLocators.TEXT_BOX_NAME_FIELD_CHECK_LOCATOR
        ).split(":")[1]
        return displayed_name

    @allure.step("Получить отображаемый 'Email' в блоке результата")
    def get_output_email_text(self) -> str:
        displayed_email = self.get_element_text(
            ElementsPageLocators.TEXT_BOX_EMAIL_FIELD_CHECK_LOCATOR
        ).split(":")[1]
        return displayed_email

    @allure.step("Получить отображаемый 'Current Address' в блоке результата")
    def get_output_current_address_text(self) -> str:
        displayed_current_address = self.get_element_text(
            ElementsPageLocators.TEXT_BOX_CURRENT_ADDRESS_FIELD_CHECK_LOCATOR
        ).split(":")[1]
        return displayed_current_address

    @allure.step("Получить отображаемый 'Permanent Address' в блоке результата")
    def get_output_permanent_address_text(self) -> str:
        displayed_permanent_address = self.get_element_text(
            ElementsPageLocators.TEXT_BOX_PERMANENT_ADDRESS_FIELD_CHECK_LOCATOR
        ).split(":")[1]
        return displayed_permanent_address

    @allure.step("Ввести текст в поле 'Full Name'")
    def input_text_full_name_field(self, text: str):
        self._check_full_name_field_visible()
        self._check_is_full_name_field_editable()
        self.input_text(ElementsPageLocators.TEXT_BOX_FULL_NAME_FIELD_INPUT_FIELD_LOCATOR, text=text)

    @allure.step("Ввести текст в поле 'Email'")
    def input_text_email_field(self, text: str):
        self._check_email_field_visible()
        self._check_is_email_field_editable()
        self.input_text(ElementsPageLocators.TEXT_BOX_EMAIL_FIELD_INPUT_FIELD_LOCATOR, text=text)

    @allure.step("Ввести текст в поле 'Current Address'")
    def input_text_current_address_field(self, text: str):
        self._check_current_address_field_visible()
        self._check_is_current_address_field_editable()
        self.input_text(ElementsPageLocators.TEXT_BOX_CURRENT_ADDRESS_INPUT_FIELD_LOCATOR, text=text)

    @allure.step("Ввести текст в поле 'Permanent Address'")
    def input_text_permanent_address_field(self, text: str):
        self._check_permanent_address_field_visible()
        self._check_is_permanent_address_field_editable()
        self.input_text(ElementsPageLocators.TEXT_BOX_PERMANENT_ADDRESS_INPUT_FIELD_LOCATOR, text=text)

    @allure.step("Проверить, что введённые данные совпадают с блоком результата")
    def check_submitted_data(self):
        assert self.get_full_name_input_value() == self.get_output_full_name_text()
        assert self.get_email_input_value() == self.get_output_email_text()
        assert self.get_current_address_input_value() == self.get_output_current_address_text()
        assert self.get_permanent_address_input_value() == self.get_output_permanent_address_text()
