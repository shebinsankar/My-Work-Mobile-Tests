from appium.webdriver.common.appiumby import AppiumBy
from page_objects.base_page import BasePage


class PrivacyPolicyPage(BasePage):

    # TODO: Update with actual locators
    PRIVACY_POLICY_TITLE = (
        AppiumBy.XPATH, "ToDo")
    CHECKBOX_ACCEPT = (AppiumBy.XPATH, "//android.widget.CheckBox")
    START_IDENTIFICATION_BUTTON = (
        AppiumBy.XPATH, "ToDo")

    def is_page_loaded(self):
        return self.is_displayed(*self.PRIVACY_POLICY_TITLE, timeout=10)

    def check_accept_checkbox(self):
        if self.is_displayed(*self.CHECKBOX_ACCEPT, timeout=3):
            self.click(*self.CHECKBOX_ACCEPT)

    def click_start_identification(self):
        self.click(*self.START_IDENTIFICATION_BUTTON)

    def accept_terms_and_start(self):
        self.check_accept_checkbox()
        self.click_start_identification()
