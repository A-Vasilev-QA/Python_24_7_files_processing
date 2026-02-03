import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DOWNLOAD_DIR = BASE_DIR / "resources"


@pytest.fixture(scope="session", autouse=True)
def setup_browser():
    browser.config.base_url = "https://file-examples.com/index.php/sample-documents-download/"
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1980,1080")

    prefs = {
        "download.default_directory": str(DOWNLOAD_DIR),
        "download.prompt_for_download": False,
        "plugins.always_open_pdf_externally": True
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.config.driver = driver

    original_open = browser.open

    def open_with_ads_hidden(url):
        original_open(url)
        browser.driver.execute_script("""
            var style = document.createElement('style');
            style.innerHTML = 'iframe, ins.adsbygoogle, [id^="aswift"], #google_ads_iframe, .adsbygoogle { display: none !important; visibility: hidden !important; pointer-events: none !important; }';
            document.head.appendChild(style);
        """)
        return browser

    browser.open = open_with_ads_hidden

    yield browser

    driver.quit()