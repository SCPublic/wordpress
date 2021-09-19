from selenium import webdriver
from login_page import LoginPage
from profile_page import ProfilePage


def test_wordpress_login():
    """Test that login and credentials work."""
    driver = webdriver.Firefox()
    login = LoginPage(driver)
    login.login()
    driver.quit()


def test_save_profile_changes():
    """Test that profile details can be changed and saved."""
    driver = webdriver.Firefox()
    login = LoginPage(driver)
    login.login()
    profile_page = ProfilePage(driver)
    profile_page.change_first_name()
    profile_page.change_last_name()
    profile_page.change_description()
    profile_page.save_profile_changes()
    driver.quit()
