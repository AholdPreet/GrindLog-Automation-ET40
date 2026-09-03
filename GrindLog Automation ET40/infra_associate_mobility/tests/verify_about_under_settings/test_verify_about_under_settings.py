from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest, os, time
from utils.device_key_actions import DeviceKeyAction
from utils.screenshot_util import ScreenshotUtil
from utils.swipe_util import SwipeUtil 
from locators.about_under_settings_locators import AboutUnderSettingsLocators as locator
from utils.auth.signin_launcher_helper import SigninLauncherHelper
from utils.data_util import DataUtil

class TestVerifyAboutUnderSettings:

    @pytest.fixture(autouse = True)
    def setup(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        path = DataUtil.load_json(
                os.path.join(
                    os.path.dirname(__file__),
                    "test_data",
                    "test_data.json"
                )
            )
        self.cred_data = path["cred"]
        self.test_data = path["test_data"]
    
    def test_signin_launcher(self):
        SigninLauncherHelper(self.driver).sign_in(
            # username= "tst_s2528sm@delhaizet.com",
            # password= 'Temp@123',
            username= self.cred_data['username'],
            password= self.cred_data['password'],
            test_file=__file__
        )
        print("Login successful")

    def test_open_app_drawer(self):
        try :
            btn = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        locator.APP_DRAWER_LOCATOR
                    )
                )
            )
            print(f"\nButton clicked : {btn.text}")
            btn.click()
            ele = self.wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.XPATH,
                        locator.ALL_APPLICATION_TEXT_LOCATOR
                    )
                )
            )
            print(f"\nText : {ele.text}")
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "APP_DRAWER_open_screenshot",
                test_file= __file__
            )
        except Exception as e :
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "Failed_to_open_APP_DRAWER_screenshot",
                test_file= __file__
            )
            raise AssertionError(f"Failed_to_open_app_drawer : {e}")
    
    def test_serach_application(self):
        try :
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.XPATH,
                        locator.SEARCH_BOX_LOCATOR
                    )   
                )      
            ).send_keys(self.test_data['application_name'])
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.XPATH,
                        locator.SETTINGS_LOCATOR
                    )
                )
            )
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "APPLICATION_found_screenshot",
                test_file=__file__
            )
        except Exception as e :
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "Failed_to_find_settings_APPLICATION_screenshot",
                test_file=__file__
            )
            raise AssertionError (f"Failed_to_find_settings_application : {e}")

    def test_open_settings(self):
        try :
            # DeviceKeyAction.press_home_btn(self.driver)
            # SwipeUtil.swipe_left(self.driver)
            btn = self.wait.until(
            EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        locator.SETTINGS_LOCATOR
                    )
                )
            )
            print(f"\nButton Clicked : {btn.text}")
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "Settings_Screenshot",
                test_file=__file__
            )
            btn.click()
            self.wait.until(
                EC.invisibility_of_element_located(
                    (
                        AppiumBy.XPATH,
                        locator.USB_DEBUGGINF_ALERT_LOCATOR
                    )
                )
            )
            print(f"\nUSB... alert dismiss")
        except Exception as e :
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "Failed_to_click_SETTINGS_btn_Screenshot",
                test_file=__file__
            )
            raise AssertionError(f"Failed to click SETTINGS button : {e}")
    
    def test_open_about_screen(self):
        try:
            element_locator = (
                AppiumBy.ANDROID_UIAUTOMATOR,
                locator.ABOUT_LOCATOR
                #AppiumBy.XPATH,
                #'//android.widget.TextView[@text="About"]'
            )
            about_btn = self.wait.until(
                EC.element_to_be_clickable(
                    element_locator
                )
            )
            about_btn.click()
            print(f"\nButton clicked : {about_btn.text}")
            element = self.wait.until(
                EC.visibility_of_element_located(
                    element_locator
                )
            )
            print(f"\nTitle : {element.text}")
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "ABOUT_screenshot",
                test_file= __file__
            )
            self.scroll_into_view()
            time.sleep(5)
            self.wait.until(
                EC.visibility_of_element_located(

                    (
                        AppiumBy.ANDROID_UIAUTOMATOR,
                        locator.ANDROID_VERSION_LOCATOR
                    )
                )
            )
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "ABOUT_the_device_screenshot",
                test_file= __file__
            )
        except TimeoutError:
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "Failed_to_open_ABOUT_screenshot",
                test_file= __file__
            )
            raise AssertionError(f"Failed to open about : {str(e)}")
    
    # def test_navigate_back_to_home_screen(self):
    #     #self.driver.press_keycode(3)
    #     DeviceKeyAction.press_back_btn(self.driver)
    #     self.wait.until(
    #         EC.visibility_of_element_located(
    #             (
    #                 AppiumBy.ANDROID_UIAUTOMATOR, 
    #                 locator.SETTINGS_LOCATOR
    #                 #AppiumBy.XPATH, 
    #                 #'//android.widget.TextView[@text="Settings"]'
    #             )
    #         )
    #     )
    #     DeviceKeyAction.press_home_btn(self.driver)
    def test_navigate_back_to_home_screen(self):
        try :
            for _ in range(3):
                DeviceKeyAction.press_back_btn(self.driver)
                try :
                    usb_debugging_alert = self.wait.until(
                        EC.visibility_of_element_located(
                            (
                                AppiumBy.XPATH,
                                locator.USB_DEBUGGINF_ALERT_LOCATOR
                            )   
                        )
                    )
                    if usb_debugging_alert :
                        self.wait.until(
                            EC.invisibility_of_element(
                                (
                                    AppiumBy.XPATH,
                                    locator.USB_DEBUGGINF_ALERT_LOCATOR
                                )
                            )
                        )
                        print("\nUSB debugging alert closed")
                except Exception :
                    pass
            #DeviceKeyAction.press_home_btn(self.driver)
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "Navigate_back_HOME_Screenshot",
                test_file=__file__
            )
        except Exception as e :
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "Failed_to_navigate_back_to_HOME_Screenshot",
                test_file=__file__
            )
            raise AssertionError(f"Failed to navigate back to home screen : {e}")
    
    def test_signout_launcher(self):
        try :
            self.wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.XPATH,
                        locator.LOGOUT_Btn_LOCATOR
                    )
                )
            ).click()
            time.sleep(5)
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "Logout_Screenshot",
                test_file=__file__
            )
            print("Logout successful")
        except Exception as e :
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "Failed_to_click_logout_btn_Screenshot",
                test_file=__file__
            )
            raise AssertionError (f"failed to click LOGOUT BUTTON : {e}")
    
    def scroll_into_view(self):
        for _ in range(10):
            try:
                element = self.wait.until(
                    EC.visibility_of_element_located(
                        ( 
                            AppiumBy.ANDROID_UIAUTOMATOR, 
                            locator.ANDROID_VERSION_LOCATOR
                            #AppiumBy.XPATH,
                            #'//android.widget.TextView[@text="Android Version"]'
                        )
                    )
                )
                print(f"\nSCROLL INTO VIEW : {element.text}")
                break
            except:
                SwipeUtil.swipe_up(self.driver)
                





