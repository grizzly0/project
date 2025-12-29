import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()