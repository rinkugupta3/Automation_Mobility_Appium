# pytest -s -v Appium_Android_Samsung_Google_App_Search.py
# pytest -s -v Appium_Android_Samsung_Google_App_Search.py --html=report.html
""" Following test will be performed:
Appium_Android_Samsung_Google_App_Search.py::test_open_chrome_app PASSED
Appium_Android_Samsung_Google_App_Search.py::test_activate_search_box PASSED
Appium_Android_Samsung_Google_App_Search.py::test_input_search_text PASSED
Appium_Android_Samsung_Google_App_Search.py::test_click_search_link PASSED
Appium_Android_Samsung_Google_App_Search.py::test_go_to_home PASSED
"""

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Define the driver fixture
@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Samsung_API_34"  # Specify the device name
    options.udid = "emulator-5556"  # Use the Samsung emulator's UDID
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    yield driver  # This will provide the driver to the test functions

    driver.quit()  # Quit the driver after the test is done


def open_chrome_app(driver):
    sleep(5)  # Wait for the app to load
    logger.info("App is loading...")
    chrome_element = driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="Chrome"]')
    chrome_element.click()
    logger.info("Chrome app opened!")
    sleep(10)  # Wait for Chrome to load


def activate_search_box(driver):
    wait = WebDriverWait(driver, 20)
    search_box = wait.until(EC.presence_of_element_located((By.ID, "com.android.chrome:id/url_bar")))
    search_box.click()  # Click on the search box to activate it
    logger.info("Search box activated!")
    sleep(10)


def input_search_text(driver):
    wait = WebDriverWait(driver, 20)
    search_box = wait.until(EC.presence_of_element_located((By.ID, "com.android.chrome:id/url_bar")))
    search_box.send_keys("apple\n")
    driver.press_keycode(66)  # Keycode 66 corresponds to Enter
    logger.info("Input 'apple' in the search box!")
    sleep(10)  # Wait for the page to load


def click_search_link(driver):
    wait = WebDriverWait(driver, 40)  # Increased timeout to 40 seconds
    apple_link = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[@text="Apple"]')))
    apple_link.click()
    logger.info("Clicked on the Apple official site link!")
    logger.info("Apple site opened successfully!")
    sleep(10)  # Wait to observe the results


# Each function will run as a separate test

def go_to_home(driver):
    # Use the Android back button to return to the home screen
    driver.press_keycode(3)  # Keycode 3 is the home button on Android
    logger.info("Navigated to home screen.")
    sleep(10)


@pytest.mark.usefixtures("driver")
def test_open_chrome_app(driver):
    open_chrome_app(driver)


@pytest.mark.usefixtures("driver")
def test_activate_search_box(driver):
    activate_search_box(driver)


@pytest.mark.usefixtures("driver")
def test_input_search_text(driver):
    input_search_text(driver)


@pytest.mark.usefixtures("driver")
def test_click_search_link(driver):
    click_search_link(driver)


@pytest.mark.usefixtures("driver")
def test_go_to_home(driver):
    go_to_home(driver)  # Navigate to home screen


# Run the tests using pytest
if __name__ == "__main__":
    pytest.main()
