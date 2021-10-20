class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator:str):
        return self.driver.find_element_by_id(locator)
    
    def find_element_by_class(self, locator:str):
        return self.driver.find_element_by_class_name(locator)


    def click_element(self, locator:str):
        element = self.find_element(locator)
        element.click()

    def input(self, locator:str, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
