import time
import pytest
from pom.home_page_elements import HomePage


@pytest.mark.parametrize("email", ["test@testmail.com",
                                             pytest.param("fakemail", marks=pytest.mark.xfail),
                                             pytest.param("test@testmai", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password", ["test123",
                                             pytest.param("test234", marks=pytest.mark.xfail),
                                             pytest.param("test123", marks=pytest.mark.xfail)])
def test_user_can_login(page, email, password):

    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

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

    page.fill("[data-testid=\"siteMembers.container\"] input[type=\"email\"]", email)

    page.click("input[type=\"password\"]")

    page.fill("input[type=\"password\"]", password)

    page.click("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]")

    page.wait_for_timeout(3000)

    assert not page.is_visible("text=Log In")



