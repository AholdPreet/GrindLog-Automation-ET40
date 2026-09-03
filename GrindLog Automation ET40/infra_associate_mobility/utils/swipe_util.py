class SwipeUtil:

    @staticmethod
    def swipe_up(driver, duration=1000):
        size = driver.get_window_size()
        driver.swipe(
            size['width'] // 2,
            int(size['height'] * 0.8),
            size['width'] // 2,
            int(size['height'] * 0.2),
            duration
        )

    @staticmethod
    def swipe_down(driver, duration=1000):
        size = driver.get_window_size()
        driver.swipe(
            size['width'] // 2,
            int(size['height'] * 0.2),
            size['width'] // 2,
            int(size['height'] * 0.8),
            duration
        )

    @staticmethod
    def swipe_left(driver, duration=1000):
        size = driver.get_window_size()
        driver.swipe(
            int(size['width'] * 0.8),
            size['height'] // 2,
            int(size['width'] * 0.2),
            size['height'] // 2,
            duration
        )

    @staticmethod
    def swipe_right(driver, duration=1000):
        size = driver.get_window_size()
        driver.swipe(
            int(size['width'] * 0.2),
            size['height'] // 2,
            int(size['width'] * 0.8),
            size['height'] // 2,
            duration
        )
