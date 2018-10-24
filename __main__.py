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
from selenium.webdriver.chrome.options import Options

import selenium
chromedriver = 'C:\Python27\selenium\webdriver\chromedriver.exe'
chrome_options = Options()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
browser = webdriver.Chrome(chromedriver,   chrome_options=chrome_options)


def checkLicensePlate(stateInitials, licensePlate):
	browser.get('https://www.autocheck.com/vehiclehistory/autocheck/en/search-by-license-plate')
	browser.find_element_by_id('plateNumber').send_keys(licensePlate)
	browser.find_element_by_id('state').click()
	browser.find_element_by_xpath("//*[contains(text(), '%s')]" % stateInitials).click()
	browser.find_element_by_id('plateSearch').click()
	time.sleep(1.0)
	element = browser.find_element_by_id('test_vinSummary_carSpecification_$4')
	summary = element.get_attribute('innerHTML')
	carName = summary.split('<h2>')[1].split('</h2>')[0].replace('&nbsp;',' ')
	print("Is your car a %s?" % carName)

checkLicensePlate("CA","ERROR405")
