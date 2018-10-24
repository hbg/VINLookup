import urllib 
from bs4  import BeautifulSoup
import ssl
import re
import time
import random
import os
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
chromedriver = 'C:\Python27\selenium\webdriver\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)


def checkLicensePlate(stateInitials, licensePlate):
	browser.get('https://www.autocheck.com/vehiclehistory/autocheck/en/search-by-license-plate')
	browser.find_element_by_id('plateNumber').send_keys(licensePlate)
	browser.find_element_by_id('state').click()
	browser.find_element_by_xpath("//*[contains(text(), '%s')]" % stateInitials).click()
	browser.find_element_by_id('plateSearch').click()
checkLicensePlate("CA","6JVC693")
