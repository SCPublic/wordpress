from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from locators import Locators


class ProfilePage(object):
    def __init__(self, driver):
        self.driver = driver

    def change_first_name(self):
        first_name = self.driver.find_element_by_id(Locators.first_name)
        first_name.send_keys("Walt")

    def change_last_name(self):
        last_name = self.driver.find_element_by_id(Locators.last_name)
        last_name.send_keys("Harris")

    def change_description(self):
        description = self.driver.find_element_by_id(Locators.description)
        description.send_keys("Test Description")

    def save_profile_changes(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.save_button_xpath))
        )
        self.driver.find_element_by_xpath(Locators.save_button_xpath).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, Locators.save_button_disabled)
            )
        )
