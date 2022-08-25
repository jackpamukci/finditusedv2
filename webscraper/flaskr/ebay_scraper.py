# Imports

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def add_plus(keywords):
    keywords = keywords.split()
    keyword_edited = ""
    for i in keywords:
        keyword_edited += i + "+"
    keyword_edited = keyword_edited[:-1]
    return keyword_edited


def search_ebay(item, kac, dri):
    driver = dri
    plusified_keyword = add_plus(item)
    url = "https://www.ebay.com/sch/i.html?_nkw=" + plusified_keyword


    driver.get(url)
    driver.implicitly_wait(1)

    data = []

    try:
        title = driver.find_elements(By.CLASS_NAME, 's-item__title')
        price = driver.find_elements(By.CLASS_NAME, 's-item__price')
        picture = driver.find_elements(By.CLASS_NAME, 's-item__image-img')
        link = driver.find_elements(By.CLASS_NAME, 's-item__link')

        for i in range(int(kac)):
            data.append({
                'title' : title[i + 1].text,
                'price' : price[i + 1].text,
                'picture' : picture[i + 1].get_attribute("src"),
                'link' : link[i + 1].get_attribute("href")
            })

    except NoSuchElementException:
        title, price, picture, link = 'no data found'
        data.append({
            'title' : title,
            'price' : price,
            'picture' : picture,
            'link' : link
        })

    return data



    
