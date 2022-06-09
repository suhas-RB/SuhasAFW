from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

class EmployeeEntitlementsPage:

    __emp_TB=(By.ID,"entitlements_employee_empName")
    __leaveperiod_lb=(By.ID,"period")
    __search_button=(By.ID,"searchBtn")
    __result_norecfound=(By.XPATH,"//td[.='No Records Found']")
    __verify_entpage=(By.XPATH,"//h1[.='Leave Entitlements']")
    __verify_search=(By.XPATH,"//td[.='No Records Found']")

    def __init__(self,driver):
        self.driver=driver


    def employeename(self,empname):
        self.driver.find_element(*self.__emp_TB).send_keys(empname)
        self.driver.find_element(*self.__emp_TB).send_keys(Keys.ENTER)

    def leaveperiod(self,period):
        sel=Select(self.driver.find_element(*self.__leaveperiod_lb))
        sel.select_by_visible_text(period)


    def clicksearch(self):
        self.driver.find_element(*self.__search_button).click()


    def verifyentitlementspage(self,wait):

        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__verify_entpage))
            print("Entitlements page is displayed")
            return True

        except:
            print("Entitlements page is not displayed")
            return False


    def verifysearch(self):
        try:

            self.driver.find_element(*self.__verify_search)
            print("No leave entitlements found for the given match")


        except:
            print("leave entitlements found for the given match")

