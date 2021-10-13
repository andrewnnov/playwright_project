from pom.home_page_elements import HomePage
import pytest
from playwright.sync_api import Playwright, sync_playwright

@pytest.mark.integration
def test_about_us_section_verbiage(playwright: Playwright) -> None:

    # Assess - Given
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()

    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    assert page.is_visible(HomePage.celebrating_beauty_header)

    assert page.is_visible(HomePage.celebrating_beauty_body)

    context.close()
    browser.close()


@pytest.mark.xfail(reason='faketext should not be visible')
@pytest.mark.regression
def test_about_us_section_verbiage_2(playwright: Playwright) -> None:

    # Assess - Given
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()

    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    assert page.is_visible("text=faketext")
    assert page.is_visible(HomePage.celebrating_beauty_header)

    assert page.is_visible(HomePage.celebrating_beauty_body)

    context.close()
    browser.close()