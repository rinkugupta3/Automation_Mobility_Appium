# pytest -s -v Appium_Android_Samsung_Phone_App.py
# In this script, we will perform the following actions:
# 1. Open the Phone app
# 2. Click on the digits 2, 3, 4, 5, 6, 7, 8, 9, 0, 1
# 3. Click on the call button
# 4. Click on the end call button
# 5. Navigate to the home screen
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


# Test function to open the Phone app
def open_phone_app(driver):
    sleep(5)  # Wait for the app to load
    logger.info("App is loading...")
    phone_element = driver.find_element(By.XPATH, "//android.widget.TextView[@content-desc='Phone']")
    phone_element.click()
    logger.info("Phone app opened!")
    sleep(10)  # Wait for Phone app to load


def click_key_pad(driver):
    sleep(5)  # Wait for the app to load if necessary
    logger.info("Key pad clicked!")
    key_pad_element = driver.find_element(By.XPATH, "//android.widget.ImageButton[@content-desc='key pad']")
    key_pad_element.click()
    logger.info("Key pad opened!")
    sleep(10)  # Wait for Key pad to load


"""
def click_phone_digit(driver):
    wait = WebDriverWait(driver, 20)

    # Step to clear existing phone number from the input field
    try:
        # Wait for the backspace button to be clickable
        delete_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//android.widget.ImageButton[@content-desc='backspace']")
        ))

        # Click the backspace button until the input field is empty
        while True:
            try:
                # Check if there's any text left in the field
                phone_input = driver.find_element(By.ID,
                                                  "com.google.android.dialer:id/number")  # Example ID of the phone input field
                if phone_input.text:  # If there is text, click backspace to delete one digit
                    delete_button.click()
                    logger.info("Clicked backspace to clear one digit.")
                    sleep(1)  # Wait briefly to ensure it's cleared one digit
                else:
                    break  # Exit loop when input field is empty
            except Exception as e:
                logger.warning(f"Failed to clear the input field: {e}")
                break  # Exit loop if there's an issue
    except Exception as e:
        logger.warning(f"Backspace button not found: {e}")

    # List of digits to click (2, 3, 4, 5, 6, etc.)
    digits = ['2', '3', '4', '5', '6', '7', '8', '9', '0', '1']

    for digit in digits:
        # Wait for each digit to be present and interactable, then click
        digit_element = wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//android.widget.TextView[@text='{digit}']")
        ))
        digit_element.click()  # Click the digit to simulate dialing
        logger.info(f"Digit '{digit}' clicked on the phone app!")
        sleep(2)  # Adjust sleep duration as needed for better timing

"""


def click_phone_digit(driver):
    wait = WebDriverWait(driver, 20)

    # List of digits to click (2, 3, 4, 5, 6)
    digits = ['2', '3', '4', '5', '6', '7', '8', '9', '0', '1']

    for digit in digits:
        # Wait for each digit to be present and interactable, then click
        digit_element = wait.until(EC.presence_of_element_located(
            (By.XPATH, f"//android.widget.TextView[@text='{digit}']")
        ))
        digit_element.click()  # Click the digit to simulate dialing
        logger.info(f"Digit '{digit}' clicked on the phone app!")
        sleep(2)  # Adjust sleep duration as needed for better timing


def click_call_button(driver):
    wait = WebDriverWait(driver, 20)  # Timeout of 40 seconds

    # Wait for the call button to be clickable and click it
    call_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//android.widget.Button[@content-desc="dial"]')
    ))
    call_button.click()
    logger.info("Clicked on the call button!")
    logger.info("Call initiated successfully!")
    sleep(10)  # Wait to observe the results


def click_end_call(driver):
    wait = WebDriverWait(driver, 20)  # Timeout of 40 seconds

    # Wait for the end call button to be clickable and click it
    end_call_button = wait.until(EC.element_to_be_clickable(
        (By.ID, 'com.google.android.dialer:id/incall_end_call')))
    end_call_button.click()
    logger.info("Clicked on the end call button!")
    logger.info("Call ended successfully!")
    sleep(5)  # Wait to observe the results


def go_to_home(driver):
    # Use the Android back button to return to the home screen
    driver.press_keycode(3)  # Keycode 3 is the home button on Android
    logger.info("Navigated to home screen.")
    sleep(10)


@pytest.mark.usefixtures("driver")
def test_open_phone_app(driver):
    open_phone_app(driver)


def test_click_key_pad(driver):
    click_key_pad(driver)


@pytest.mark.usefixtures("driver")
def test_click_phone_digit(driver):
    click_phone_digit(driver)


@pytest.mark.usefixtures("driver")
def test_click_call_button(driver):
    click_call_button(driver)


@pytest.mark.usefixtures("driver")
def test_click_end_call(driver):
    click_end_call(driver)


def test_go_to_home(driver):
    go_to_home(driver)  # Navigate to home screen


# Run the tests using pytest
if __name__ == "__main__":
    pytest.main()
