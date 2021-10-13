import time
import pytest

from playwright.sync_api import Playwright, sync_playwright


@pytest.mark.smoke
def test_logged_user_can_view_my_orders_menu(login_set_up) -> None:

    # Assess - Given
    page = login_set_up

    # Act - When/And


    # Assert - Then
    #assert page.is_visible("text=My Order")






