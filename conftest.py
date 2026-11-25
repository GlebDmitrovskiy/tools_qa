import pytest
from faker import Faker
from playwright.sync_api import Page
from page.base_page import BasePage


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "args": ["--start-maximized"],
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "no_viewport": True,
    }


@pytest.fixture
def base_page(page: Page):
    return BasePage(page)


@pytest.fixture
def user_data():
    fake = Faker()
    email = fake.email()
    full_name = fake.name()
    address = fake.address().replace("\n", " ")
    yield {
        "email": email,
        "fullname": full_name,
        "address": address
    }
