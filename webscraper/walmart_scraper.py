# Imports

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



from random_user_agent import user_agent
from random_user_agent.params import SoftwareName, OperatingSystem
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType


software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value]

user_agent_rotator = user_agent.UserAgent(SoftwareName=software_names,OperatingSystem=operating_systems,limit=100)

user_agent = user_agent_rotator.get_random_user_agent()

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1420,1080")
chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument(f'user-agent={user_agent}')



def search_walmart(item, kac):
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    url = f"https://www.walmart.com/search?q={item}"


    driver.get(url)
    driver.implicitly_wait(0.5)

    data = []


    try:

        titles = driver.find_elements(By.XPATH, "//span[@data-automation-id='product-title']")
        prices = driver.find_elements(By.XPATH, "//div[@data-automation-id='product-price']")
        pictures = driver.find_elements(By.XPATH, "//img[@data-testid='productTileImage']")
        links = driver.find_elements(By.XPATH, "//a[@class='absolute w-100 h-100 z-1']")

        for i in range(kac):
            data.append({
                'title' : titles[i + 1].text,
                'price' : prices[i + 1].find_element(By.XPATH, "//div[@class='b black f5 mr1 mr2-xl lh-copy f4-l']").text,
                'picture' : pictures[i + 1].get_attribute('src'),
                'link' : links[i + 1].get_attribute('href')
            })

    except NoSuchElementException:
        title, price, picture, link = 'no data found'
        data.append({
            'title' : title,
            'price' : price,
            'picture' : picture,
            'link' : link
        })

    print(data)

search_walmart('fifa 22', 3)





    
