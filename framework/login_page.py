from .page import Page
import time


class LoginPage(Page):

    LOGIN = 'com.ajaxsystems:id/login'
    PASSWORD = 'com.ajaxsystems:id/password'
    NEXT_PAGE = 'com.ajaxsystems:id/next'
    LOGIN_ACCESS = 'com.ajaxsystems:id/addFirstHub'
    CANCEL_BUTTON = 'com.ajaxsystems:id/cancel_button'


    def wait(self):
        return time.sleep(5)
    
    def tap_login(self):
        self.click_element(self.LOGIN)
    
    def get_login_text(self):
        return self.find_element(self.LOGIN)
    
    def tap_password(self):
        self.click_element(self.PASSWORD)
    
    def get_password_text(self):
        return self.find_element(self.PASSWORD)

    def enter_login(self, user_login):
        self.input(self.LOGIN, text=user_login)
    
    def enter_password(self, user_password):
        self.input(self.PASSWORD, text=user_password)
    
    def tap_next(self):
        self.click_element(self.NEXT_PAGE)
    
    def get_next_text(self):
        return self.find_element(self.NEXT_PAGE)
    
    def tap_cancel_button(self):
        self.click_element(self.CANCEL_BUTTON)

    def valid_login(self):
        return self.find_element(self.LOGIN_ACCESS)
