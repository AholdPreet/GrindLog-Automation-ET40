import os
from datetime import datetime

class ScreenshotUtil:

    @staticmethod
    def take_screenshot(driver, file_name, test_file):
        test_dir = os.path.dirname(os.path.abspath(test_file))
        screenshot_dir = os.path.join(
            test_dir,
            "screenshots"
        )
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        os.makedirs(screenshot_dir, exist_ok=True)
        file_path = os.path.join(screenshot_dir, f"{file_name}_{timestamp}.png")
        driver.save_screenshot(file_path)
        return file_path
