"""
Configuration file for Appium test execution.
Contains desired capabilities for Android and iOS platforms.
"""

import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Test Data
# Override with environment variable
TEST_IDENT_ID = os.getenv('IDENT_ID', 'TEST123456')

# Timeouts (in seconds)
IMPLICIT_WAIT = 10
EXPLICIT_WAIT = 20
PAGE_LOAD_TIMEOUT = 30

# Appium Server
APPIUM_SERVER = 'http://localhost:4723'

# Android Configurations
ANDROID_CAPS = {
    'platformName': 'Android',
    'platformVersion': '13.0',  # Adjust versions
    'deviceName': 'Android Emulator',
    'automationName': 'UiAutomator2',
    'app': str(PROJECT_ROOT / 'apps' / 'idnow-autoident.apk'),  # Path to APK
    'appPackage': '',  # Replace with actual package name
    'appActivity': '',  # Replace with actual activity
    'noReset': False,
    'fullReset': False,
    'newCommandTimeout': 300,
    'autoGrantPermissions': True,
    'language': 'en',
    'locale': 'US'
}

# iOS Configurations
IOS_CAPS = {
    'platformName': 'iOS',
    'platformVersion': '16.0',  # Adjust versions
    'deviceName': 'iPhone 14',
    'automationName': 'XCUITest',
    'app': str(PROJECT_ROOT / 'apps' / 'IDnowAutoIdent.ipa'),  # Path to IPA
    'bundleId': '',  # Replace with actual bundle ID
    'noReset': False,
    'fullReset': False,
    'newCommandTimeout': 300,
    'autoAcceptAlerts': True,
    'language': 'en',
    'locale': 'en_US'
}

# Select active platform
PLATFORM = os.getenv('PLATFORM', 'android').lower()  # android or ios


def get_capabilities():
    """Return the appropriate capabilities based on platform."""
    if PLATFORM == 'ios':
        return IOS_CAPS
    else:
        return ANDROID_CAPS
