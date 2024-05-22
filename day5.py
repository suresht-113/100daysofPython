# # 🚨 Don't change the code below 👇
#below code is done to perform for loop understanding
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆

# sum_of_height = int()
# no_of_students = 0
# #Write your code below this row 👇
# for n in student_heights:
#     sum_of_height += n
#     no_of_students += 1
# average_height= round(sum_of_height/no_of_students)
# print(average_height)

# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# max_value = 0
# for score in student_scores:
#     if score> max_value:
#         max_value= score
# print(f"The highest score in the class is: {max_value}")

#Write your code below this row 👇
#adding only even numbers
# sum_of_even= int()
# for i in range(1,101):
#     if i % 2 ==0:
#         sum_of_even += i
# print(sum_of_even)

#write code for fizz buzz logic
# for i in range(1,101):
#     if i % 3 == 0 and i % 5==0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else: print(i)

#password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = str()

#easy level
for i in range(0,nr_letters):
    password += random.choice(letters)
for i in range(0,nr_symbols):
    password += random.choice(symbols)
for i in range(0,nr_numbers):
    password += random.choice(numbers)
print(password)

#hard level
passwordlist = []
for i in range(0,nr_letters):
    passwordlist += random.choice(letters)
for i in range(0,nr_symbols):
    passwordlist += random.choice(symbols)
for i in range(0,nr_numbers):
    passwordlist += random.choice(numbers)
random.shuffle(passwordlist)
password=""
for i in passwordlist:
    password+=i
print(password)
#https://replit.com/@SureshT3/sureshtpasswordgenerator?v=1