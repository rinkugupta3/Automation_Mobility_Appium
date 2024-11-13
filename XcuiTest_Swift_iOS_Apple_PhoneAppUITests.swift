import XCTest

class PhoneAppUITests: XCTestCase {

    var app: XCUIApplication!

    override func setUpWithError() throws {
        continueAfterFailure = false
        app = XCUIApplication()
        app.launch()
    }

    override func tearDownWithError() throws {
        app.terminate()
    }

    func testOpenPhoneApp() throws {
        // Wait for the app to load
        sleep(5)
        print("App is loading...")

        // Find and tap the Phone app element
        let phoneElement = app.staticTexts["Phone"]
        XCTAssertTrue(phoneElement.exists, "Phone app not found")
        phoneElement.tap()

        print("Phone app opened!")
        sleep(10) // Wait for Phone app to load
    }

    func testClickKeyPad() throws {
        // Ensure the app is ready
        sleep(5)

        // Find and tap the Keypad button
        let keyPadElement = app.buttons["key pad"]
        XCTAssertTrue(keyPadElement.exists, "Key pad button not found")
        keyPadElement.tap()

        print("Key pad opened!")
        sleep(10) // Wait for Key pad to load
    }

    func testClickPhoneDigit() throws {
        // Add logic to click on phone digits
        sleep(5)
        print("Clicking phone digits...")
        let digitElement = app.buttons["1"] // Replace with the appropriate digit button identifier
        XCTAssertTrue(digitElement.exists, "Digit button not found")
        digitElement.tap()
        print("Digit clicked!")
    }

    func testClickCallButton() throws {
        // Add logic to click the call button
        sleep(5)
        print("Clicking call button...")
        let callButtonElement = app.buttons["call"] // Replace with the appropriate call button identifier
        XCTAssertTrue(callButtonElement.exists, "Call button not found")
        callButtonElement.tap()
        print("Call button clicked!")
    }

    func testClickEndCall() throws {
        // Add logic to click the end call button
        sleep(5)
        print("Clicking end call button...")
        let endCallButtonElement = app.buttons["end call"] // Replace with the appropriate end call button identifier
        XCTAssertTrue(endCallButtonElement.exists, "End call button not found")
        endCallButtonElement.tap()
        print("End call button clicked!")
    }

    func testGoToHome() throws {
        // Add logic to navigate to the home screen
        print("Navigating to home screen...")
        app.buttons["home"].tap() // Replace with the appropriate home button identifier
        print("Navigated to home screen.")
    }
}
