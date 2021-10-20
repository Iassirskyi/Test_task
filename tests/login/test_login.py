import pytest

from framework.login_page import LoginPage


@pytest.mark.parametrize('user_login, user_password, expected_result', [
    ('t.tester@gmail.com', 'test_password', 'Back'),
    ('qa.ajax.app.automation@gmail.com', 'qa_automation_password', 'Back'),
])
def test_user_login(user_login_fixture, user_login, user_password, expected_result):
    page = user_login_fixture.create_page(LoginPage)
    page.driver.implicitly_wait(5)
    page.tap_login()
    page.driver.implicitly_wait(5)
    page.enter_login(user_login)
    page.tap_password()
    page.enter_password(user_password)
    page.driver.implicitly_wait(5)
    page.tap_next()
    page.driver.implicitly_wait(5)
    assert expected_result in page.find_element_by_class('android.widget.TextView').text


