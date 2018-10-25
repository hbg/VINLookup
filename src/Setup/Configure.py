import urllib 
from bs4  import BeautifulSoup
import ssl
import re
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import selenium
class Configure:

	def __init__(self, jsonpath):
		self.chromedriver = 'C:\Python27\selenium\webdriver\chromedriver.exe'
		self.chrome_options = Options()

		ctx = ssl.create_default_context()
		ctx.check_hostname = False
		ctx.verify_mode = ssl.CERT_NONE

		with open(jsonpath) as f:
    			self.data = json.load(f)