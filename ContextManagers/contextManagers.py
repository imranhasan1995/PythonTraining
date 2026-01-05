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
        self.file = open(self.filename, self.mode)
        print("Entering the context")
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Exiting the context")
        self.file.close()

with FileManager(file_path, 'r') as f:
    f.read()
    print("Reading file content...")