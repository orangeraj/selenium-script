import datetime

import pytest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="select browser"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=r"C:\Users\mhatr\Downloads\chromedriver_win32\chromedriver.exe")
    elif browser_name == "firefox":
        pass
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


    @pytest.mark.hookwrapper
    def pytest_runtest_makereport(item, call):

        timestamp = datetime.now().strftime('%H-%M-%S')

        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])
        if report.when == 'call':

            feature_request = item.funcargs['request']

            driver = feature_request.getfuncargvalue('browser')
            driver.save_screenshot('D:/report/scr' + timestamp + '.png')

            extra.append(pytest_html.extras.image('D:/report/scr' + timestamp + '.png'))

            # always add url to report
            extra.append(pytest_html.extras.url(
                'file:///C:/Users/mhatr/PycharmProjects/SeleniumProject/pytestsDemo/pytest_html_report.html'))
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                # only add additional html on failure
                extra.append(pytest_html.extras.image('D:/report/scr.png'))
                extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
            report.extra = extra