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
# FUNCTION decrypt(message, shift):
#     create empty result string
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