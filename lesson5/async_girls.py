import asyncio
import time
from uuid import uuid1
import requests
import httpx

url = 'https://loremflickr.com/g/320/240/girl'


def time_decor(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(time.time() - start)

    return inner


# def get_response(url_address):
#     return requests.get(url_address, allow_redirects=True)
#
#
# def write_file(res: requests.Response):
#     file_name = f'{uuid1()}.jpeg'
#     with open(file_name, 'wb') as file:
#         file.write(res.content)
#
#
# @time_decor
# def cr_file():
#     global url
#     for _ in range(50):
#         write_file(get_response(url))
#
#
# cr_file()

def write_file(data):
    file_name = f'{uuid1()}.jpg'
    with open(file_name, 'wb') as file:
        file.write(data)


async def get_response(url, client):
    res = await client.get(url, follow_redirects=True)
    write_file(res.read())


async def cr_fls_async():
    global url
    tasks = []
    async with httpx.AsyncClient() as client:
        for _ in range(50):
            task = asyncio.create_task(get_response(url, client))
            tasks.append(task)
        await asyncio.gather(*tasks)


@time_decor
def main():
    asyncio.run(cr_fls_async())


main()
