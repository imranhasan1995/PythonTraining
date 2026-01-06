import asyncio
from contextlib import asynccontextmanager

lock = asyncio.Lock()

@asynccontextmanager
async def acquireLock(name: str):
    print(f"{name}: waiting for lock")
    if not lock.locked():
        await lock.acquire()
    print(f"{name}: lock acquired")
    try:
        yield
    finally:
        if lock.locked():
            lock.release()
        print(f"{name}: lock released")

async def worker(name: str):
    async with acquireLock(name):
        print(f"{name}: inside critical section")
        await asyncio.sleep(1)
        print(f"{name}: leaving critical section")


async def main():
    await asyncio.gather(
        worker("Task-1"),
        worker("Task-2"),
        worker("Task-3"),
    )

asyncio.run(main())