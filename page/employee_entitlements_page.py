from selenium.webdriver.common.by import By


class EmployeeEntitlementsPage:
    __ent_button=(By.XPATH,"//a[.='Employee Entitlements']")
    __emp_TB=(By.ID,"entitlements_employee_empName")
    __leaveperiod_lb=(By.ID,"period")