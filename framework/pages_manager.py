class PagesManager:

    def __init__(self, driver):
        self.driver = driver
        #self.login_page = LoginPage(driver)

    def create_page(self, page_class):
        return page_class(self.driver)
