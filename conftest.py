from playwright.sync_api import Page
import pytest
from page.base_page import BasePage


@pytest.fixture
def base_page(page: Page):
    return BasePage(page)
