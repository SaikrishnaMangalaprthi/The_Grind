
with open("Test.txt", "a") as file:
    file.write("New log entry\\n")

with open("Test.txt", "r") as file:
    print(file.read())