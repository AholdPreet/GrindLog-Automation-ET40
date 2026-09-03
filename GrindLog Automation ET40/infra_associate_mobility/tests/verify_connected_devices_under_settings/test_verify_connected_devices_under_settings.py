from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest, os, time
from utils.device_key_actions import DeviceKeyAction
from utils.screenshot_util import ScreenshotUtil
from utils.swipe_util import SwipeUtil 
from locators.connected_devices_under_settings_locators import ConnectedDevicesUnderSettingsLocators as locator
from utils.auth.signin_launcher_helper import SigninLauncherHelper
from utils.data_util import DataUtil

class TestVerifyConnectedDevicesUnderSettings:

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

    def test_bluetooth(self):
        try:
            bluetooth_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH, 
                        locator.BLUETOOTH_LOCATOR
                    )
                )
            )
            print(f"\nButton clicked : {bluetooth_btn.text}")
            bluetooth_btn.click()
            try:
                msg = self.wait.until( 
	                EC.visibility_of_element_located(	
		                (                      
			                AppiumBy.ANDROID_UIAUTOMATOR,        
			                locator.MSG_LOCATOR                  
		                )                
	                )          
                )            
                print(f"\nMessage : {msg.text}")
                allow_btn = self.wait.until(
                    EC.element_to_be_clickable(
                        (
                            AppiumBy.XPATH, 
                            locator.ALLOW_Btn_LOCATOR
                        )
                    )
                )
                print(f"\nButton clicked : {allow_btn.text}")
                allow_btn.click()
            except TimeoutException:
                print("Permission popup not displayed")

            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="BLUETOOTH_screenshot",
                test_file=__file__
            )

        except Exception as e:
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Failed_to_open_BLUETOOTH_screenshot",
                test_file=__file__
            )
            raise AssertionError(f"Failed to open bluetooth : {e}")
    
    def test_device_info(self):
        try :
            print("\n--------Available devices--------")
            print(f"{'Device Name':<40} {'Status'}")
            
            printed_devices = []
            for _ in range(5):
                all_elements = self.wait.until(
                    EC.presence_of_all_elements_located(
                        (
                            AppiumBy.CLASS_NAME, 
                            "android.widget.TextView"
                        )
                    )
                )
                ignore = ["Bluetooth", "Devices", "Device Connection" ]
                i = 0
                while i < len(all_elements):
                    text = all_elements[i].text.strip()

                    if text and text not in ignore and not text.startswith("This device is discoverable"):
                        if i + 1 < len(all_elements):
                            status = all_elements[i + 1].text.strip()
                            #print(f"{text:<40} {status}")
                            if text not in printed_devices:                   
                                print(f"{text:<40} {status}")                   
                                printed_devices.append(text)
                        i += 2
                    else:
                        i += 1
                SwipeUtil.swipe_up(self.driver)
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="DEVICE_INFO_screenshot",
                test_file=__file__
            )
        except Exception as e :
            ScreenshotUtil.take_screenshot(
                driver=self.driver,
                file_name="Failed_to_see_DEVICE_INFO_screenshot",
                test_file=__file__
            )
            raise AssertionError(f"Failed to see device info : {e}")
    
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
        


        


        


    
   
        


            
            




    