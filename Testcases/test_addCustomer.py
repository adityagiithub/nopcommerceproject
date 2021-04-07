import pytest
from selenium import webdriver
from Pageobjects.loginpage import Loginpage
from Pageobjects.addcustomer import addcustomer
from Utilities.readproperties import Readconfig
import string
import random
# from Utilities.custumloger import LogGen

class Test_003_AddCustomer:
    url =Readconfig.getApplicationURL()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    # logger=LogGen.loggen()
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addcustomer(self,setup):
        print("test addcustomer has started")
        self.driver=setup
        self.driver.get(self.url)
        print("website launched")
        self.driver.maximize_window()
        act_title=self.driver.title
        print(act_title)


        self.lp=Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.addcust=addcustomer(self.driver)
        self.addcust.clickoncustomer()
        self.addcust.clickcustomeritem()
        self.addcust.clickonaddnew()
        print("providing customer informaton")
        self.email= random_generator() + "@gmail.com"
        self.addcust.setemail(self.email)
        self.addcust.setpassword("test123")
        self.addcust.setfirstname("adit")
        self.addcust.setlastname("dude")
        self.addcust.setgender("female")
        self.addcust.setdob("12/3/2019")
        self.addcust.setcompany("nodiscrimination")
        self.addcust.clicktaxexpmnt()
        # self.addcust.setcustomeroles("Vendors")
        self.addcust.select_managerofvendor("vendor 2")
        self.addcust.clickcbxactive_xpath()
        self.addcust.write_txtcomment("hey this is workign=ng fine")
        self.addcust.clickOnSave()
        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            print("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            print("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        print("******* Ending Add customer test **********")


def random_generator(size=9, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

#pytest -v -s Testcases/test_addCustomer.py --browser chrome
