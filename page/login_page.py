from selenium.webdriver.common.by import By


class LoginPage:
    __un=(By.ID,"txtUsername")
    __pwd=(By.ID,"txtPassword")
    __loginbutton=(By.ID,"btnLogin")

    def __init__(self,driver):
        self.driver=driver

    def set_username(self,un):
        self.driver.find_element(*self.__un).send_keys(un)

    def set_password(self,pwd):
        self.driver.find_element(*self.__pwd).send_keys(pwd)


    def click_login(self):
        self.driver.find_element(*self.__loginbutton).click()