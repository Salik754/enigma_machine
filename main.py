"""
Caesar Cipher Program
Encrypts and decrypts messages using a shift value.
"""

# Alphabet used for shifting
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Function to encrypt a message
def encrypt(message, shift):
    result = ""# creates an empty result string


    for char in message: # loop through each character in message
        if char in alphabet: # if character is a letter
            index = alphabet.index(char)  # find position
            new_index = (index + shift) % 26  # shift forward + wrap around
            result += alphabet[new_index] # add new letter to result
        else:
            result += char  # keep spaces/punctuation

    return result

# Function to decrypt a message
def decrypt(message, shift):
    result = ""

    for char in message:# creates an empty result string
        if char in alphabet: # loop through each character 
            index = alphabet.index(char) # find position   
            new_index = (index - shift) % 26  # shift backward + wrap around
            result += alphabet[new_index] # add new letter to result
        else:
            result += char # keep spaces/punctuations

    return result

#     loop through each character:
#         if character is a letter:
#             find position
#             shift backward
#             wrap around
#             add new letter
#         else:
#             keep character the same
#     return result

# FUNCTION get_choice():
#     ask user for "e" or "d"
#     validate input
#     return choice
# Function to get valid choice
def get_choice():
    while True:
        choice = input("Encrypt or Decrypt? (e/d): ").strip().lower()
        if choice == "e" or choice == "d": # ask the user for "e" or "d"
            return choice # return the valid choice, also stops the loop
        else:
            print("Invalid input. Enter 'e' or 'd'.") #if the choice is invalid, print this message



# MAIN:
#     greet user
#     loop forever:
#         get choice
#         get message
#         clean message
#         get shift number
#         if choice is "e":
#             call encrypt
#         else:
#             call decrypt
#         display result
#         ask if user wants to continue
#         if no:
#             exit loop

# END PROGRAM