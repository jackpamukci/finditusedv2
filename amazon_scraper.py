from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

import requests
import json
import time

# comments for fuckery

def search_amazon():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.amazon.com/FIFA-22-PlayStation-4/dp/B098KVCFM8')
    driver.close()

search_amazon()
