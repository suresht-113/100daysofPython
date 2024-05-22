# hangman project
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word= random.choice(word_list).lower()

#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = list()
for i in range(len(chosen_word)):
    display.append("_")

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
end_of_game = False
lives = 6
while not end_of_game:
    print(display)
    print(stages[lives])
    guess = input("please guess a letter").lower()

#TLoop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

    counter = 0
    for i in chosen_word:
        if i == guess: 
            display[counter]= i
        counter+=1
    
    if guess not in display:
        lives-=1
    if "_" not in display:
        end_of_game= True
        print(f'You wun!!, the Word is {chosen_word}.')
    elif lives==0:
        end_of_game= True
        print(stages[lives])
        print(f'Pssst, the solution is {chosen_word}.')
# https://replit.com/@SureshT3/sureshtHangman?v=1