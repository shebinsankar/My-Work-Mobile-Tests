import pytest
import time
from page_objects.id_entry_page import IdEntryPage
from page_objects.privacy_policy_page import PrivacyPolicyPage
from config.config import TEST_IDENT_ID


class TestIDnowBasicFlow:

    def test_launch_app_and_accept_terms(self, driver):
        # Verify app launched and ID entry screen loaded
        id_entry_page = IdEntryPage(driver)
        assert id_entry_page.is_page_loaded(), "ID entry page not loaded"
        id_entry_page.take_screenshot("01_app_launched")

        # Enter Ident ID and click Start
        id_entry_page.enter_ident_id(TEST_IDENT_ID)
        time.sleep(1)
        id_entry_page.click_start_button()
        time.sleep(2)

        # Accept terms on privacy page
        privacy_page = PrivacyPolicyPage(driver)
        assert privacy_page.is_page_loaded(), "Privacy page not loaded"
        privacy_page.take_screenshot("02_privacy_page")

        privacy_page.accept_terms_and_start()
        time.sleep(2)
        privacy_page.take_screenshot("03_terms_accepted")
