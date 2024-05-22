# #generating random numbers
# import random	 
# # 🚨 Don't change the code below 👇
# # test_seed = int(input("Create a seed number: "))
# # random.seed(test_seed)
#  # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
# #Write the rest of your code below this line 👇
# random_int = random.randint(0,1)
# if random_int==0:
#     print("Tails")
# else:
#     print("Heads")

# # Banker Roulette
# import random
# # 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# length = len(names)
# random_integer = random.randint(0,length-1)
# print(f"{names[random_integer]} is going to buy the meal today!")

# 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# column = int(position[0])
# row= int(position[1])
# map[row-1][column-1] = "X"
# print(f"{row1}\n{row2}\n{row3}")

# Rock paper scissors game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
test_seed = 5
mylist = [rock,paper,scissors]
mychoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
Computer_choice=  random.randint(0,2)

if mychoice >= 3 or mychoice < 0: 
    result ="You typed an invalid number, you lose!"
elif (Computer_choice==mychoice):
    result="Draw"
elif mychoice==0 and Computer_choice == 1:
    result="You Lose!!"
elif mychoice==0 and Computer_choice == 2:
    result="You Win!!"
elif mychoice == 1 and Computer_choice == 2:
    result="You Lose!!"
elif mychoice == 1 and Computer_choice == 0:
    result="You Win!!"
elif mychoice == 2 and Computer_choice == 0:
    result="You Lose!!"
elif mychoice == 2 and Computer_choice == 1:
    result="You Win"

print(mylist[mychoice])
print(mylist[Computer_choice])
print(result)
# https://replit.com/@SureshT3/sureshtrock-paper-scissor?v=1
# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!") 
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")