import pytest


def test_valid_login_page(user_login_fixture):
    user_login_fixture.tap_login()
    user_login_fixture.wait()
    assert 'Email' in user_login_fixture.get_login_text().text


@pytest.mark.parametrize('user_login, expected_result', [
    ('user.login.test', 'user.login.test'),
    ('User.login.test2', 'User.login.test2')
    ])
def test_input_login(user_login_fixture, user_login, expected_result):
    user_login_fixture.enter_login(user_login)
    user_login_fixture.wait()
    assert expected_result == user_login_fixture.get_login_text().text


@pytest.mark.parametrize('user_password, expected_result', [
    ('user_password_test', 'user_password_test'),
    ('user_password_test2', 'user_password_test2')
    ])
def test_input_password(user_login_fixture, user_password, expected_result):
    user_login_fixture.enter_password(user_password)
    user_login_fixture.wait()
    assert len(expected_result) == len(user_login_fixture.get_password_text().text)




# @pytest.mark.parametrize('user_login, user_password, expected_result', [
#     ('t.tester@gmail.com', 'test_password', 'Back'),
#     ('qa.ajax.app.automation@gmail.com', 'qa_automation_password', 'Back'),
# ])
# def test_user_login(user_login_fixture, user_login, user_password, expected_result):
#     page = user_login_fixture.create_page(LoginPage)
#     page.wait()
#     page.tap_login()
#     page.driver.implicitly_wait(5)
#     page.enter_login(user_login)
#     page.tap_password()
#     page.enter_password(user_password)
#     page.driver.implicitly_wait(5)
#     page.tap_next()
#     page.driver.implicitly_wait(5)
#     assert expected_result in page.find_element_by_class('android.widget.TextView').text


