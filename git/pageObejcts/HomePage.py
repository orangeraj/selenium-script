from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href='/angularpractice/shop']")
    name = (By.NAME,"name")
    email = (By.NAME,'email')
    password = (By.CSS_SELECTOR,"input[placeholder='Password']")
    id = (By.ID,"exampleCheck1")
    submit = (By.CSS_SELECTOR,"input[type='submit']")
    gender = (By.CSS_SELECTOR,"select[id='exampleFormControlSelect1']")
    text = (By.XPATH,"//strong[contains(text(),'Success!')]")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def getname(self):
        return  self.driver.find_element(*HomePage.name)

    def getemail(self):
        return  self.driver.find_element(*HomePage.email)

    def getpassword(self):
        return  self.driver.find_element(*HomePage.password)

    def getid(self):
        return  self.driver.find_element(*HomePage.id)

    def getsubmit(self):
        return  self.driver.find_element(*HomePage.submit)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)

    def gettext(self):
        return self.driver.find_element(*HomePage.text)