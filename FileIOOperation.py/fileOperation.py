# open file in write mode
file = open("Example.txt", "w")
file.write("File opened in write mode.\n")
file.write("second line.")
file.close()

# read file
file = open("Example.txt", "r")
print(file.read())
file.close()

# readLine
file = open("Example.txt", "r")
line = file.readline()
while line:
    print(line, end='')
    line = file.readline()
file.close()


# write lines
lines = ["First line\n", "Second line\n", "Third line\n"]
with open("example.txt", "w") as file:
    file.writelines(lines)
    print("Content added Successfully!!")

# readLines
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
