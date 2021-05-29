from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    checkbox = (By.CSS_SELECTOR, "div[class*='checkbox checkbox-primary']")
    purchasebtn = (By.CSS_SELECTOR, "input[class*='btn btn-success btn-lg']")
    successtext = (By.XPATH, "//strong[contains(text(),'Success!')]")

    def getcheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getpurchasebtn(self):
        return self.driver.find_element(*ConfirmPage.purchasebtn)

    def gettext(self):
        return self.driver.find_element(*ConfirmPage.successtext)