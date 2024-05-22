# # Functions with output
# def format_name(fname, lname):
#     fname.title()
#     lname.title()

# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(fyear, fmonth):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
#     days= month_days[fmonth-1]
#     if is_leap(fyear) and fmonth == 2:
#         days+=1
#     return days
  
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

import art

# calculator
def add(n1,n2):
    return n1+n2
def mult(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def sub(n1,n2):
    return n1-n2

operations ={
    "+":add, 
    "-":sub, 
    "*":mult, 
    "/":divide
    }
def calculator():
    print(art.logo_calc)
    num1 = int(input("What's the first number?: "))
    exit = False
    while not exit:    
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation from the line above: ")
        num2 = int(input("What's the next number?: "))
        calculation_fun = operations[operation]
        answer = calculation_fun(num1,num2)
        print(f"{num1} {operation} {num2} = {answer}")
        option = input("Do you want to continue with previous answer? y or n:")
        if option == "y":
            num1 = answer
        elif option =="n":
            exit = True

calculator()