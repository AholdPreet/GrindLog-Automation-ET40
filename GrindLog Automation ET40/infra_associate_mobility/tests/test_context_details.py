def test_context_details(driver):

    print("Current Context:", driver.current_context)

    contexts = driver.contexts

    for c in contexts:
        print("Context =", c)

    print("\nPage Source:\n")
    print(driver.page_source[:5000])