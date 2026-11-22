class MainPageUsersLocators:
    def __init__(self):
        self.elements_page_button_locator = "//h5[text()='Elements']"
        self.forms_page_button_locator = "//h5[text()='Forms']"
        self.alerts_page_button_frame_and_windows = "//h5[text()='Alerts, Frame & Windows']"
        self.elements_menu_locator = "//div[@class='element-list accordion-collapse collapse show']"
        #TODO: Разделить на 2 класса Enum с локаторами и urlами
        self.elements_page_url = "https://demoqa.com/elements"