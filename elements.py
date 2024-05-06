from selenium.webdriver.common.by import By

class RegisterLocators():
    shadowHost = (By.CSS_SELECTOR, '.remoteComponent')
    name_field = (By.CSS_SELECTOR, 'div[data-wi="user-name"] input[specialtoken="k-text-field-primary"]')
    mail_field = (By.CSS_SELECTOR, '#username')
    pass_field = (By.CSS_SELECTOR, '#new-password')
    referral_field = (By.CSS_SELECTOR, 'div[data-wi="referral"] input[specialtoken="k-text-field-primary"]')
    continue_btn = (By.CSS_SELECTOR, 'button[type="submit"]')
    check_box = (By.CSS_SELECTOR, 'input[type="checkbox"]')