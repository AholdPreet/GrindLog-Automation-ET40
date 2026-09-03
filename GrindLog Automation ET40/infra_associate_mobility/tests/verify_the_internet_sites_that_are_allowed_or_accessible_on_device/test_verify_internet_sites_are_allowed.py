from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest, os, time
from utils.device_key_actions import DeviceKeyAction
from utils.screenshot_util import ScreenshotUtil
from utils.swipe_util import SwipeUtil 
from locators.internet_sites_locators import InternetSitesLocators as locator
from utils.auth.signin_launcher_helper import SigninLauncherHelper
from utils.data_util import DataUtil

class TestVerifyInternetSitesAreAllowed :

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
                        locator.EDGE_LOCATOR
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

    def test_open_edge(self):
        try :
            self.wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        locator.EDGE_LOCATOR
                    )
                )
            ).click()
            print(f"\nApplication opening...")
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "Edge_opening_Screenshot",
                test_file=__file__
            )
        except Exception as e :
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "Failed_to_open_edge_Screenshot",
                test_file=__file__
            )
            raise AssertionError(f"Failed to open edge : {e}")
    
    def test_serach_on_edge(self):
        try :
            # serch on edge browser (eg. google.com, microsoft.com)
            time.sleep(10)
            edge_search = self.wait.until(
                EC.element_to_be_clickable(
                    (
                        AppiumBy.XPATH,
                        locator.EDGE_SEARCH_LOCATOR
                    )
                )
            )
            print(f"\nEdge open successfully : {edge_search.text}")

            # checking the legit sites are accessible or not (zscaler wroking perfectly or not)
            for site in self.test_data['sites'] :
                edge_search.click()
                print(f"\nSearch box open : {site}")
                edge_search.send_keys(site)
                DeviceKeyAction.press_enter_btn(self.driver)
                time.sleep(10)
                ScreenshotUtil.take_screenshot(
                    driver= self.driver,
                    file_name= "Accessible_SITE_screenshot",
                    test_file=__file__
                )
                edge_back_btn = self.wait.until(
                    EC.element_to_be_clickable(
                        (
                            AppiumBy.XPATH,
                            locator.EDGE_BACK_Btn_LOCATOR
                        )
                    )
                )
                print("\nButton clicked : edge_back_btn")
                edge_back_btn.click()
        except Exception as e :
            ScreenshotUtil.take_screenshot(
                driver= self.driver,
                file_name= "Failed_to_access_site_screenshot",
                test_file=__file__
            )
            raise AssertionError(f"Failed to access the site : {e}")
    
    def test_navigate_back_to_home_screen(self):
        try :
            for _ in range(3):
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
    
    
    

