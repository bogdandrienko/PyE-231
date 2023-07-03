import random

import aiohttp
import asyncio
import tkinter as tk


async def async_download_one_image():
    url = "https://picsum.photos/320/240"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(f"temp2/image{random.randint(1, 10000)}.jpg", "wb") as opened_file:
                opened_file.write(data)
                print("img write")


def async_task():
    async def async_task_inline():
        await asyncio.gather(*[async_download_one_image() for _ in range(1, 10 + 1)])

    asyncio.run(async_task_inline())



def window_for_async():
    window = tk.Tk()
    window.title("Downloading")
    window.geometry("300x150")
    button = tk.Button(window, text="Download Images ", command=async_task)
    button.pack()
    window.mainloop()

if __name__ == "__main__":
    window_for_async()
