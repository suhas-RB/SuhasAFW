from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class OrangeHRMPage:

        __v=(By.XPATH,"//h1[.='Dashboard']")
        __leave_button=(By.XPATH,"//b[.='Leave']")
        __ent_button=(By.XPATH,"//a[.='Entitlements']")
        __employeeent_button = (By.XPATH, "//a[.='Employee Entitlements']")
        __recruitment_button=(By.XPATH,"//b[.='Recruitment']")
        __vacancies_button=(By.XPATH,"//a[.='Vacancies']")

        def __init__(self,driver):
            self.driver=driver

        def verify_homepage(self,wait):

            try:
                wait.until(expected_conditions.visibility_of_element_located(self.__v))
                print("Home page is displayed")
                return True

            except:
                print("Home page is not displayed")
                return False

        def clickentitlementspage(self,action):
            action.move_to_element(self.driver.find_element(*self.__leave_button)).perform()
            action.move_to_element(self.driver.find_element(*self.__ent_button)).perform()
            self.driver.find_element(*self.__employeeent_button).click()


        def clickvacanciespage(self,action):
            action.move_to_element(self.driver.find_element(*self.__recruitment_button)).perform()
            self.driver.find_element(*self.__vacancies_button).click()
