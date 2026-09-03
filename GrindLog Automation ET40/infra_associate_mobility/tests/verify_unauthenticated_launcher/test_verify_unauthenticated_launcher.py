import pytest, time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot_util import ScreenshotUtil
from utils.swipe_util import SwipeUtil
from utils.device_key_actions import DeviceKeyAction
from utils.data_util import DataUtil
from locators.unauthenticated_launcher_locators import UnauthenticatedLauncherLocators as locator

class TestVerifyUnauthenticatedLauncher :

    @pytest.fixture(autouse = True)
    def setup(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def test_unauthenticated_launcher_home_screen(self):
        try :
            DeviceKeyAction.press_home_btn(self.driver)
            SwipeUtil.swipe_left(self.driver)
            print("Left swipe")
            store_number = self.wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.XPATH,
                        locator.STORE_NUMBER
                    )
                )
            )
            print(f"Store Message: {store_number.text}")
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.XPATH,
                        locator.SIGNIN_Btn_LOCATOR
                    )
                )
            )
            time.sleep(5)
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "unauthenticated_LAUNCHER_screenshot",
                test_file= __file__
            )
            DeviceKeyAction.press_home_btn(self.driver)
        except Exception as e:
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "Failed_to_open_unauthenticated_LAUNCHER_screenshot",
                test_file= __file__
            )
            raise AssertionError(f"Failed to open unauthenticated launcher : {e}")

    