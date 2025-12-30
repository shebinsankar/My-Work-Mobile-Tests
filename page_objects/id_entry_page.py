from appium.webdriver.common.appiumby import AppiumBy
from page_objects.base_page import BasePage


class IdEntryPage(BasePage):

    # TODO: Update with actual locators from Appium Inspector
    IDENT_ID_INPUT = (AppiumBy.ACCESSIBILITY_ID, "ident_id_input")
    IDENT_ID_INPUT_XPATH = (AppiumBy.XPATH, "//android.widget.EditText")
    START_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "start_button")
    START_BUTTON_XPATH = (
        AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Start')]")

    def is_page_loaded(self):
        try:
            return (self.is_displayed(*self.IDENT_ID_INPUT, timeout=10) or
                    self.is_displayed(*self.IDENT_ID_INPUT_XPATH, timeout=5))
        except:
            return False

    def enter_ident_id(self, ident_id):
        try:
            self.send_keys(*self.IDENT_ID_INPUT, ident_id)
        except:
            self.send_keys(*self.IDENT_ID_INPUT_XPATH, ident_id)

    def click_start_button(self):
        try:
            self.click(*self.START_BUTTON)
        except:
            self.click(*self.START_BUTTON_XPATH)
