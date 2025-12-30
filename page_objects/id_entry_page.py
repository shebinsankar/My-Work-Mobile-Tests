from appium.webdriver.common.appiumby import AppiumBy
from page_objects.base_page import BasePage


class IdEntryPage(BasePage):

    # TODO: Update with actual locators from Appium Inspector
    IDENT_ID_INPUT = (AppiumBy.ACCESSIBILITY_ID, "ToDo")
    IDENT_ID_INPUT_XPATH = (AppiumBy.XPATH, "ToDo")
    START_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "ToDo")
    START_BUTTON_XPATH = (
        AppiumBy.XPATH, "ToDo")

    def is_page_loaded(self):
        try:
            return (self.is_displayed(*self.IDENT_ID_INPUT, timeout=10) or
                    self.is_displayed(*self.IDENT_ID_INPUT_XPATH, timeout=5))
        except Exception:
            return False

    def enter_ident_id(self, ident_id):
        try:
            self.send_keys(*self.IDENT_ID_INPUT, ident_id)
        except Exception:
            self.send_keys(*self.IDENT_ID_INPUT_XPATH, ident_id)

    def click_start_button(self):
        try:
            self.click(*self.START_BUTTON)
        except Exception:
            self.click(*self.START_BUTTON_XPATH)
            self.click(*self.START_BUTTON_XPATH)
