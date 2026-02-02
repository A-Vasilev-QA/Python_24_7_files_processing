import time
import os
import zipfile
import csv

from selene.support.shared import browser

def test_files():

    browser.open("/sample-xls-download/")
    browser.element("button.fc-button.fc-cta-do-not-consent").click()
    browser.element("//a[contains(@href,'file_example_XLSX_10.xlsx')]").click()

    time.sleep(5)