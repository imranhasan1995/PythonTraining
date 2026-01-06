import asyncio

class AsyncCounter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current >= self.limit:
            raise StopAsyncIteration
        
        await asyncio.sleep(1)
        self.current += 1
        return self.current
    
async def main():
    async for val in AsyncCounter(5):
        print(val)

asyncio.run(main())
