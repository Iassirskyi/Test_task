from .login_page import LoginPage
import time


class SideBarPage(LoginPage):

    ADD_HUB = 'com.ajaxsystems:id/addHub'
    APP_SETTINGS = 'com.ajaxsystems:id/settings'
    HELP = 'com.ajaxsystems:id/help'
    REPORT = 'com.ajaxsystems:id/logs'
    MENU = 'com.ajaxsystems:id/menuDrawer'
    MENU_TEXT = 'com.ajaxsystems:id/menuTitle'
    BACK_BUTTON = 'com.ajaxsystems:id/back'
    ADD_MANUALLY_BUTTON = 'com.ajaxsystems:id/next'
    CANCEL_BUTTON = 'com.ajaxsystems:id/cancel'


    def wait(self):
        return time.sleep(5)
    
    def back_button(self):
        self.click_element(self.BACK_BUTTON)
    
    def get_back_button_text(self):
        return self.find_element(self.BACK_BUTTON)

    def tap_menu(self):
        self.click_element(self.MENU)
    
    def get_menu_text(self):
        return self.find_element(self.MENU_TEXT)
    
    def tap_add_hub(self):
        self.click_element(self.ADD_HUB)
    
    def valid_add_hub_text(self):
        return self.find_element(self.ADD_MANUALLY_BUTTON)
    
    def exit_from_add_hub_session(self):
        self.click_element(self.ADD_MANUALLY_BUTTON)
        self.wait()
        self.click_element(self.CANCEL_BUTTON)

    
    def tap_app_settings(self):
        self.click_element(self.APP_SETTINGS)
    
    def get_app_settings_text(self):
        return self.find_element(self.APP_SETTINGS)

    def tap_help(self):
        self.click_element(self.HELP)
    
    def tap_report(self):
        self.click_element(self.REPORT)



