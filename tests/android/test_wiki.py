import os
import pytest
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    load_dotenv()
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        # Set URL of the application under test
        "app": "bs://sample.app",

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": os.getenv('BSTACK_USER'),
            "accessKey": os.getenv('BSTACK_KEY'),
        }
    })

    browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()


def test_one():
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    assert 1 == 1


def test_two():
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()

    assert 1 == 1
