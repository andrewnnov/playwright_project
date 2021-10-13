import time

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:

    # Assess - Given
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()

    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    # Act - When/And
    # Click button:has-text("Log In")

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

    page.fill("input[type=\"password\"]", "test123")

    page.click("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]")

    page.click("[aria-label=\"test account menu\"]")

    # Assert - Then
    assert page.is_visible("text=My Order")
    # Click text=My Orders
    # with page.expect_navigation(url="https://symonstorozhenko.wixsite.com/website-1/account/my-orders"):
    # with page.expect_navigation():
    #     page.click("text=My Orders")
    # ---------------------
    # context.close()
    # browser.close()


with sync_playwright() as playwright:
    run(playwright)

