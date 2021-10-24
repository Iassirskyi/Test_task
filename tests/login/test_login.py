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



@pytest.mark.parametrize('user_login, user_password', [
    ('abra_cadabrd', 'abra_cadabrd_password'),
    ('tester@gmail.com', 'tester_test')
])
def test_invalid_login_password(user_login_fixture, user_login, user_password):
    user_login_fixture.enter_login(user_login)
    user_login_fixture.enter_password(user_password)
    user_login_fixture.tap_next()
    user_login_fixture.wait()
    assert 'Log In' == user_login_fixture.get_next_text().text


@pytest.mark.parametrize('user_login, user_password, expected_result', [
    ('qa.ajax.app.automation@gmail.com', 'qa_automation_password', 'Add')
])
def test_valid_login_password(user_login_fixture, user_login, user_password, expected_result):
    user_login_fixture.enter_login(user_login)
    user_login_fixture.enter_password(user_password)
    user_login_fixture.wait()
    user_login_fixture.tap_next()
    user_login_fixture.wait()
    user_login_fixture.tap_cancel_button()
    user_login_fixture.wait()
    assert expected_result in user_login_fixture.valid_login().text
