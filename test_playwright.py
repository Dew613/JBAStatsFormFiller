from playwright.sync_api import sync_playwright

def test_browser():
    with sync_playwright() as p:
        # Launch the broswer with headless to make it visible
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        # Test browser by visiting example site
        page.goto("https://example.com")
        print("Opened page with title: ", page.title())

        # Pause for 2 seconds
        page.wait_for_timeout(2000)

        # Close broswer
        browser.close()


if __name__ == "__main__":
    test_browser()