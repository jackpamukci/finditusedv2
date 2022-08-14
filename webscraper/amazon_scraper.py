# Imports

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# comments for fuckery

def search_amazon():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.amazon.com/FIFA-22-PlayStation-4/dp/B098KVCFM8')
    driver.implicitly_wait(1)

    try:
        prod_title = driver.find_element(By.XPATH, '//*[@id="productTitle"]').text
    except NoSuchElementException:
        print('title not found')

    try:
        prod_picture = driver.find_element(By.XPATH, '//*[@id="landingImage"]').get_attribute("src")
    except NoSuchElementException:
        prod_picture = 'image not found'

    driver.close()

    return {
        "title" : prod_title,
        "picture": prod_picture
    }

search_amazon()

