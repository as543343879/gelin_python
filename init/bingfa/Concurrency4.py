import asyncio
import time


async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')


async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')


async def main():
    print('before await')
    await worker_1()
    print('awaited worker_1')
    await worker_2()
    print('awaited worker_2')


async def main2():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print('before await')
    await task1
    print('awaited worker_1')
    await task2
    print('awaited worker_2')

start_time = time.time()
asyncio.run(main())
end_time = time.time()

print(end_time - start_time)

print("--------------------------")

start_time = time.time()
asyncio.run(main2())
end_time = time.time()

print(end_time - start_time)