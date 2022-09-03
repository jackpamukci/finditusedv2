from requests_html import HTMLSession
import time

start = time.perf_counter()

url = 'https://www.amazon.com/s?k=fifa+22'

s = HTMLSession()
r = s.get(url)
r.html.render(sleep=1)

data = []

titles = r.html.xpath("//span[@class = 'a-size-medium a-color-base a-text-normal']")
whole_price = r.html.xpath(".//span[@class='a-price-whole']")
fraction_price = r.html.xpath(".//span[@class='a-price-fraction']")
imgs = r.html.xpath(".//img[@class = 's-image']")
links = r.html.xpath(".//a[@class = 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")

for i in range(3):
    if whole_price != [] and fraction_price != []:
        price = '.'.join([whole_price[i].text, fraction_price[i].text])
    else:
        price = 0

    data.append({
        'title' : titles[i].text,
        'price' : '$' + str(price),
        'img' : imgs[i].attrs['src'],
        'link' : links[i].absolute_links
    })

print(r.html)
fub = time.perf_counter() - start
print(fub)