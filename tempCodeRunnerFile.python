import os
with open("Test.txt", "w") as file:
    file.write("Monday: started Python\n")     # write() adds NO line break — you do
    file.write("Tuesday: learned lists\n")

print("File created?", os.path.exists("Test.txt"))

with open("Test.txt", "r") as file:
    everything = file.read()          # one long string, newlines included
print("=== read() gives one big string ===")
print(everything)

with open("Test.txt") as file:       # no mode given, so "r" is assumed
    lines = file.readlines()
print("=== readlines() gives a list ===")
print(lines)

print("=== looping, tidied up with .strip() ===")
with open("Test.txt") as file:
    for number, line in enumerate(file, start=1):
        print(f"{number}. {line.strip()}") 

with open("diary.txt", "a") as file:
    file.write("Wednesday: read a file\n")

with open("diary.txt") as file:
    print("Lines now:", len(file.readlines()))

try:
    with open("missing.txt") as file:
        file.read()
except FileNotFoundError as err:
    print("FileNotFoundError:", err)
os.remove("Test.txt")
print("Cleaned up. Still there?", os.path.exists("Test.txt"))