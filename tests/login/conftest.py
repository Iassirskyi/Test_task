import pytest

from framework.login_page import LoginPage
from framework.sidebar_page import SideBarPage


@pytest.fixture(scope='function')
def user_login_fixture(page_manager):
    login_page = page_manager.create_page(LoginPage)
    yield login_page


@pytest.fixture(scope='function')
def sidebar_fixture(page_manager):
    sidebar_page = page_manager.create_page(SideBarPage)
    yield sidebar_page

