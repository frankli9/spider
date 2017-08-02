# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from bs4 import BeautifulSoup

browser=webdriver.Chrome()
browser.implicitly_wait(3)
browser.get('https://tw.eztable.com/channel/1013')
for i in range(1,10):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(2)
soup=BeautifulSoup(browser.page_source,"lxml")
for ele in soup.select('.info-wrapper h4'):
    print(ele.text)
# browser.find_element_by_id("paginationNext").click()
#browser.close()




