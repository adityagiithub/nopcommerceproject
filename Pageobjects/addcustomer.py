import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class addcustomer():
    lnk_customers_xpath="//body/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[4]/a[1]"
    link_customersitem_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    click_Addnew_xpath="//body/div[3]/div[1]/form[1]/div[1]/div[1]/a[1]"
    txt_Email_xpath="//input[@id='Email']"
    txt_Password_Xpath="//input[@id='Password']"
    txt_Firstname_xpath=" //input[@id='FirstName']"
    txt_Lastname_xpath="//input[@id='LastName']"
    rb_malegender_xpath="//input[@id='Gender_Male']"
    rb_Femalegender_xpath=" //input[@id='Gender_Female']"
    txt_Dob_xpath=" //input[@id='DateOfBirth']"
    txt_Cmpyname_xpath="//input[@id='Company']"
    cbx_taxexmpt_xpath=" //input[@id='IsTaxExempt']"
    # txt_Newsletter_xpath="//div[@xpa"
    # lst_strname_xpath=" //option[contains(text(),'Your store name')]"
    # lst_str2_xpath=" //option[contains(text(),'Test store 2')]"
    drpdwn_Customerroles_xpath="//body/div[3]/div[1]/form[1]/section[1]/div[1]/div[1]/nop-cards[1]/nop-card[1]/div[1]/div[2]/div[10]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]"

    lst_Administrator_xpath=" //option[contains(text(),'Administrators')]"
    lst_Moderators_xpath="//option[contains(text(),'Forum Moderators')]"
    lst_Guests_xpath="//option[contains(text(),'Guests')]"
    lst_Registered_xapth="//option[contains(text(),'Registered')]"
    lst_vendors_xpath=" //option[contains(text(),'Vendors')]"
    drp_magofvendors_xpath="//select[@id='VendorId']"
    lst_notavendor_xpath="// option[contains(text(), 'Not a vendor')]"
    lst_vendor1_xpath=" //option[contains(text(),'Vendor 1')]"
    lst_vendor2_xpath=" //option[contains(text(),'Vendor 2')]"
    cbx_Active_xpath="//input[@id='Active']"
    txt_Admincomment_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickoncustomer(self):
        self.driver.find_element_by_xpath(self.lnk_customers_xpath).click()

    def clickcustomeritem(self):
        self.driver.find_element_by_xpath(self.link_customersitem_xpath).click()

    def clickonaddnew(self):
        self.driver.find_element_by_xpath(self.click_Addnew_xpath).click()

    def setemail(self,email):
        self.driver.find_element_by_xpath(self.txt_Email_xpath).send_keys(email)

    def setpassword(self,password):
        self.driver.find_element_by_xpath(self.txt_Password_Xpath).send_keys(password)

    def setfirstname(self,firstname):
        self.driver.find_element_by_xpath(self.txt_Firstname_xpath).send_keys(firstname)

    def setlastname(self,lastname):
        self.driver.find_element_by_xpath(self.txt_Lastname_xpath).send_keys(lastname)

    def setgender(self,gender):
        if gender=="male":
            self.driver.find_element_by_xpath(self.rb_malegender_xpath).click()
        elif gender=="female":
            self.driver.find_element_by_xpath(self.rb_Femalegender_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.rb_malegender_xpath).click()

    def setdob(self,dob):
        self.driver.find_element_by_xpath(self.txt_Dob_xpath).send_keys(dob)

    def setcompany(self,company):
        self.driver.find_element_by_xpath(self.txt_Cmpyname_xpath).send_keys(company)

    def clicktaxexpmnt(self):
        self.driver.find_element_by_xpath(self.cbx_taxexmpt_xpath).click()
    # def setnewsletter(self,newsletter):
    #     self.driver.find_element_by_xpath(self.txt_Newsletter_xpath).send_keys(newsletter)
    #
    # def setcustomeroles(self,role):
    #     self.driver.find_element_by_xpath(self.drpdwn_Customerroles_xpath).click()
    #
    #     if role == 'Registered':
    #         self.list = self.driver.find_element_by_xpath(self.lst_Registered_xapth).click()
    #     elif role == 'Administrators':
    #         self.list = self.driver.find_element_by_xpath(self.lst_Administrator_xpath).click()
    #     elif role == 'Guests':
    #         # Here user can be Registered( or) Guest, only o
    #         self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
    #         self.list = self.driver.find_element_by_xpath(self.lst_Guests_xpath)
    #
    #     elif role == 'Vendors':
    #         self.listitem = self.driver.find_element_by_xpath(self.lst_vendors_xpath).click()
    #
    #     time.sleep(3)
    #     self.listitem.click()
    #     self.driver.execute_script("arguments[0].click();", self.list)

    def select_managerofvendor(self,vendor):
        self.driver.find_element_by_xpath(self.drp_magofvendors_xpath).click()
        if vendor=='Not a vendor':
            self.driver.find_element_by_xpath(self.lst_notavendor_xpath).click()
        elif vendor=='vendor 1':
            self.driver.find_element_by_xpath(self.lst_vendor1_xpath).click()
        elif vendor=='vendor 2':
            self.driver.find_element_by_xpath(self.lst_vendor2_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.lst_notavendor_xpath).click()
        time.sleep(3)

    def clickcbxactive_xpath(self):
        self.driver.find_element_by_xpath(self.cbx_Active_xpath).click()

    time.sleep(3)
    def write_txtcomment(self,txt):
        self.driver.find_element_by_xpath(self.txt_Admincomment_xpath).send_keys(txt)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()

