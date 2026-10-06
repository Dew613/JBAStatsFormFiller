import os
import yaml
import time
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
        #page.wait_for_timeout(2000)

        (
        page.locator('div[data-automation-id="questionItem"]')
        .filter(has_text="Department")
        .get_by_text("JBA")
        .click()
        )


        page.get_by_text("Workshop/Program").click()

        # Click the Next button
        page.get_by_role("button", name="Next").click()

        # 1. Click the dropdown field to open the menu
        page.get_by_label("Workshop/Program Location").click()

        # 2. Click "Central" from the revealed options list
        page.get_by_role("option", name="Central").click()


        
        #================================

        # Date picker is not immediately responsive, hence the need for the wait_for_timeout()
        # If you are on the previous field, pressing Tab moves focus directly to the date input
        page.keyboard.press("Tab")
        page.wait_for_timeout(1000)
        page.keyboard.type("6/15/2026")
        page.wait_for_timeout(1000)
        page.keyboard.press("Tab")

        #================================

        # Fill out Program Title
        page.get_by_label("Workshop/Program Title").fill("Automated test for workshop title")

        #Fill out Attendance
        page.get_by_label("Attendance").fill("13")

        # 1. Click the dropdown field to open the menu
        page.get_by_label("Duration (minutes only)").click()

        # 2. Click the time from the revealed options list
        page.get_by_role("option", name="90").click()

        # 1. Click the dropdown field to open the menu
        page.get_by_label("Platform").click()

        # 2. Click "In-Person" from the revealed options list
        page.get_by_role("option", name="In-Person").click()
        
        # Fill out LAMPS number
        page.get_by_label("LAMPS").fill("12345-Aug")

        # Click Submit
        page.get_by_role("button", name="Submit").click()

        # Check if submission went through
        page.wait_for_timeout(1000)

        # Close browser
        browser.close()



if __name__ == "__main__":
    url = get_url()
    if (not url):
        print("Error: config.yaml not found or missing form_url")
        exit()
    
    run_form_filler(url)