from contextlib import contextmanager
from typing import Generator, IO, Any

@contextmanager
def file_manager(file_path: str, mode: str) -> Generator[IO, Any, None]:
    file: IO = open(file_path, mode)
    print("Opening file")
    try:
        yield file
    # the execution will continue from here after returning from with
        print("execution started...")
    except Exception as e:
        print(e)
    finally:
        print("Closing file")
        if file:
            file.close()

with file_manager("example.txt", "r") as f:
    #raise Exception("file error")
    #f.write("Hello World")
    print(f.read())

