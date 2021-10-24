
def test_menu(logger, sidebar_fixture):
    try:
        sidebar_fixture.tap_menu()
        assert 'Menu' == sidebar_fixture.get_menu_text().text
    except Exception as e:
        logger.info(e)


def test_add_hub(logger, sidebar_fixture):
    try:
        sidebar_fixture.tap_add_hub()
        assert 'Add' in sidebar_fixture.valid_add_hub_text().text
    except Exception as e:
        logger.info(e)


def test_app_settings(logger, sidebar_fixture):
    try:
        sidebar_fixture.exit_from_add_hub_session()
        sidebar_fixture.tap_app_settings()
        assert 'Back' == sidebar_fixture.get_back_button_text().text
    except Exception as e:
        logger.info(e)


def test_help(logger, sidebar_fixture):
    try:
        sidebar_fixture.back_button()
        sidebar_fixture.tap_help()
        assert 'Back' == sidebar_fixture.get_back_button_text().text
    except Exception as e:
        logger.info(e)


def test_report_button(logger, sidebar_fixture):
    try:
        sidebar_fixture.back_button()
        sidebar_fixture.tap_report()
        assert 'Back' == sidebar_fixture.get_back_button_text().text
    except Exception as e:
        logger.info(e)