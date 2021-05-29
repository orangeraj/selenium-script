import pytest

from Utilities.BaseClass import BaseClass
from pageObejcts.HomePage import HomePage
from selenium.webdriver.support.select import Select


class TestSubmit(BaseClass):

    def test_submitpage(self,getData):

        #driver = webdriver.Chrome(executable_path=r"C:\Users\mhatr\Downloads\chromedriver_win32\chromedriver.exe")
        #driver.get("https://rahulshettyacademy.com/angularpractice/")
        #driver.maximize_window()

        homepage = HomePage(self.driver)

        homepage.getname().send_keys(getData["name"])
        homepage.getemail().send_keys(getData["email"])
        homepage.getpassword().send_keys(getData["pswd"])
        homepage.getid().click()

        sel = Select(homepage.getgender())
        sel.select_by_visible_text("Male")

        #driver.find_element_by_css_selector("//input[@type='date']").send_keys("23/08/1993")
        homepage.getsubmit().click()

        success_text = homepage.gettext()
        self.driver.refresh()

    #@pytest.fixture(params=[("rajas", "rajas@abc.com", "xyz" ), ("harshit", "harsh@abc.com", "abc")])
    @pytest.fixture(params=BaseClass.getdata("03"))

    def getData(self,request):
        return request.param

