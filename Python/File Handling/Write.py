with open("Test.txt","w") as file:
    file.write("Hello World! \n")
    file.write("Second Line \n")
    

with open("Test.txt","r") as file:
    print(file.read())