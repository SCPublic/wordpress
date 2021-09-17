from selenium import webdriver
from login_page import LoginPage


def test_wordpress_login():
    driver = webdriver.Firefox()
    login = LoginPage(driver)
    login.login()
