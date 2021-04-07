import time
import pytest
from Pageobjects.loginpage import Loginpage
from Pageobjects.addcustomer import addcustomer
from Pageobjects.searchCustomer import SearchCustomer
from Utilities.readproperties import Readconfig
from Utilities.custumloger import  LogGen

class Test_SearchCustomerByEmail_004:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()  # Logger
    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = addcustomer(self.driver)
        self.addcust.clickoncustomer()
        self.addcust.clickcustomeritem()

        self.logger.info("************* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByEmail_004 Finished  *********** ")

