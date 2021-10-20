from .page import Page


class LoginPage(Page):
    # LOGIN = 'qa.ajax.app.automation@gmail.com'
    # PASSWORD = 'qa_automation_password'
    LOGIN = 'com.ajaxsystems:id/login'
    PASSWORD = 'com.ajaxsystems:id/password'
    NEXT_PAGE = 'com.ajaxsystems:id/next'

    def tap_login(self):
        self.click_element(self.LOGIN)
    
    def tap_password(self):
        self.click_element(self.PASSWORD)

    def enter_login(self, user_login):
        self.input(self.LOGIN, text=user_login)
    
    def enter_password(self, user_password):
        self.input(self.PASSWORD, text=user_password)
    
    def tap_next(self):
        self.click_element(self.NEXT_PAGE)

