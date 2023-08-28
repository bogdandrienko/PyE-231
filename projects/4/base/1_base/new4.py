import asyncio
import random
import requests
import aiohttp
import aiofiles


url = "https://picsum.photos/320/240/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}


def data2():
    with open(f"temp2/image{random.randint(1, 10000000)}.jpg", "wb") as opened_file:
        opened_file.write(requests.get(url=url, headers=headers).content)


# data2()


async def async_t():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as response:
            data = await response.read()  # тут поток начинает делать другие задачи, пока эта задача не изменит свой статус

            with open(f"temp2/image{random.randint(1, 10000000)}.jpg", "wb") as opened_file:
                opened_file.write(data)

asyncio.run(async_t())  #

# event_loop = asyncio.get_event_loop()
# event_loop.run_until_complete(async_t())


