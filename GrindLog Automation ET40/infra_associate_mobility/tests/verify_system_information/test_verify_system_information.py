from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest, os, time
from utils.device_key_actions import DeviceKeyAction
from utils.screenshot_util import ScreenshotUtil
from utils.swipe_util import SwipeUtil 
from locators.system_information_locators import SystemInformationLocators as locator
from utils.auth.signin_launcher_helper import SigninLauncherHelper
from utils.data_util import DataUtil 

class TestVerifySystemInformation:

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

    def test_open_system_information(self):
        try :
            system_info_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        locator.SYSTEM_INFO_BUTTON_LOCATOR
                        #'//android.view.View[@content-desc="System Info"]'
                    )
                )
            )
            system_info_btn.click()
            tittle = self.wait.until(
                EC.visibility_of_element_located(
                    (
                        AppiumBy.XPATH, 
                        locator.SYSTEM_INFO_TITLE_LOCATOR
                        #'//android.widget.TextView[@text="System Information"]'
                    )
                )
            )
            print(f"TITLE : {tittle.text}")
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "TC53_screenshot_system_information_screen",
                test_file= __file__
            )
        except Exception as e  :
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "ERROR_screenshot_system_info_btn_NOT_FOUND",
                test_file= __file__
            )
            raise AssertionError(f"System information button (i) not found, Error : {str(e)}")

    def test_connection_status_label(self):
        self.validate_lable(
            xpath_type=AppiumBy.XPATH,
            appium_xpath_label= locator.CONNECTION_STATUS_LABEL_LOCATOR,
            label_value= self.test_data["connection_status_value"],   # expected value
            appium_xpath_label_value= locator.CONNECTION_STATUS_VALUE_LOCATOR,
            screenshot_name= 'TC53_screenshot_connection_status_label_screen'
        )

    def test_network_name_label(self):
        self.validate_lable(
            xpath_type=AppiumBy.XPATH,
            appium_xpath_label= locator.NETWORK_NAME_LABEL_LOCATOR,
            label_value= self.test_data["network_name_value"],  # expected value
            appium_xpath_label_value= locator.NETWORK_NAME_VALUE_LOCATOR,
            screenshot_name= 'TC53_screenshot_network_name_lable_screen'
        )
    
    def test_device_MAC_address_label(self):
        self.validate_lable(
            xpath_type=AppiumBy.XPATH,
            appium_xpath_label= locator.DEVICE_MAC_LABEL_LOCATOR,
            label_value= self.test_data["device_MAC_address_value"],   # expected value
            appium_xpath_label_value= locator.DEVICE_MAC_VALUE_LOCATOR,
            screenshot_name= 'TC53_screenshot_device_MAC_address_screen'
        )
    
    def test_device_signal_label(self):
        self.validate_lable(
            xpath_type=AppiumBy.XPATH,
            appium_xpath_label= locator.SIGNAL_LABEL_LOCATOR,
            label_value= self.test_data["signal_label"],   # expected value
            appium_xpath_label_value= locator.SIGNAL_VALUE_LOCATOR,
            screenshot_name= 'TC53_screenshot_signal_screen'
        )

    def test_device_IP_address_label(self):
        self.validate_lable(
            xpath_type=AppiumBy.XPATH,
            appium_xpath_label= locator.DEVICE_IP_ADDRESS_LABEL_LOCATOR,
            label_value= self.test_data["device_IP_address_value"],  # expected value
            appium_xpath_label_value=locator.DEVICE_IP_ADDRESS_VALUE_LOCATOR,
            screenshot_name= 'TC53_screenshot_device_IP_address_screen'
        )

    def test_device_serial_number_label(self):
        self.scroll_into_view()
        self.validate_lable(
            xpath_type=AppiumBy.XPATH,
            appium_xpath_label= locator.DEVICE_SERIAL_LABEL_LOCATOR,
            label_value= self.test_data["device_serial_number_value"],
            appium_xpath_label_value= locator.DEVICE_SERIAL_VALUE_LOCATOR,
            screenshot_name='TC53_screenshot_device_serial_number_screen'
        )

    def test_android_version_label(self):
        self.validate_lable(
            xpath_type=AppiumBy.XPATH,
            appium_xpath_label=locator.ANDROID_VERSION_LABEL_LOCATOR,
            label_value=self.test_data["android_version_value"],
            appium_xpath_label_value= locator.ANDROID_VERSION_VALUE_LOCATOR,
            screenshot_name='TC53_screenshot_android_version_screen'
        )

    def test_launcher_vserion_label(self):
        self.validate_lable(
            xpath_type=AppiumBy.XPATH,
            appium_xpath_label= locator.LAUNCHER_VERSION_LABEL_LOCATOR,
            label_value=self.test_data["launcher_vserion_value"],
            appium_xpath_label_value=locator.LAUNCHER_VERSION_VALUE_LOCATOR,
            screenshot_name='TC53_screenshot_launcher_vserion_screen'
        )

    def test_navigate_back_to_home_screen(self):
        #self.driver.press_keycode(3)
        DeviceKeyAction.press_home_btn(self.driver)

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

    def validate_lable(self, xpath_type, appium_xpath_label, label_value, appium_xpath_label_value, screenshot_name):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(
                    ( 
                        xpath_type,
                        appium_xpath_label
                    )
                )
            )
            element_value = self.wait.until(
                EC.visibility_of_element_located(
                   (
                        xpath_type,
                        appium_xpath_label_value
                   )
                )
            )
            print(f"\n{element.text} : {element_value.text}")
            assert element_value.text == label_value
            print(f"VALIDATED : {element_value.text}")
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= screenshot_name,
                test_file= __file__
            )
            
        except Exception as e  :
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= f"ERROR_screenshot_{element.text}_NOT_FOUND",
                test_file= __file__
            )
            raise TimeoutException (f"{element.text} not found, ERROR : {str(e)}")

    def scroll_into_view(self):
        for _ in range(10):
            try:
                element = self.wait.until(
                    EC.visibility_of_element_located(
                        ( 
                            AppiumBy.XPATH,
                            locator.REFRESH_LAUNCHER_LOCATOR
                            #'//android.widget.TextView[@text="Refresh Launcher Apps"]'
                        )
                    )
                )
                print(f"\nSCROLL INTO VIEW : {element.text}")
                break
            except:
                # size = self.driver.get_window_size()
                # self.driver.swipe(
                #     size['width']//2,
                #     int(size['height']*0.8),
                #     size['width']//2,
                #     int(size['height']*0.2),
                #     1000
                # )
                SwipeUtil.swipe_up(self.driver)
    

        
    
    