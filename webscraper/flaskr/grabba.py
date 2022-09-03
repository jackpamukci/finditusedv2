# Imports

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from amazon_scraper import search_amazon
from ebay_scraper import search_ebay



from mercari_scraper import search_mercari


# comments for fuckery

def search_me(title, kac):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1420,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--log-level=1')


    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    merc = search_mercari(title, kac, driver)

    data = {
        'amazon' : search_amazon(title, kac, driver),
        'ebay' : search_ebay(title, kac, driver),
        'mercari' : merc
    }

    return data

print(search_me('assassins creed', 3))





    


