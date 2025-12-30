"""
Base Page class containing common methods for all page objects.
Implements Page Object Model.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import EXPLICIT_WAIT
from pathlib import Path


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    def find_element(self, locator_type, locator_value, timeout=EXPLICIT_WAIT):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((locator_type, locator_value)))

    def click(self, locator_type, locator_value):
        element = self.find_element(locator_type, locator_value)
        element.click()

    def send_keys(self, locator_type, locator_value, text):
        element = self.find_element(locator_type, locator_value)
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator_type, locator_value, timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(
                (locator_type, locator_value)))
            return True
        except TimeoutException:
            return False

    def take_screenshot(self, filename):
        reports_dir = Path(__file__).parent.parent / 'reports'
        screenshot_path = reports_dir / f"{filename}.png"
        self.driver.save_screenshot(str(screenshot_path))
        return screenshot_path
