from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class IMDbSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_url = "https://www.imdb.com/search/name/"

    # Locators
    NAME_BOX = (By.NAME, 'name')
    BIRTH_YEAR_BOX = (By.NAME, 'birth_date')
    DEATH_YEAR_BOX = (By.NAME, 'death_date')
    PROFESSIONS_BOX = (By.NAME, 'professions')
    SORT_DROPDOWN = (By.NAME, 'sort')
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")

    def load(self):
        self.driver.get(self.search_url)

    def enter_name(self, name):
        name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.NAME_BOX)
        )
        name_input.clear()
        name_input.send_keys(name)

    def enter_birth_year(self, birth_year):
        birth_year_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.BIRTH_YEAR_BOX)
        )
        birth_year_input.clear()
        birth_year_input.send_keys(birth_year)

    def enter_death_year(self, death_year):
        death_year_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DEATH_YEAR_BOX)
        )
        death_year_input.clear()
        death_year_input.send_keys(death_year)

    def enter_professions(self, profession):
        profession_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.PROFESSIONS_BOX)
        )
        profession_input.clear()
        profession_input.send_keys(profession)

    def select_sort_option(self, sort_option_value):
        sort_dropdown = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SORT_DROPDOWN)
        )
        sort_dropdown.send_keys(sort_option_value)
        sort_dropdown.send_keys(Keys.RETURN)

    def click_search(self):
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )
        search_button.click()
