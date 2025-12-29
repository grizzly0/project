from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://saby.ru/"
        self.browser.maximize_window()

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),message= f"can`t find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until( EC.presence_of_all_elements_located(locator), message=f"can't find elements by locator {locator}")

    def go_to_site(self):
        self.browser.get(self.url)

    def move_element(self, tutorial):
        actions = ActionChains(self.browser)
        actions.move_to_element(tutorial).perform()

