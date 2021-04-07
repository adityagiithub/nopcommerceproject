import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")
    elif browser=='Edge':
        driver = webdriver.Edge(executable_path="C:\drivers\edgedriver_win64\msedgedriver.exe")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# for generating html report the below two methods gives the changes to project name etc
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

# # pytest -s -v -n=3 --html=Reports\report.html Testcases/test_login.py --browser chrome