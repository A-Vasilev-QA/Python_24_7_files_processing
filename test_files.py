import time
import os
import zipfile
import csv

from selene.support.shared import browser
from pathlib import Path
from selene.support.conditions import be, have
from conftest import DOWNLOAD_DIR
from selene import command

def remove_ads(browser):
    browser.driver.execute_script("""
        document.querySelectorAll('iframe, .adsbygoogle, [id^="aswift"], [class*="overlay"], [class*="popup"]').forEach(el => el.remove());
    """)

def test_files():
    filename_pdf = "file-sample_150kB.pdf"
    filename_xlsx = "file_example_XLSX_10.xlsx"
    filename_csv = "file_example_CSV_5000.csv"

    browser.open("/sample-xls-download/")
    browser.element("button.fc-button.fc-cta-do-not-consent").click()
    browser.element(f"a[href*='{filename_xlsx}']").click()
    filepath = Path(DOWNLOAD_DIR) / filename_xlsx
    browser.wait.until(lambda: filepath.exists())

    browser.open("/sample-pdf-download/")
    browser.element(f"a[href*='{filename_pdf}']").perform(command.js.click)
    filepath = Path(DOWNLOAD_DIR) / filename_pdf
    browser.wait.until(lambda: filepath.exists())

    browser.open("/text-files-and-archives-download/")
    browser.element(f"a[href*='{filename_csv}']").perform(command.js.click)
    filepath = Path(DOWNLOAD_DIR) / filename_csv
    browser.wait.until(lambda: filepath.exists())
