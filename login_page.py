import os
from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class LoginPage(object):
    load_dotenv()
    username = os.environ.get("secretUser")
    password = os.environ.get("secretKey")

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.get("https://www.wordpress.com/me")
        username_field = self.driver.find_element_by_id("usernameOrEmail")
        username_field.send_keys(self.username)
        username_field.send_keys(Keys.RETURN)
        password_field = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, "first_name"))
        )


