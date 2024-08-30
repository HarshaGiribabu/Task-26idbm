import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from imdb_search_page import IMDbSearchPage  # Assuming you save the IMDbSearchPage class in imdb_search_page.py


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.mark.usefixtures("setup")
class TestIMDbSearch:
    def test_search_by_name(self):
        # Instantiate the page object
        search_page = IMDbSearchPage(self.driver)

        # Load the IMDb search page
        search_page.load()

        # Fill in the form
        search_page.enter_name("Tom Hanks")
        search_page.enter_birth_year("1956")
        search_page.enter_death_year("")  # Keep empty if no input
        search_page.enter_professions("Actor")
        search_page.select_sort_option("alpha")  # Sorting alphabetically

        # Submit the form
        search_page.click_search()

        # Assert that results are displayed
        assert "Tom Hanks" in self.driver.page_source
