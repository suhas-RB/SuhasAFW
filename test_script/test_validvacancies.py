from selenium.webdriver import ActionChains
import pytest
from generic.Base_Setup import Base_Setup
import openpyxl
from generic.read_data import Excel
from page.login_page import LoginPage
from page.OrangeHRM_page import OrangeHRMPage
from page.vacancies_page import VacanciesPage

class Test_validvacancies(Base_Setup):


    @pytest.mark.run(order=3)
    def test_employeevacancies(self):

        #validlogin
        un=Excel.read_data(self.xl_path,"login",2,1)
        pwd=Excel.read_data(self.xl_path,"login",2,2)

        print(un,pwd)
        loginpage=LoginPage(self.driver)

        #enter username
        loginpage.set_username(un)

        #enter password
        loginpage.set_password(pwd)

        #click login
        loginpage.click_login()

        homepage=OrangeHRMPage(self.driver)

        #verify home page is displayed
        homepage.verify_homepage(self.wait)

        #click vacancies button
        actions=ActionChains(self.driver)
        homepage.clickvacanciespage(actions)



        vacanciespage=VacanciesPage(self.driver)

        #verify vacancies page displayed
        result=vacanciespage.verify_vacanciespage(self.wait)

        if result==True:

            jt=Excel.read_data(self.xl_path,"vacancies",2,1)
            vacancy=Excel.read_data(self.xl_path,"vacancies",2,2)
            hm=Excel.read_data(self.xl_path,"vacancies",2,3)

            #select job title
            vacanciespage.vacancies_jobtitle(jt)

            #select vacancy
            vacanciespage.vacancies_vacancy(vacancy)

            #select hiring manager
            vacanciespage.vacancy_hiringmanager(hm)

            #click search
            vacanciespage.clicksearch()

            #verify if records displayed
            vacanciespage.vacancies_verifyrecords()