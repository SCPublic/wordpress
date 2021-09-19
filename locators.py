class Locators:
    # Login page locators
    username_field = "usernameOrEmail"
    password_field = "password"

    # Profile page locators
    first_name = "first_name"
    last_name = "last_name"
    display_name = "display_name"
    description = "description"
    save_button_xpath = "//*[contains(text(), 'Save profile details')]"
    save_button_disabled = ".form-button[disabled]"
