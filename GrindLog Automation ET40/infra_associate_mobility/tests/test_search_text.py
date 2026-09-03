def test_search_text(driver):

    source = driver.page_source

    words = [
        "Trim Cut Log",
        "Tube Grind",
        "Trim Grind",
        "Grind Notes",
        "Exit"
    ]

    for word in words:
        print(f"{word} = {word in source}")