#Odd or even
# # 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# if (number%2==0):
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

#BMI 2.0
# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# BMI= round( weight/height**2)
# if BMI < 18.5:
#     print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI < 25 :
#     print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI < 30 :
#     print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI < 35 :
#     print(f"Your BMI is {BMI}, you are obese.")
# else:    
#     print(f"Your BMI is {BMI}, you are clinically obese.")

#Finding a leap year
# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# output = "Not leap year."
# if year % 4 == 0:
#     output = "Leap year."
#     if year % 100 == 0:
#         output = "Not leap year."
#         if year % 400 == 0:
#             output = "Leap year."
# print(output)

# #pizza value calculator
# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# final_bill = 0
# if size== "S":
#     final_bill+=15
# elif size=="M":    
#     final_bill+=20
# elif size=="L":
#     final_bill+=25

# if add_pepperoni=="Y":
#     if size== "S":
#         final_bill+=2
#     else:    
#         final_bill+=3

# if extra_cheese=="Y":
#     final_bill+=1

# print(f"Your final bill is: ${final_bill}.")

#love calculator
# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# name1_lc= name1.lower()
# name2_lc= name2.lower()

# #count of T in names
# count_t= name1_lc.count("t")
# count_t+= name2_lc.count("t")

# #count of T in names
# count_r= name1_lc.count("r")
# count_r+= name2_lc.count("r")

# #count of u in names
# count_u= name1_lc.count("u")
# count_u+= name2_lc.count("u")

# #count of e in names
# count_e= name1_lc.count("e")
# count_e+= name2_lc.count("e")

# #count of l in names
# count_l= name1_lc.count("l")
# count_l+= name2_lc.count("l")

# count_o= name1_lc.count("o")
# count_o+= name2_lc.count("o")

# count_v= name1_lc.count("v")
# count_v+= name2_lc.count("v")

# #first part of output
# count1 = count_t + count_r + count_u + count_e
# count2 = count_l + count_o + count_v + count_e

# Love_meter = int(str(count1) + str(count2))

# if Love_meter < 10 or Love_meter>90:
#     print(f"Your score is {Love_meter}, you go together like coke and mentos.")
# elif Love_meter>40 and Love_meter<50:
#     print(f"Your score is {Love_meter}, you are alright together.")
# else:
#     print(f"Your score is {Love_meter}.")


#day 3 project: treasure island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
 ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 


# #Write your code below this line 👇
# choice = input("Left or right ").lower()
# if choice=="left":
#     choice = input("swim or wait ").lower()
#     if choice=="wait":
#         choice = input("which leftdoor, red/blue/yellow etc ").lower()
#         if choice=="red":
#             print("Burned by fire. Game over")
#         elif choice=="blue":
#             print("Eaten by beasts. Game Over.")
#         elif choice=="yellow":
#             print("You Win!!")
#         else: print("Game over")
#     else: print("game over")
# else: print("game over")

# https://replit.com/@SureshT3/sureshsay-treasur-island-day3?v=1