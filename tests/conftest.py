"""
Pytest configuration and fixtures.
"""

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from config.config import get_capabilities, APPIUM_SERVER, IMPLICIT_WAIT, PLATFORM


@pytest.fixture(scope="function")
def driver():
    """
    Fixture to provide Appium driver instance for each test.

    Yields:
        WebDriver: Appium driver instance
    """
    # Initialize driver
    caps = get_capabilities()

    if PLATFORM == 'ios':
        options = XCUITestOptions().load_capabilities(caps)
    else:
        options = UiAutomator2Options().load_capabilities(caps)

    driver_instance = webdriver.Remote(APPIUM_SERVER, options=options)
    driver_instance.implicitly_wait(IMPLICIT_WAIT)

    yield driver_instance

    # Teardown: quit driver after test
    driver_instance.quit()


@pytest.fixture(scope="session", autouse=True)
def test_session_setup():
    """Setup before all tests and cleanup after."""
    print("\n" + "="*50)
    print("Starting IDnow AutoIdent Test Session")
    print("="*50)
    yield
    print("\n" + "="*50)
    print("Test Session Complete")
    print("="*50)
