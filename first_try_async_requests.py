import socket
import asyncio

import aiohttp

GET_POST_URL = 'https://hacker-news.firebaseio.com/v0/item/{}.json'
GET_MAX_ITEM_URL = 'https://hacker-news.firebaseio.com/v0/maxitem.json'


# A simple async fetch function
async def fetch(url, session):
    # (a)waiting for the server response to come back
    # (during that time the event loop is free)
    async with session.get(url) as response:
        # reading the response and parsing in is also async operation
        return await response.json()


# The main function to download, get the number of posts to download as n
async def run(n):
    # specify connector resolver family to be ipv4
    conn = aiohttp.TCPConnector(
            family=socket.AF_INET,
            verify_ssl=False,
            )
    # fetch all responses within one Client session,
    # keep connection alive for all requests
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(GET_MAX_ITEM_URL) as resp:
            max_item = await resp.json()
        # init the future, each future is a url-request
        tasks = [
                asyncio.ensure_future(fetch(
                    GET_POST_URL.format(max_item-i),
                    session)) for i in range(n)]

        # wait for all responses to come back
        return await asyncio.gather(*tasks)


def get_last_n_stories(n=10):
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(n))
    return loop.run_until_complete(future)

responses = get_last_n_stories()
print(responses)
