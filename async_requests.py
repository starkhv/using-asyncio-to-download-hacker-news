import asyncio
import aiohttp

URL_GET_POST = "https://hacker-news.firebaseio.com/v0/item/{}.json"
URL_MAX_ITEM = "https://hacker-news.firebaseio.com/v0/maxitem.json"

async def get_max_item():
    async with aiohttp.ClientSession() as session:
        async with session.get(URL_MAX_ITEM) as resp:
            max_item = await resp.json()
            return max_item

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(get_max_item())
max_item = loop.run_until_complete(future)
print(max_item)
