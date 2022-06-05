from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

class EmployeeEntitlementsPage:

    __emp_TB=(By.ID,"entitlements_employee_empName")
    __leaveperiod_lb=(By.ID,"period")
    __search_button=(By.ID,"searchBtn")
    __result_norecfound=(By.XPATH,"//td[.='No Records Found']")
    __ent_page=(By.XPATH,"//h1[.='Leave Entitlements']")

    def __init__(self,driver):
        self.driver=driver


    def employeename(self,empname):
        self.driver.find_element(*self.__emp_TB).send_keys(empname)

    def leaveperiod(self,period):
        sel=Select(self.driver.find_element(*self.__leaveperiod_lb))
        sel.select_by_visible_text(period)


    def clicksearch(self):
        self.driver.find_element(*self.__search_button).click()


    def verifyentitlementspage(self,wait):

        try:
            wait.until(expected_conditions.visibility_of_element_located(self.__ent_page))
            print("Entitlements page is displayed")
            return True

        except:
            print("Entitlements page is not displayed")
            return False




