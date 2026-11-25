from enum import StrEnum


class ElementsPageLocators(StrEnum):
    TEXT_BOX_BUTTON_LOCATOR = "//span[@class='text' and text()='Text Box']"
    TEXT_BOX_FULL_NAME_FIELD_INPUT_FIELD_LOCATOR = "//input[@id='userName']"
    TEXT_BOX_EMAIL_FIELD_INPUT_FIELD_LOCATOR = "//input[@id='userEmail']"
    TEXT_BOX_CURRENT_ADDRESS_INPUT_FIELD_LOCATOR = "//textarea[@id='currentAddress']"
    TEXT_BOX_PERMANENT_ADDRESS_INPUT_FIELD_LOCATOR = "//textarea[@id='permanentAddress']"
    TEXT_BOX_NAME_FIELD_CHECK_LOCATOR = "//p[@id='name']"
    TEXT_BOX_EMAIL_FIELD_CHECK_LOCATOR = "//p[@id='email']"
    TEXT_BOX_CURRENT_ADDRESS_FIELD_CHECK_LOCATOR = "//p[@id='currentAddress']"
    TEXT_BOX_PERMANENT_ADDRESS_FIELD_CHECK_LOCATOR = "//p[@id='permanentAddress']"
    TEXT_BOX_SUBMIT_BUTTON_LOCATOR = "//button[@id='submit']"
    CHECK_BOX_BUTTON_LOCATOR = "//span[@class='text' and text()='Check Box']"
    
    
class ElementsPageURL(StrEnum):
    TEXT_BOX_URL = "https://demoqa.com/text-box"
    CHECK_BOX_URL = "https://demoqa.com/checkbox"