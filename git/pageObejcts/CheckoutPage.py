from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn btn-primary']")
    checkoutButton2 = (By.CSS_SELECTOR, "button[class*='btn btn-success']")

    def getcheckoutItems(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getcheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def getcheckoutButton2(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton2)