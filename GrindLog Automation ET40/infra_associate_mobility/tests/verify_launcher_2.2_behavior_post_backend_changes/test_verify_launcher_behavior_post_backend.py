from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pytest, os, time
from utils.device_key_actions import DeviceKeyAction
from utils.screenshot_util import ScreenshotUtil
from utils.swipe_util import SwipeUtil 
from utils.auth.signin_launcher_helper import SigninLauncherHelper
from utils.data_util import DataUtil

class TestVerifyLauncherBehaviorPostBackend : 

    @pytest.fixture(autouse = True)
    def setup(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.cred_data = DataUtil.load_json(
            os.path.join(
                os.path.dirname(__file__),
                "test_data",
                "test_data.json"
            )
        )["cred"]
    
    def test_signin_launcher(self):
        SigninLauncherHelper(self.driver).sign_in(
            # username= "tst_s2528sm@delhaizet.com",
            # password= 'Temp@123',
            username= self.cred_data['username'],
            password= self.cred_data['password'],
            test_file=__file__
        )
        print("Login successful")
        print("\nNow reboot/remove the battery and connect it back")


