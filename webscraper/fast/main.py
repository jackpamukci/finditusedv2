from fastapi import FastAPI
import json
from scrapers import main

app = FastAPI()

@app.get("/{search}")
async def read(search):
    loop = asyncio.get_event_loop()
    try:
        product = loop.run_until_complete(main(search, 3))
    finally:
        print('done')

    return json(product)
