import os
os.chdir('C:/Users/stejaram/Downloads/100daysofPython/Day24')
file = open("my_file.txt" , "r")
contents= file.read()
file.close()

with open("my_file.txt" , "a") as file:
    file.write("new test")