from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class OrangeHRMPage:

        __v=(By.XPATH,"//h1[.='Dashboard']")

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
