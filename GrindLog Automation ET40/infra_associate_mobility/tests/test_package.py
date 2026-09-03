def test_package(driver):

    print("Package:", driver.current_package)

    try:
        print("Activity:", driver.current_activity)
    except Exception as e:
        print(e)