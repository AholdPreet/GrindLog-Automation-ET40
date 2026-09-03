from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators.signin_launcher_helper_locators import SigninLauncherHelperLocators as locator
from utils.coordinate_click import CoordinateClick
from utils.screenshot_util import ScreenshotUtil
import time

class SigninLauncherHelper:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def sign_in(self, username, password, test_file):
        try:
            self.wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH, 
                        locator.SIGNIN_Btn_LOCATOR
                    )
                )
            ).click()
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Signin_Screenshot",
                test_file=test_file
            )

        except Exception as e:
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Signin_Button_Failed",
                test_file=test_file
            )
            raise AssertionError(f"Failed to click SIGN-IN button: {e}")

        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.XPATH, 
                        locator.USERNAME_LOCATOR
                    )
                )
            ).send_keys(username)
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Username_Entered",
                test_file=test_file
            )

        except Exception as e:
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Username_Entry_Failed",
                test_file=test_file
            )
            raise AssertionError(f"Failed to enter username: {e}")

        try:
            self.wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH, 
                        locator.NEXT_Btn_LOCATOR
                    )
                )
            ).click()
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Username_Screenshot",
                test_file=test_file
            )

        except Exception as e:
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Next_Button_Failed",
                test_file=test_file
            )
            raise AssertionError(f"Failed to click Next button: {e}")

        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.XPATH, 
                        locator.PASSWORD_LOCATOR
                    )
                )
            ).send_keys(password)
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Password_Entered",
                test_file=test_file
            )

        except Exception as e:
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Password_Entry_Failed",
                test_file=test_file
            )
            raise AssertionError(f"Failed to enter password: {e}")

        try:
            self.wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH, 
                        locator.SI_Btn_LOCATOR
                    )
                )
            ).click()
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Password_Screenshot",
                test_file=test_file
            )

        except Exception as e:
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="SignIn_Submit_Failed",
                test_file=test_file
            )
            raise AssertionError(f"Failed to click Sign In button: {e}")

        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.CLASS_NAME,
                        "android.widget.FrameLayout"
                    )
                )
            )
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Temp_PIN_Screenshot",
                test_file=test_file
            )

        except Exception as e:
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Temp_PIN_Screen_Failed",
                test_file=test_file
            )
            raise AssertionError(f"Temporary PIN screen not displayed: {e}")

        try:
            time.sleep(10)

            CoordinateClick.coordinate_click(driver= self.driver, x=544, y= 944, label="2")
            CoordinateClick.coordinate_click(driver= self.driver, x=535, y= 1670, label="0")
            CoordinateClick.coordinate_click(driver= self.driver, x=544, y= 944, label="2")
            CoordinateClick.coordinate_click(driver= self.driver, x=803, y= 1181, label="6") 
            
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Confirm_Temp_PIN_Screenshot",
                test_file=test_file
            )
            CoordinateClick.coordinate_click(driver= self.driver, x=544, y= 944, label="2")
            CoordinateClick.coordinate_click(driver= self.driver, x=535, y= 1670, label="0")
            CoordinateClick.coordinate_click(driver= self.driver, x=544, y= 944, label="2")
            CoordinateClick.coordinate_click(driver= self.driver, x=803, y= 1181, label="6") 

        except Exception as e:
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Confirm_PIN_Entry_Failed",
                test_file=test_file
            )
            raise AssertionError(f"Failed to enter PIN: {e}")

        self.verify_store(test_file)

    def verify_store(self, test_file):

        try:
            store_text = self.wait.until(
                EC.visibility_of_element_located(
                    (AppiumBy.XPATH, locator.STORE_NUMBER)
                )
            ).text

            print(f"Store Message: {store_text}")

            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Store_Number_Screenshot",
                test_file=test_file
            )

            assert "You are at store" in store_text, (
                f"Expected store message not found. Actual text: {store_text}"
            )

        except Exception as e:
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Store_Validation_Failed",
                test_file=test_file
            )
            raise AssertionError(f"Store validation failed: {e}")