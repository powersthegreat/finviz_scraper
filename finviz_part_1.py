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
from top_500_part_2 import top_500_list

url = "https://finviz.com/quote.ashx?t="

ticker_list = top_500_list("sp500.xlsx")
ticker_list_practice = ticker_list[0:1]

PATH = "C:\Webdrivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(7)
driver.maximize_window()

xlwriter = pandas.ExcelWriter("finviz_500_report.xlsx")

for ticker in ticker_list_practice:
    driver.get(url + str(ticker))
    time.sleep(2)

    print(f"Processing page: {ticker}")

    try:
        #7 was first table
        #///html/body/div[4]/div/table[3]/tbody/tr[10]/td/div/table[2]
        df = pandas.read_html(driver.page_source)[2][1]
        df.replace('-', '', inplace=True)
        df.to_excel(xlwriter, sheet_name=ticker, index=False)

    #once again bringing time standards to the program so I can know 'how things are going'
    except (NoSuchElementException, TimeoutException):
        print(f"Report {ticker} is not found")
        continue
    time.sleep(2)

xlwriter.save()

driver.quit()
    



