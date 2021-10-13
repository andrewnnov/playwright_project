import os

import pytest
from playwright.sync_api import Playwright, sync_playwright




@pytest.fixture(scope="session")
def set_up(browser):
    # Assess - Given
    # browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # # Open new page
    page = context.new_page()
    # page.goto("")
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    yield page
    page.close()


@pytest.fixture(scope="session")
def login_set_up(set_up):

    page = set_up

    login_issue = True
    while login_issue:
        if not page.is_visible("[data-testid=\"signUp.switchToSignUp\"]"):
            page.click("button:has-text(\"Log In\")")
        else:
            login_issue = False
        page.wait_for_timeout(1000)
    # page.wait_for_selector("button:has-text(\"Log In\")")
    # page.click("button:has-text(\"Log In\")")
    # page.click("text=Log In")
    # page.click("'Log In'")

    page.click("[data-testid=\"signUp.switchToSignUp\"]")

    page.click("[data-testid=\"switchToEmailLink\"] [data-testid=\"buttonElement\"]")

    page.click("[data-testid=\"siteMembers.container\"] input[type=\"email\"]")

    page.fill("[data-testid=\"siteMembers.container\"] input[type=\"email\"]", "test@testmail.com")

    page.click("input[type=\"password\"]")

    page.fill("input[type=\"password\"]", os.environ['PASSWORD'])

    page.click("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]")

    yield page




@pytest.fixture()
def go_to_new_collection_page(page):
    # Assess - Given
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # # Open new page
    # page = context.new_page()

    page.goto("/new-collection")
    page.set_default_timeout(3000)

    yield page