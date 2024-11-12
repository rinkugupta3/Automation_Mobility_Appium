import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define the driver fixture for iOS
@pytest.fixture(scope="function")
def driver():
    options = XCUITestOptions()
    options.platform_name = "iOS"
    options.device_name = "iPhone X"  # Ensure this matches your real device name
    options.platform_version = "14.0"  # Replace with your iOS version
    options.udid = "YOUR_DEVICE_UDID"  # Replace with the UDID of your device
    options.app = "com.apple.mobilesafari"  # Safari bundle ID for browser testing

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    yield driver  # This will provide the driver to the test functions

    driver.quit()  # Quit the driver after the test is done


def open_safari_app(driver):
    sleep(5)  # Wait for the app to load
    logger.info("Opening Safari app...")
    # For iOS, launching Safari typically involves using the bundle ID
    driver.activate_app("com.apple.mobilesafari")
    logger.info("Safari app opened!")
    sleep(10)  # Wait for Safari to load


def activate_search_bar(driver):
    wait = WebDriverWait(driver, 20)
    search_bar = wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "URL")))
    search_bar.click()
    logger.info("Search bar activated!")
    sleep(10)


def input_search_text(driver):
    wait = WebDriverWait(driver, 20)
    search_bar = wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, "URL")))
    search_bar.send_keys("apple\n")
    logger.info("Input 'apple' in the search bar!")
    sleep(10)  # Wait for the page to load


def click_search_link(driver):
    wait = WebDriverWait(driver, 40)
    apple_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//XCUIElementTypeLink[@name="Apple"]')))
    apple_link.click()
    logger.info("Clicked on the Apple official site link!")
    logger.info("Apple site opened successfully!")
    sleep(10)  # Wait to observe the results


def go_to_home(driver):
    # For iOS, use `driver.terminate_app("com.apple.mobilesafari")` to return to the home screen or swipe up gesture.
    driver.terminate_app("com.apple.mobilesafari")
    logger.info("Navigated to home screen.")
    sleep(10)


@pytest.mark.usefixtures("driver")
def test_open_safari_app(driver):
    open_safari_app(driver)


@pytest.mark.usefixtures("driver")
def test_activate_search_bar(driver):
    activate_search_bar(driver)


@pytest.mark.usefixtures("driver")
def test_input_search_text(driver):
    input_search_text(driver)


@pytest.mark.usefixtures("driver")
def test_click_search_link(driver):
    click_search_link(driver)


@pytest.mark.usefixtures("driver")
def test_go_to_home(driver):
    go_to_home(driver)


# Run the tests using pytest
if __name__ == "__main__":
    pytest.main()
