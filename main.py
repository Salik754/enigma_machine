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


# Function to get valid choice
def get_choice():
    while True:
        choice = input("Encrypt or Decrypt? (e/d): ").strip().lower()
        if choice == "e" or choice == "d": # ask the user for "e" or "d"
            return choice # return the valid choice, also stops the loop
        else:
            print("Invalid input. Enter 'e' or 'd'.") #if the choice is invalid, print this message



# Main program
def main():
    print("Welcome to the Caesar Cipher Program!\n")

    while True:
        choice = get_choice()
        message = input("Enter your message: ").strip().lower()
        
         # validate shift
        while True:
            try:
                shift = int(input("Enter shift number: ").strip())
                break
            except ValueError:
                print("Please enter a valid number.")

        if choice == "e":
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        else:
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")

        again = input("Run again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break
# Run program
if __name__ == "__main__":
    main()