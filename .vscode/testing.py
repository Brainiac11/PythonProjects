import os
import sys
import base64
import string
import random
from cryptography.fernet import Fernet

password_characters = string.ascii_letters + string.digits + string.punctuation
choices = ['1', '2', '3']
print("Welcome to the Password Generator")
print("this program will generate a password for you")
print("It will also store your passwords in a file for you")
print("The file name will be Passwords.txt")
print("It will be encrypted, so you will need to enter your password to decrypt it")
input("Press enter to continue")
print("type 1 to generate a password, type 2 to view your passwords, type 3 to exit")
mode_of_use = input("")
try:
    if mode_of_use in choices:
        pass #cool code
    else:
        raise ValueError
except ValueError:
    print("Please type out 1, 2, or 3")
    exit()
if mode_of_use == '1':
    print("You have chosen to generate a password")
    site = input("Please enter the site this password is for: ")
    print("Please enter the length of the password")
    length = input("")
    try:
        length = int(length)
        if length > 0:
            pass #to pass the test
        else:
            raise ValueError
    except ValueError:
        print("Please enter a natural number")
        exit()
    length = int(length)
    password = "".join(password_characters[ord(random.SystemRandom().choice(password_characters)) % len(password_characters)] for _ in range(length))
    print("Your password is: " + password)
    password = 'Passwords.txt'
    key = Fernet.generate_key()
    key = str(key)
    with open (password, 'w') as f:
        f.write(key)
        # opening the key
    with open(password, 'rb') as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # opening the original file to encrypt
    with open(password, 'rb') as file:
        original = file.read()
        
    # encrypting the file
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and
    # writing the encrypted data
    with open(password, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    with open (password, "a") as file:
        file.write(site + ' ' + ':' + ' ' + password + "\n")
        file.close()
    print("Your password has been stored in Passwords.txt")
    exit()
    
    
