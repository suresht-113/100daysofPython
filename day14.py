from art import logo_hl
from art import vs
from gamedata import data
import random
from os import system, name

def clear():
   # for windows
   if name == 'nt':
       _ = system('cls')

   # for mac and linux
   else:
       _ = system('clear')

def fetch_data():
    selected= random.choice(data)
    choice_str=" "
    for i in selected:
        if i != 'follower_count':
            choice_str += selected[i]
            choice_str += ', '
        else:
            count= selected[i]  
    returnlist=[choice_str, count]
    return returnlist

def compare(inp1, inp2, inp3):
    if inp1 > inp2 and inp3=='A':
        return True
    elif inp2 > inp1 and inp3=='B':
        return True
    else: return False

def game():
    print(logo_hl)
    compare_a = fetch_data()
    streak = True
    counter=0
    while streak: 
        compare_b = fetch_data()
        print(f"Compare A: {compare_a[0]}")
        print(vs)
        print(f"Against B: {compare_b[0]}")
        selected = input("Who has more followers? Type 'A' or 'B': ")
        result = compare(compare_a[1], compare_b[1],selected)
        clear()
        print(logo_hl)
        if result:
            counter+=1
            compare_a= compare_b
            print(f"You are right! Current score: {counter}.")
        else:
            print(f"Sorry, that's wrong. Final score {counter}.")
            streak=False
game()
    

# Tutor code
# from gamedata import data
# import random
# from art import logo, vs
# from replit import clear

# def get_random_account():
#   """Get data from random account"""
#   return random.choice(data)

# def format_data(account):
#   """Format account into printable format: name, description and country"""
#   name = account["name"]
#   description = account["description"]
#   country = account["country"]
#   # print(f'{name}: {account["follower_count"]}')
#   return f"{name}, a {description}, from {country}"

# def check_answer(guess, a_followers, b_followers):
#   """Checks followers against user's guess 
#   and returns True if they got it right.
#   Or False if they got it wrong.""" 
#   if a_followers > b_followers:
#     return guess == "a"
#   else:
#     return guess == "b"


# def game():
#   print(logo)
#   score = 0
#   game_should_continue = True
#   account_a = get_random_account()
#   account_b = get_random_account()

#   while game_should_continue:
#     account_a = account_b
#     account_b = get_random_account()

#     while account_a == account_b:
#       account_b = get_random_account()

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}.")
    
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     clear()
#     print(logo)
#     if is_correct:
#       score += 1
#       print(f"You're right! Current score: {score}.")
#     else:
#       game_should_continue = False
#       print(f"Sorry, that's wrong. Final score: {score}")

# game()
