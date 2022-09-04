from requests_html import AsyncHTMLSession
import asyncio
import time



#///////////////////////////////////////////////////////////////
async def ebay(s, search, kac):
    url = f"https://www.ebay.com/sch/i.html?_nkw={search}"
    r = await s.get(url)
        
    data = []

    title = r.html.find(".s-item__title")
    price = r.html.find(".s-item__price")
    img = r.html.find(".s-item__image-img")
    link = r.html.find(".s-item__link")

    for i in range(int(kac)):
        data.append({
            'title' : title[i + 1].text,
            'price' : price[i + 1].text,
            'img' : img[i + 1].attrs['src'],
            'link' : list(link[i + 1].absolute_links)[0]
        })

    return data
#/////////////////////////////////////////////////////////////
async def amazon(s, search, kac):
    url = f'https://www.amazon.com/s?k={search}'

    r = await s.get(url)

    await r.html.arender()

    data = []

    titles = r.html.xpath("//span[@class = 'a-size-medium a-color-base a-text-normal']")
    whole_price = r.html.xpath(".//span[@class='a-price-whole']")
    fraction_price = r.html.xpath(".//span[@class='a-price-fraction']")
    imgs = r.html.xpath(".//img[@class = 's-image']")
    links = r.html.xpath(".//a[@class = 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")

    for i in range(int(kac)):
        if whole_price != [] and fraction_price != []:
            price = '.'.join([whole_price[i].text, fraction_price[i].text])
        else:
            price = 0

        data.append({
            'title' : titles[i].text,
            'price' : '$' + str(price),
            'img' : imgs[i].attrs['src'],
            'link' : list(links[i].absolute_links)[0]
        })
        

    return data
#/////////////////////////////////////////////////////////
async def newegg(s, search, kac):
    url = f'https://www.newegg.com/p/pl?d={search}'

    r = await s.get(url)

    data = []

    titles = r.html.find('.item-title')
    price = r.html.find("li.price-current")
    imgs = r.html.find("img[src]")

    for i in range(int(kac)):

        data.append({
            'title' : titles[i + 5].text,
            'price' : price[i].text,
            'img' : imgs[i + 1].attrs['src'],
            'link' : list(titles[i + 5].absolute_links)[0]
        })

    return data



#/////////////////////////////////////////////////////////

async def main(search, kac):
    s = AsyncHTMLSession()
    tasks = []
    tasks.append(asyncio.create_task(ebay(s, search, kac)))
    tasks.append(asyncio.create_task(amazon(s, search, kac)))
    tasks.append(asyncio.create_task(newegg(s, search, kac)))
    results = await asyncio.gather(*tasks)
    star = dict(zip(['ebay', 'newegg', 'mercari'],results))
    return star
        # amazon(s, search, kac), 
        # newegg(s, search, kac)
                        


def mano(search, kac):
    return asyncio.run(main(search, kac))


# def getem(search, kac):
#     # results = asyncio.run(main('assassins creed 2', 3))
#     loop = asyncio.new_event_loop()
#     results = loop.run_until_complete(main(search, kac))
#     fub = time.perf_counter() - start
#     print(fub)
#     print(results)

# getem('fifa 22', 3)
    
