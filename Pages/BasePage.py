from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""This is the Parent of all Pages"""

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def click_on(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def send_to(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element(self, by_locator):
        element =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    def click_when_clickable(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    def click_using_js(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].click();", element)







