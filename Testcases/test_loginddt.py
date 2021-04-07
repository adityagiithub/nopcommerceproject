import pytest
from selenium import webdriver
from Pageobjects.loginpage import Loginpage
from Utilities.readproperties import Readconfig
from Utilities.custumloger import LogGen
from Utilities import xlutilities
class Test_002_DDT_login:
    url =Readconfig.getApplicationURL()
    path=".//Testdata//logindata.xlsx"


    @pytest.mark.sanity
    def test_login_ddt(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        self.lp=Loginpage(self.driver)
        self.rows=xlutilities.getRowCount(self.path,'Sheet1')
        print('no of rows ',self.rows)
        list_status=[]
        for r in range(2,self.rows+1):
          self.Username=xlutilities.readData(self.path,'Sheet1',r,1)
          self.Password=xlutilities.readData(self.path,'Sheet1',r,2)
          self.expected=xlutilities.readData(self.path,'Sheet1',r,3)

          self.lp.setUsername(self.Username)
          self.lp.setPassword(self.Password)
          self.lp.clickLogin()
          act_title=self.driver.title
          # print(act_title)
          exp_title="Dashboard / nopCommerce administration"
          if act_title==exp_title:

            if self.expected=='pass':
                self.lp.clickLogout()
                list_status.append("pass")

            elif self.expected=='fail':
                self.lp.clickLogout()
                list_status.append('fail')

          elif act_title!=exp_title:

              if self.expected=='pass':
                  list_status.append("fail")
              elif self.expected=='fail':
                  list_status.append('pass')
          print(list_status)
        if "fail" not in list_status:
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False

        #
        # if act_title=="Dashboard / nopCommerce administration":
        #     self.lp.clickLogout()
        #     assert True
        #
        #     self.driver.close()
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\" +"test_login.png")
        #     self.lp.clickLogout()
        #     self.driver.close()
        #
        #     assert False





# pytest -v -s Testcases/test_login.py
