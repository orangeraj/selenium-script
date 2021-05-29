from Utilities.BaseClass import BaseClass
from pageObejcts.CheckoutPage import CheckoutPage
from pageObejcts.ConfirmPage import ConfirmPage
from pageObejcts.HomePage import HomePage

class TestOne(BaseClass):

    def test_e2e(self):

        homePage = HomePage(self.driver)
        checkoutPage = CheckoutPage(self.driver)
        confirmpage = ConfirmPage(self.driver)

        #self.driver.find_element_by_css_selector("a[href='/angularpractice/shop']").click()
        homePage.shopItems().click()
        #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        products = checkoutPage.getcheckoutItems()

        for product in products:
            product_name = product.find_element_by_xpath("div/h4/a").text
            if product_name == "iphone X":
                product.find_element_by_xpath("div[2]/button").click()
                break
        #self.driver.find_element_by_css_selector("a[class*='btn btn-primary']").click()
        checkoutPage.getcheckoutButton().click()
        checkout_name = self.driver.find_element_by_css_selector("div h4 a[href='#']").text


        assert product_name == checkout_name
        #self.driver.find_element_by_css_selector("button[class*='btn btn-success']").click()
        checkoutPage.getcheckoutButton2().click()
        # driver.find_element_by_id("country").send_keys("India")

        # wait = WebDriverWait(driver, 7)
        # wait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT, "India"))
        # driver.find_element_by_link_text("India").click()
        #self.driver.find_element_by_css_selector("div[class*='checkbox checkbox-primary']").click()
        confirmpage.getcheckbox().click()
        confirmpage.getpurchasebtn().click()
        assert confirmpage.gettext() == "Success!"
        print(confirmpage.gettext())
        #self.driver.find_element_by_css_selector("input[class*='btn btn-success btn-lg']").click()
        #self.driver.find_element_by_xpath("//strong[contains(text(),'Success!')]").text == "Success!"

