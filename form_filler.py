import os
import yaml
from playwright.sync_api import sync_playwright


def get_url():
    if os.path.exists("config.yaml"):
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)
            form_url = config.get("form_url")
            return form_url

    return None
    

def run_form_filler(url):
    with sync_playwright() as p:
        # Launch the browser without headless to make it visible
        browser = p.chromium.launch(headless = False)
        page = browser.new_page()

        # Go to Form Url
        page.goto(url)
        page.wait_for_timeout(2000)

        # Close browser
        browser.close()



if __name__ == "__main__":
    url = get_url()
    if (not url):
        print("Error: config.yaml not found or missing form_url")
        exit()
    
    run_form_filler(url)