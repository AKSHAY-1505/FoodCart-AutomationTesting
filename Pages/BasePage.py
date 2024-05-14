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

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def do_apply_leave(self):
        leave_type_dropdown = self.getElement(By.XPATH, "//div[text()='-- Select --']")
        self.clickElement(leave_type_dropdown)

        leave_type_option = self.getElement(By.XPATH, '//div[@role = "listbox"]//span')
        self.clickElement(leave_type_option)

        from_date_picker = self.getElement(By.XPATH, "//label[contains(text(),'From Date')]/../following-sibling::div")
        self.clickElement(from_date_picker)

        from_date = self.getElement(By.XPATH, "//div[@class='oxd-calendar-date' and text()='27']")
        self.clickElement(from_date)

        time.sleep(2)

        to_date_picker = self.getElement(By.XPATH, "//label[contains(text(),'To Date')]/../following-sibling::div")
        self.clickElement(to_date_picker)

        to_date = self.getElement(By.XPATH, "//div[@class='oxd-calendar-date' and text()='29']")
        self.clickElement(to_date)

        partial_days_dropdown = self.getElement(By.XPATH,
                                                "//label[contains(text(),'Partial Days')]/../following-sibling::div")
        self.clickElement(partial_days_dropdown)

        partial_days_option = self.getElement(By.XPATH,
                                              "//label[text() = 'Partial Days']/../following-sibling::div//span[text() = 'End Day Only']")
        self.clickElement(partial_days_option)

        end_day_dropdown = self.getElement(By.XPATH, "//label[text() = 'End Day']/../following-sibling::div")
        self.clickElement(end_day_dropdown)

        end_day_option = self.getElement(By.XPATH, "//span[contains(normalize-space(),'Half Day - Morning')]")
        self.clickElement(end_day_option)

        comments = self.getElement(By.XPATH, "//label[contains(text(),'Comments')]/../following-sibling::div/textarea")
        self.sendKeys(comments, "Test")

        apply_button = self.getElement(By.XPATH, "//button[contains(normalize-space(),'Apply')]")
        self.clickElement(apply_button)

        my_leave = self.getElement(By.XPATH, "//a[text()='My Leave']")
        self.clickElement(my_leave)

    def view_leave_details(self):
        three_dot_button = self.getElement(By.XPATH,
                                           "//div[@class='oxd-table-body']/div//div[text()='Test']/../following-sibling ::div//button[text()=' Cancel ']/following-sibling::li/button")
        self.clickElement(three_dot_button)

        view_details_option = self.getElement(By.XPATH,
                                              "//div[@class='oxd-table-body']/div//div[text()='Test']/../following-sibling ::div//button[text()=' Cancel ']/following-sibling::li/ul//p[text()='View Leave Details']")
        self.clickElement(view_details_option)




