import pytest
from faker import Faker
from playwright.sync_api import Page
from page.base_page import BasePage


@pytest.fixture
def base_page(page: Page):
    return BasePage(page)

@pytest.fixture
def user_data():
    fake = Faker()
    email = fake.email()
    full_name = fake.name()
    address = fake.address()
    yield {
        "email": email,
        "fullname": full_name,
        "address": address
    }

