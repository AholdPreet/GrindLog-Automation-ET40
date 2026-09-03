HOME = 3
BACK = 4
ENTER = 66
MENU = 82
RECENT_APPS = 187

class DeviceKeyAction:
   
    @staticmethod
    def press_home_btn(driver):
        driver.press_keycode(HOME)

    @staticmethod
    def press_back_btn(driver):
        driver.press_keycode(BACK)

    @staticmethod
    def press_enter_btn(driver):
        driver.press_keycode(ENTER)
    
    @staticmethod
    def press_menu_btn(driver):
        driver.press_keycode(MENU)

    @staticmethod
    def press_recent_apps_btn(driver):
        driver.press_keycode(RECENT_APPS)
