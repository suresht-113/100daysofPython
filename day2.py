
# # 🚨 Don't change the code below 👇
# two_digit_number = input("Type a two digit number: ")
# # 🚨 Don't change the code above 👆

# ####################################
# #Write your code below this line 👇
# print(int(two_digit_number[0]) + int(two_digit_number[1]))

#tip calculator
total_bill_amount = input("What is the total bill amount? ")
no_of_users = input("how many person this needs to be split? ")
tip = input("how much tip you would like to pay: 12/15/10? ")
split= round((float(total_bill_amount) + (float(total_bill_amount)*float(tip)/100))/float(no_of_users),2)
print(split)
#https://replit.com/@SureshT3/sureshtip-calculator-start#main.py
# #BMI calculator
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# BMI = int(int(weight)/float(height)**2)
# print(BMI)

# #life in weeks
# # 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# no_years_left = 90 - int(age)
# no_of_days = no_years_left*365
# no_of_weeks= no_years_left*52
# no_of_months = no_years_left*12
# print(f"You have {no_of_days} days, {no_of_weeks} weeks, and {no_of_months} months left.")
