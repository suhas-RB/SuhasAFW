import pytest
from selenium.webdriver import ActionChains

from generic.Base_Setup import Base_Setup
from generic.read_data import Excel
from page.employee_entitlements_page import EmployeeEntitlementsPage
from page.login_page import LoginPage
from page.OrangeHRM_page import OrangeHRMPage


class Test_B(Base_Setup):

    @pytest.mark.run(order=2)
    def test_employeeentitlements(self):

        #valid login
        un = Excel.read_data(self.xl_path, "login", 2, 1)
        pwd = Excel.read_data(self.xl_path, "login", 2, 2)

        loginpage = LoginPage(self.driver)

        loginpage.set_username(un)

        loginpage.set_password(pwd)

        loginpage.click_login()

        orangeHRMpage = OrangeHRMPage(self.driver)
        result = orangeHRMpage.verify_homepage(self.wait)

        if result==True:

            empname=Excel.read_data(self.xl_path,"empentitlements",2,1)
            period=Excel.read_data(self.xl_path,"empentitlements",2,2)

            entitlementspage=EmployeeEntitlementsPage(self.driver)

            #click Employee Entitlements page
            homepage=OrangeHRMPage(self.driver)
            actions=ActionChains(self.driver)
            homepage.clickentitlementspage(actions)
            result1=entitlementspage.verifyentitlementspage(self.wait)

            if result1==True:

                #Type Employee Name
                entitlementspage.employeename(empname)

                #select period
                entitlementspage.leaveperiod(period)

                #click search
                entitlementspage.clicksearch()

            else:
                print("Entitlements page is not displayed")
                assert False


        else:
            print("Home page is not displayed")
            assert False
