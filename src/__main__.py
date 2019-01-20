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
from Setup.tester import tester
from selenium.webdriver.chrome.options import Options
import pymongo
from pymongo import MongoClient
import selenium
import cv2


jsonConfigPATH = "C:\\Python27\\VINLookup.json"


declared = Configure(jsonConfigPATH)
signalparameters = {
	"user": declared.data["user"],
	"password": declared.data["password"],
	"host": declared.data["host"],
	"port": declared.data["port"],
	"namespace": declared.data["namespace"],
}
autoURL = 'https://www.autocheck.com/vehiclehistory/autocheck/en/search-by-license-plate'

conn = MongoClient(
    'mongodb://{user}:{password}@{host}:'
    '{port}/{namespace}'.format(**signalparameters)
)

db = conn.licenseplates
browser = webdriver.Chrome(declared.chromedriver,   chrome_options=declared.chrome_options)


def findByID(ID):
	return browser.find_element_by_id(ID)

def checkLicensePlate(stateInitials, licensePlate):
	browser.get(autoURL)
	findByID('plateNumber').send_keys(licensePlate)
	findByID('state').click()
	browser.find_element_by_xpath("//*[contains(text(), '%s')]" % stateInitials).click()
	findByID('plateSearch').click()
	time.sleep(1.0)
	element = findByID('test_vinSummary_carSpecification_$4')
	summary = element.get_attribute('innerHTML')
	#print(summary)
	carName = summary.split('<h2>')[1].split('</h2>')[0].replace('&nbsp;',' ').upper()
									"""

									CROSS CHECK FOR COMPANY NAME & YEAR IN CAR NAME

									"""
	carMake = ""
	carYear = 0
	for mk in CarSetup.makesList:
		if (mk.upper() in carName):
			carName = carName.replace(mk.upper(), "")
			carMake = mk
	for i in range(1885, int(datetime.now().year) + 1):
		if str(i) in carName:
			carName = carName.replace(str(i), "")
			carYear = i
	carModel = carName.replace(" ","")
	VroomVroom = CarSetup.Car(carMake, carModel, carYear)
	db.test.insert(VroomVroom.info)
	print(VroomVroom.info)


state = input("STATE of License's Origin (initials): ").upper()	
lp = input("License Plate: ").upper()	

checkLicensePlate(state, lp)
