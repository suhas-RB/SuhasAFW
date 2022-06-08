from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

class VacanciesPage:

    __vacancies_page=(By.XPATH,"//h1[.='Vacancies']")
    __jobtitle=(By.ID,"vacancySearch_jobTitle")
    __vacancy=(By.ID,"vacancySearch_jobVacancy")
    __hiringmanager=(By.ID,"vacancySearch_hiringManager")
    __search_button=(By.ID,"btnSrch")

    def __init__(self,driver):
        self.driver=driver


    def verify_vacanciespage(self,wait):

        try:
           wait.until(expected_conditions.visibility_of_element_located(self.__vacancies_page))
           print("vacancies page is displayed")
           return True

        except:
            print("vacancies page is not displayed")
            return False


    def vacancies_jobtitle(self,jobtitle):
        sel=Select(self.driver.find_element(*self.__jobtitle))
        sel.select_by_visible_text(jobtitle)

    def vacancies_vacancy(self,vacancy):
        sel=Select(self.driver.find_element(*self.__vacancy))
        sel.select_by_visible_text(vacancy)

    def vacancy_hiringmanager(self,hiringmanager):
        sel = Select(self.driver.find_element(*self.__hiringmanager))
        sel.select_by_visible_text(hiringmanager)


