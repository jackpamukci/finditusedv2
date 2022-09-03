# Imports

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager




def search_mercari(item, kac):



    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = f"https://www.mercari.com/search/?keyword={item}"


    driver.get(url)
    driver.implicitly_wait(0.5)

    data = []

    try:
        title = driver.find_elements(By.XPATH, "//div[@data-testid='ItemName']")
        price = driver.find_elements(By.XPATH, "//p[@data-testid='ItemPrice']")
        picture = driver.find_elements(By.XPATH, "//div[@data-testid='StyledProductThumb']")
        link = driver.find_element(By.XPATH, "//div[@data-testid='SearchResults']")

        for i in range(int(kac)):
            data.append({
                'title' : title[i].text,
                'price' : price[i].find_element(By.CSS_SELECTOR, 'span').text,
                'picture' : picture[i].find_element(By.CSS_SELECTOR, 'div').find_element(By.CSS_SELECTOR, 'img').get_attribute('src'),
                'link' : 'mercari.com' + link.find_elements(By.CSS_SELECTOR, 'a')[i].get_attribute('href')
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



    
