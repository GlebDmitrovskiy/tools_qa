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
    CHECK_BOX_HOME_BUTTON_LIST_BOXES_LOCATOR = "//div[@class='rc-tree-list-holder-inner']//span[@role='checkbox']"
    RADIO_BUTTON_LOCATOR = "//span[@class='text' and text()='Radio Button']"
    RADIO_BUTTON_YES_BUTTON_LOCATOR = "//input[@id='yesRadio']"
    RADIO_BUTTON_YES_BUTTON_CHECK_LOCATOR = "//span[@class='text-success' and text()='Yes']"
    RADIO_BUTTON_IMPRESSIVE_BUTTON_LOCATOR = "//input[@id='impressiveRadio']"
    RADIO_BUTTON_IMPRESSIVE_BUTTON_CHECK_LOCATOR = "//span[@class='text-success' and text()='Impressive']"
    RADIO_BUTTON_NO_BUTTON_LOCATOR = "//input[@id='noRadio']"


class ElementsPageURL(StrEnum):
    TEXT_BOX_URL = "https://demoqa.com/text-box"
    CHECK_BOX_URL = "https://demoqa.com/checkbox"
    RADIO_BUTTON_URL = "https://demoqa.com/radio-button"
