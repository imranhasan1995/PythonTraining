file_path = "D:/pythonProjects/pythonFundamentals/fundamentalsvenv/PythonTraining/classes.py"

with open(file_path) as f:
    data = f.read()
    #print(data)

### custom context manager ###

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        
    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            print("Entering the context")
            return self.file
        except FileNotFoundError:
            print(f"Error: The file '{self.filename}' was not found.")
        except IOError as e:
            print(f"Error opening file '{self.filename}': {e}")
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print("Exiting the context")
        
        if exc_type:
            # Handle exceptions occurring inside the block
            print(f"An exception occurred: {exc_type.__name__}: {exc_value}")

with FileManager(file_path, 'r') as f:
    f.read()
    print("Reading file content...")