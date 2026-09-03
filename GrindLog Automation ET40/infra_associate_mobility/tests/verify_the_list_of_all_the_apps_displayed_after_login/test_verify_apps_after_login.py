from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest, os, time
from utils.device_key_actions import DeviceKeyAction
from utils.screenshot_util import ScreenshotUtil
from utils.swipe_util import SwipeUtil 
from locators.apps_after_login_locators import AppAfterLoginLocators as locator
from utils.auth.signin_launcher_helper import SigninLauncherHelper
from utils.data_util import DataUtil

class TestVerifySSOFeatureWorks :

    @pytest.fixture(autouse=True)
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
        banner = "GIANT_Company"
        self.cred_data = path[banner]["cred"]
        self.test_data = path[banner]["test_data"]
    
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
        for application_name in self.test_data['application_name']:
            try:
                print(f"\nSearching application : {application_name}")
                search_box = self.wait.until(
                    EC.visibility_of_element_located(
                        (
                            AppiumBy.XPATH,
                            locator.SEARCH_BOX_LOCATOR
                        )
                    )
                )
                search_box.clear()
                search_box.send_keys(application_name)
                self.wait.until(
                    EC.visibility_of_element_located(
                        (
                            AppiumBy.XPATH,
                            f'//android.widget.TextView[contains(@text,"{application_name}")]'
                        )
                    )
                )
                print(f"{application_name} : is present")
                ScreenshotUtil.take_screenshot(
                    driver=self.driver,
                    file_name=f"{application_name}_found_screenshot",
                    test_file=__file__
                )
            except Exception:
                print(f"{application_name} : is not found")
                ScreenshotUtil.take_screenshot(
                    driver=self.driver,
                    file_name=f"{application_name}_not_found_screenshot",
                    test_file=__file__
                )

            finally:
                try:
                    self.wait.until(
                        EC.element_to_be_clickable(
                            (
                                AppiumBy.XPATH,
                                locator.CLEAR_Btn_LOCATORS
                            )
                        )
                    ).click()
                except:
                    pass

    def test_navigate_back_to_home_screen(self):
        #self.driver.press_keycode(3)
        try :
            for _ in range(2):
                DeviceKeyAction.press_back_btn(self.driver)
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
            raise AssertionError (f"Failed to click LOGOUT BUTTON : {e}")
    
    
    
    
    