# START PROGRAM

# Create alphabet string

# FUNCTION encrypt(message, shift):
#     create empty result string
#     loop through each character in message:
#         if character is a letter:
#             find its position in alphabet
#             shift position forward
#             wrap around if needed
#             add new letter to result
#         else:
#             keep character the same
#     return result

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