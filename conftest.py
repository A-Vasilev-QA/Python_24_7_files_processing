import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session", autouse=True)
def browser_config():
    browser.config.base_url = "https://file-examples.com/index.php/sample-documents-download/"

    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    prefs = {
        "download.default_directory": r"/Users/Aleksei_Vasilev5/PycharmProjects/Python_24_7_files_processing/resources",
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.config.driver = driver

    yield

    driver.quit()

