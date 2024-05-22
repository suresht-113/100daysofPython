# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades ={}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for stu in student_scores:
#     if student_scores[stu]>=91:
#         student_grades[stu] = "Outstanding"
#     elif student_scores[stu]>=81:
#         student_grades[stu] = "Exceeds Expectations"
#     elif student_scores[stu]>=71:
#         student_grades[stu] = "Acceptable"
#     elif student_scores[stu]<=70:
#         student_grades[stu] = "Fail"
    
# # 🚨 Don't change the code below 👇
# print(student_grades)

# nested dictionaries
# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(f_country, f_visits, f_cities):
#     new_country={}
#     new_country["Country"]= f_country
#     new_country["visits"]= f_visits
#     new_country["cities"]= f_cities
#     travel_log.append(new_country)
#     return

# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


from os import system, name

def clear():
   # for windows
   if name == 'nt':
       _ = system('cls')

   # for mac and linux
   else:
       _ = system('clear')

def winner(f_bids):
    highest_bid=0
    highest_bidder=""
    for users in f_bids:
        if f_bids[users] > highest_bid:
            highest_bid = f_bids[users]
            highest_bidder = users
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")    
    return
    
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''' 
exit = True
Bids ={}
while(exit):
    print(logo)
    print("Welcome to the secret auction program")
    user = input("What is your name?: ")
    bid = int(input("What is your bid?: " ))
    Bids[user] = bid
    more_bid = input("Are there more bidders? Type 'Yes' or 'No'. ")
    if more_bid == 'No':
        winner(Bids)
        exit = False
    else: 
        clear()
