# Imports

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# comments for fuckery

def grab_amazon(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1420,1080")
    chrome_options.add_argument("--disable-gpu")


    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get(url)
    driver.implicitly_wait(1)

    try:
        prod_title = driver.find_element(By.XPATH, '//*[@id="productTitle"]').text
    except NoSuchElementException:
        prod_title = 'no title found'

    try:
        prod_price = driver.find_element(By.XPATH, '//*[@id="priceblock_ourprice"]').text
    except NoSuchElementException:
        prod_price = 'price not found'

    try:
        prod_picture = driver.find_element(By.XPATH, '//*[@id="landingImage"]').get_attribute("src")
    except NoSuchElementException:
        prod_picture = 'image not found'

    driver.close()

    return {
        "title" : prod_title,
        "price" : prod_price,
        "picture": prod_picture
    }



