# Imports

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def search_amazon(item, kac):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = "https://www.amazon.com/s?k=" + item


    driver.get(url)
    driver.implicitly_wait(0.5)

    data = []

    

    try:

        # items = driver.find_element(By.XPATH, "//span[@data-component-type='s-search-results']")
        # prods = items.find_elements(By.CSS_SELECTOR, 'div')[2]
        # listo = prods.find_element()

        stuff = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
        
        for i in range(int(kac)): 

            whole_price = stuff[i].find_elements(By.XPATH, './/span[@class="a-price-whole"]')
            fraction_price = stuff[i].find_elements(By.XPATH,'.//span[@class="a-price-fraction"]')
            if whole_price != [] and fraction_price != []:
                price = '.'.join([whole_price[0].text, fraction_price[0].text])
            else:
                price = 0

            data.append({
                'title' : stuff[i].find_element(By.XPATH, ".//span[@class = 'a-size-medium a-color-base a-text-normal']").text,
                'price' : '$' + price,
                'picture' : stuff[i].find_element(By.XPATH, ".//img[@class = 's-image']").get_attribute('src'),
                'link' : stuff[i].find_element(By.XPATH, ".//a[@class = 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']").get_attribute('href')
            })

    except NoSuchElementException:
        data.append({
            'title' : 'api failed',
            'price' : 'api failed',
            'picture' : 'api failed',
            'link' : 'api failed'
        })

        print('something happened')

    return data

search_amazon('skateboard', 3)


    
