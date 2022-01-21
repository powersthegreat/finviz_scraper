# importing os, time, and pywin to make things run a little smoother, more specifically pywin gets rid of usb
# errors, os helps path of webdriver be called faster, and time allows for rest periods while data loads
import pywin
import os
import time

#various selenium webdriver imports for the various commands used including the Exceptions list
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException, NoSuchElementException

#importing bs4 even though it wasn't used I am afraid to touch this program and mess it up
#as well as importing pandas to create and export data frames of data pulled
from bs4 import BeautifulSoup
import pandas as pandas

urls = [
    "https://www.slickcharts.com/sp500",
]

#initiating driver instance and sending that instance the path where the driver is stored
#PATH = "C:\Program Files (x86)\chromedriver.exe"
PATH = "C:\Webdrivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(7)
driver.maximize_window()

for url in urls:
    driver.get(url)
    time.sleep(3)

    file_base_name = url.split('/')[-1]
    url_base_name = url.split('/')[-2]

    xlwriter = pandas.ExcelWriter(file_base_name + ".xlsx")

    print(f"Processing page: {url_base_name}")

    try:
        df = pandas.read_html(driver.page_source)[0]
        df.replace('-', '', inplace=True)
        df.to_excel(xlwriter, sheet_name=file_base_name, index=False)

    #once again bringing time standards to the program so I can know 'how things are going'
    except (NoSuchElementException, TimeoutException):
        print(f"Report {url_base_name} is not found")
        continue
    time.sleep(3)

xlwriter.save()

driver.quit()