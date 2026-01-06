import asyncio

async def printInEveryNSeconds(n: int, limit: int):
    for i in range(limit):
        print(f"value: {i}")
        await asyncio.sleep(n)

asyncio.run(printInEveryNSeconds(2, 2))


async def func1():
    print("Function 1 started..")
    await asyncio.sleep(2)
    print("Function 1 Ended")


async def func2():
    print("Function 2 started..")
    await asyncio.sleep(3)
    print("Function 2 Ended")


async def func3():
    print("Function 3 started..")
    await asyncio.sleep(1)
    print("Function 3 Ended")


async def main():
    L = await asyncio.gather(
        func1(),
        func2(),
        func3(),
    )
    print("Main Ended..")


asyncio.run(main())