# Paint required exercise
# #Write your code below this line 👇
# import math
# def paint_calc(height,width,cover):
#     no_of_cans = math.ceil(height*width / cover )
#     print(f"You'll need {no_of_cans} cans of paint")
#     return
# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


#prime number calculation
#Write your code below this line 👇

# def prime_checker(number):
#     divider = 2
#     prime = True
#     while divider < number:
#         if number%divider == 0:
#             prime = False
#             print("It's not a prime number.")
#             return
#         divider +=1 
#     if prime:
#         print("It's a prime number.")
#     return



# #Write your code above this line 👆
    
# #Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)


# ceasar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(texta,shifta):
    textenc=""
    for letter in texta:
        index_of_letter = alphabet.index(letter)
        shiftreq = (index_of_letter + shifta) % 26
        textenc += alphabet[shiftreq]
    print(textenc)
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(textd,shiftd):
    textdec=""
    for letter in textd:
        index_of_letter= alphabet.index(letter)
        shiftreq = (index_of_letter - shiftd)%26
        # if shiftreq <0: shiftreq+=26
        textdec+=alphabet[shiftreq]
    print(textdec)
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
#  Then call the correct function based on that 'drection' variable.
#  You should be able to test the code to encrypt *AND* decrypt a message.

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction=="encode":
        encrypt(text,shift)
    elif direction=="decode":
        decrypt(text,shift)