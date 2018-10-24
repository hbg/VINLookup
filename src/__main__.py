import urllib 
from bs4  import BeautifulSoup
from CarProperties import CarSetup
from Setup.Configure import Configure
import ssl
import re
import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import selenium

declared = Configure()
browser = webdriver.Chrome(declared.chromedriver,   chrome_options=declared.chrome_options)


def checkLicensePlate(stateInitials, licensePlate):
	browser.get('https://www.autocheck.com/vehiclehistory/autocheck/en/search-by-license-plate')
	browser.find_element_by_id('plateNumber').send_keys(licensePlate)
	browser.find_element_by_id('state').click()
	browser.find_element_by_xpath("//*[contains(text(), '%s')]" % stateInitials).click()
	browser.find_element_by_id('plateSearch').click()
	time.sleep(1.0)
	element = browser.find_element_by_id('test_vinSummary_carSpecification_$4')
	summary = element.get_attribute('innerHTML')
	print(summary)
	carName = summary.split('<h2>')[1].split('</h2>')[0].replace('&nbsp;',' ')
	"""

	CROSS CHECK FOR COMPANY NAME & YEAR IN CAR NAME

	"""
	carMake = ""
	carYear = 0
	for mk in CarSetup.makesList:
		if (mk in carName):
			carName = carName.replace(mk, "")
			carMake = mk
	for i in range(1885, int(datetime.now().year) + 1):
		if str(i) in carName:
			carName = carName.replace(str(i), "")
			carYear = i
	carModel = this.replace(" ","")
	VroomVroom = CarSetup.Car(carMake, carModel, carYear)
	print(VroomVroom.info)

	

checkLicensePlate("CA","6JVC693")
