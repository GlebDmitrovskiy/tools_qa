from enum import StrEnum


class MainPageUsersLocators(StrEnum):
    ELEMENTS_PAGE_BUTTON_LOCATOR = "//h5[text()='Elements']"
    FORMS_PAGE_BUTTON_LOCATOR = "//h5[text()='Forms']"
    ALERTS_PAGE_BUTTON_FRAME_AND_WINDOWS = "//h5[text()='Alerts, Frame & Windows']"
    ELEMENTS_MENU_LOCATOR = "//div[@class='element-list accordion-collapse collapse show']"


class MainPageURL(StrEnum):
    ELEMENTS_PAGE_URL = "https://demoqa.com/elements"
    FORMS_PAGE_URL = "https://demoqa.com/forms"
    ALERT_FRAME_URl = "https://demoqa.com/alertsWindows"