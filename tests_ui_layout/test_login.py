import time
import pytest

from playwright.sync_api import Playwright, sync_playwright

@pytest.mark.smoke
def test_login(set_up) -> None:

    # Assess - Given
    page = set_up

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






