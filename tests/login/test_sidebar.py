
def test_menu(sidebar_fixture):
    sidebar_fixture.tap_menu()
    sidebar_fixture.wait()
    assert 'Menu' == sidebar_fixture.get_menu_text().text

def test_add_hub(sidebar_fixture):
    sidebar_fixture.tap_add_hub()
    sidebar_fixture.wait()
    assert 'Add' in sidebar_fixture.valid_add_hub_text().text

def test_app_settings(sidebar_fixture):
    sidebar_fixture.exit_from_add_hub_session()
    sidebar_fixture.wait()
    sidebar_fixture.tap_menu()
    sidebar_fixture.wait()
    sidebar_fixture.tap_app_settings()
    sidebar_fixture.wait()
    assert 'Back' == sidebar_fixture.get_back_button_text().text

def test_help(sidebar_fixture):
    sidebar_fixture.back_button()
    sidebar_fixture.wait()
    sidebar_fixture.tap_menu()
    sidebar_fixture.wait()
    sidebar_fixture.tap_help()
    sidebar_fixture.wait()
    assert 'Back' == sidebar_fixture.get_back_button_text().text

def test_report_button(sidebar_fixture):
    sidebar_fixture.back_button()
    sidebar_fixture.wait()
    sidebar_fixture.tap_menu()
    sidebar_fixture.wait()
    sidebar_fixture.tap_report()
    sidebar_fixture.wait()
    assert 'Back' == sidebar_fixture.get_back_button_text().text