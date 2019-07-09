from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup


driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://nid.naver.com/nidlogin.login")

def login():
    time.sleep(0.5)
    driver.find_element_by_name('id').send_keys('moduedu')
    time.sleep(0.5)
    driver.find_element_by_name('pw').send_keys('passwerd')
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
login()


