import asyncio
import aiohttp

urls = [
    "https://www.baidu.com/",
    "https://www.qq.com/"
]


async def main(url):
    async with aiohttp.ClientSession() as client:
        response = await client.get(url)
        print(await response.text())

tasks = [
    main(url)
    for url in urls
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
