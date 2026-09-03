def test_switch_webview(driver):

    print("Before:", driver.current_context)

    driver.switch_to.context("WEBVIEW_chrome")

    print("After:", driver.current_context)

    print("Title:", driver.title)

    print("URL:", driver.current_url)