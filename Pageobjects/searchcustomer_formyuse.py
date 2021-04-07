#
# class SearchCustomer:
#     lnk_customers_xpath = "//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]"
#     link_customersitem_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
#     txt_Email_xpath="//input[@id='SearchEmail']"
#     txt_Firstname_xpath="//input[@id='SearchFirstName']"
#     txt_Lastname_xpath=" //input[@id='SearchLastName']"
#     drp_dob_Month_xpath="//select[@id='SearchMonthOfBirth']"
#     from_drp_selectmonth_xpath=" //option[contains(text(),'Month')]"
#     drp_dob_Day_xpath=" //select[@id='SearchDayOfBirth']"
#     from_drp_selectday_xpath="//option[contains(text(),'Day')]"
#     txt_company_xpath="//input[@id='SearchCompany']"
#     txt_IPaddress_xpath="//input[@id='SearchIpAddress']"
#     btm_Search_xpath="//button[@id='search-customers']"
#     def __init__(self,driver):
#         self.driver=driver
#     def clickcusotmerlist(self):
#         self.driver.find_element_by_xpath(self.lnk_customers_xpath).click()
#     def clickcustomeritem(self):
#         self.driver.find_element_by_xpath(self.link_customersitem_xpath).click()
#     def enterEmail(self,email):
#         self.driver.find_element_by_xpath(self.txt_Email_xpath).send_keys(email)
#     def enterFirstname(self,firstname):
#         self.driver.find_element_by_xpath(self.txt_Firstname_xpath).send_keys(firstname)
#     def enterLastname(self,lastname):
#         self.driver.find_element_by_xpath(self.txt_Lastname_xpath).send_keys(lastname)
#     def selectmonthofdob(self,month):
#         self.driver.find_element_by_xpath(self.drp_dob_Month_xpath).click()
#         self.driver.find_element_by_xpath(self.from_drp_selectmonth_xpath).send_keys(month)
#     def selectdayofdob(self,day):
#         self.driver.find_element_by_xpath(self.drp_dob_Day_xpath).click()
#         self.driver.find_element_by_xpath(self.from_drp_selectday_xpath).send_keys(day)
#     def setcomapnyname(self,company):
#         self.driver.find_element_by_xpath(self.txt_company_xpath).send_keys(company)
#     def setipadress(self,ip):
#         self.driver.find_element_by_xpath(self.txt_IPaddress_xpath).send_keys(ip)
#     def entersearchbutton(self):
#         self.driver.find_element_by_xpath(self.btm_Search_xpath).click()
