import time

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:

    # Assess - Given
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://symonstorozhenko.wixsite.com/website-1
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    # Act - When/And
    # Click button:has-text("Log In")
    # time.sleep(5)
    page.click("button:has-text(\"Log In\")", timeout=7000)
    # Click [data-testid="signUp.switchToSignUp"]
    # time.sleep(5)
    page.click("[data-testid=\"signUp.switchToSignUp\"]")
    # Click [data-testid="switchToEmailLink"] [data-testid="buttonElement"]
    page.click("[data-testid=\"switchToEmailLink\"] [data-testid=\"buttonElement\"]")
    # Click [data-testid="siteMembers.container"] input[type="email"]
    page.click("[data-testid=\"siteMembers.container\"] input[type=\"email\"]")
    # Fill [data-testid="siteMembers.container"] input[type="email"]
    page.fill("[data-testid=\"siteMembers.container\"] input[type=\"email\"]", "test@testmail.com")
    # Click input[type="password"]
    page.click("input[type=\"password\"]")
    # Fill input[type="password"]
    page.fill("input[type=\"password\"]", "test123")
    # Click [data-testid="submit"] [data-testid="buttonElement"]
    page.click("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]")
    # Click [aria-label="test account menu"]
    page.click("[aria-label=\"test account menu\"]")

    # Assert - Then
    assert page.is_visible("text=My Order")
    # Click text=My Orders
    # with page.expect_navigation(url="https://symonstorozhenko.wixsite.com/website-1/account/my-orders"):
    # with page.expect_navigation():
    #     page.click("text=My Orders")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

