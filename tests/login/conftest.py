import pytest

from framework.login_page import LoginPage


@pytest.fixture(scope='function')
def user_login_fixture(page_manager):
    login_page = page_manager.create_page(LoginPage)
    yield login_page
