import asyncio

class AsyncFileManager:
    def __init__(self, filename, mode, message):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.message = message

    async def __aenter__(self):
        print(f"Opening file asynchronously for {self.message}")
        await asyncio.sleep(1)  # simulate async I/O
        self.file = open(self.filename, self.mode)
        return self.file

    async def __aexit__(self, exc_type, exc, tb):
        print("Closing file asynchronously")
        await asyncio.sleep(1)
        if self.file:
            self.file.close()

        if exc:
            print("Exception occurred:", exc)

        return False  # do NOT suppress exceptions
    

async def main():
    async with AsyncFileManager("temp.txt", "w", "Writting") as f:
        f.write("Hello World.")
    async with AsyncFileManager("temp.txt", "r", "Reading") as f:
        print(f'file content: {f.read()}')

asyncio.run(main())
