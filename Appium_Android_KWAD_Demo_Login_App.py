# UiAutomator2Options: This is used to create an options object specifically for Android with the UiAutomator2 automation engine.
# python Appium_Android_KWAD_Demo_Login_App.py
from appium import webdriver
from appium.options.android import UiAutomator2Options
from time import sleep

# Define the options for Android
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "Pixel 3a API 34"
options.udid = "emulator-5554"
options.app_package = "com.code2lead.kwad"
options.app_activity = "com.code2lead.kwad.MainActivity"

# Initialize the Appium driver with options
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    # Wait for the app to load
    sleep(1)

    print("KWADemo app is opened successfully!")

    # Find and click the LOGIN button
    login_button = driver.find_element("id", "com.code2lead.kwad:id/Login")  # Using the correct ID
    login_button.click()

    print("LOGIN button clicked!")
    sleep(10)

    # Find and fill the email input field
    email_field = driver.find_element("id", "com.code2lead.kwad:id/Et4")
    email_field.send_keys("admin@gmail.com")  # Enter the email
    sleep(3)

    # Find and fill the password input field
    password_field = driver.find_element("id", "com.code2lead.kwad:id/Et5")  # Update this line for the correct ID
    password_field.send_keys("admin123")  # Enter the password
    sleep(3)

    # Find and click the LOGIN button
    login_button = driver.find_element("id", "com.code2lead.kwad:id/Btn3")  # Use the ID for the LOGIN button
    login_button.click()

    print("LOGIN Successfully")

    # Find and fill the next EditText field after login
    # admin_field = driver.find_element("id", "com.code2lead.kwad:id/Edt_admin")
    admin_field = driver.find_element("xpath",
                                      "//android.widget.EditText[@resource-id='com.code2lead.kwad:id/Edt_admin']")
    admin_field.send_keys("John")  # Enter the text needed

    # Find and click the next button (Admin Submit button)
    admin_submit_button = driver.find_element("id", "com.code2lead.kwad:id/Btn_admin_sub")
    admin_submit_button.click()
    print("Admin Submit button clicked!")

    # Wait for a while to observe the app being opened
    sleep(20)

finally:
    # Quit the driver
    driver.quit()


