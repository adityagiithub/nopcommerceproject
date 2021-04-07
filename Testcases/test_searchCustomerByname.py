import time
import pytest
from Pageobjects.loginpage import Loginpage
from Pageobjects.addcustomer import addcustomer
from Pageobjects.searchCustomer import SearchCustomer
from Utilities.readproperties import Readconfig
from Utilities.custumloger import  LogGen

class Test_SearchCustomerByName_005:
    baseURL = Readconfig.getApplicationURL()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    logger = LogGen.loggen()  # Logger
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        # self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # self.logger.info("************* Login succesful **********")

        # self.logger.info("******* Starting Search Customer By Name **********")

        self.addcust = addcustomer(self.driver)
        self.addcust.clickoncustomer()
        self.addcust.clickcustomeritem()
        time.sleep(2)

        # self.logger.info("************* searching customer by Name **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert True==status
        # self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")
