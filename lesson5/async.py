import asyncio


async def print_num():
    n = 0
    while True:
        print('num= ', n)
        n += 1
        await asyncio.sleep(0.1)


async def print_time_one_second():
    t = 0
    while True:
        print('time: ', t)
        t += 1
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_num())
    task2 = asyncio.create_task(print_time_one_second())
    await asyncio.gather(task1, task2)


# asyncio.run(print_num())
# asyncio.run(print_time_one_second())
asyncio.run(main())
