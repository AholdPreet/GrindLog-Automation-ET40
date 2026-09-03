def test_contexts(driver):

    print("Current Context:", driver.current_context)

    print("Available Contexts:")

    for context in driver.contexts:
        print(context)