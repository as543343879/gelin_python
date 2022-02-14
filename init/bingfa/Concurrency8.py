import asyncio
import time
from asyncio import shield, CancelledError

import requests
from bs4 import BeautifulSoup


async def worker_1():
    await asyncio.sleep(1)
    return 1


async def worker_2():
    await asyncio.sleep(2)
    return 2 / 0


async def something():
    await asyncio.sleep(10)
    print("---")
    return


async def main():
    try:
        task = asyncio.create_task(something())
        res = await shield(task)
        task.cancel()
    except CancelledError:
        print('----- CancelledError')
        res = None
    return res

start_time = time.time()
asyncio.run(main())
end_time = time.time()

print(end_time - start_time)
