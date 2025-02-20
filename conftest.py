from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.close()