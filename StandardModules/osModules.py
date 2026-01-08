import os
dir = os.getcwd()
print(dir)

file_path = dir + "/example.txt"

if os.path.isfile(file_path):
    with open(file_path) as f:
        print(f.read())
else:
    print("File not found")
