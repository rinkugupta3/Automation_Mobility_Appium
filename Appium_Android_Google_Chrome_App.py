# python Appium_Android_Google_Chrome_App.py
from appium import webdriver
from appium.options.android import UiAutomator2Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define the options for Android
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "Pixel 3a API 34"
options.udid = "emulator-5554"

# Initialize the Appium driver with options
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    # Wait for the app to load
    sleep(3)

    # Find and click the Chrome icon to open the browser
    chrome_element = driver.find_element(By.XPATH, '(//android.widget.TextView[@content-desc="Chrome"])[2]')
    chrome_element.click()
    print("Chrome app opened!")
    sleep(5)  # Wait for Chrome to load

    # Wait until the search box is visible
    wait = WebDriverWait(driver, 20)
    # search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.EditText[''@resource-id="com.android.chrome:id/search_box_text"]')))
    search_box = wait.until(EC.presence_of_element_located((By.ID, "com.android.chrome:id/url_bar")))
    search_box.click()  # Click on the search box to activate it
    print("Search box activated!")
    sleep(5)

    # Enter the URL "apple.com" in the search box
    search_box.send_keys("apple\n")
    driver.press_keycode(66)  # Keycode 66 corresponds to Enter
    print("Input 'apple' in the search box!")
    sleep(2)

    apple_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.View[@text="Apple | Official Site"]')))
    apple_link.click()
    print("Clicked on the Apple official site link!")
    print("Apple site opened successfully!")

    # Wait to observe the results
    sleep(5)

finally:
    # Quit the driver
    driver.quit()
