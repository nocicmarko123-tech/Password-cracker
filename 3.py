import time
import pathlib
import random

password = input("Enter the password to crack: ")
start = time.time()

def banana( start, end, descripted):
    descripted = descripted.rstrip()
    print("Password cracked. Password is: " + descripted)
    print("Time for cracking: " + str(round(time.time() - start)))       

def type_password(password):
    if password.isalnum():
        if password.islower():
            characters = "abcdefghijklmnopqrstuvwxyz" + "0123456789"
        elif password.isupper():
            characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "0123456789"
    elif password.isalpha():
        if password.islower():
            characters = "abcdefghijklmnopqrstuvwxyz"
        elif password.isupper():
            characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif password.isdigit():
        characters = "0123456789"
    elif password.isspace():
        for i in range(18):
            character = " "
            if character == password:
                end = time.time()
                banana(start, end, password)
                break
            else:
                character += " "
    else:
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:',.<>?/`~ "
    return characters

def lofp(password):
    lenght = len(password)
    return lenght

characters = type_password(password)
lenght = lofp(password)

class Ai:
    def __init__(self, characters, password):
        self.characters = characters
        self.password = password
    
    def crack_password(self, characters, password):
        attempt = ""
        for i in range(len(characters)):
            letter = random.choice(characters)
            attempt += letter
            if attempt == password:
                end = time.time()
                banana(start, end, password)
                break
            else:
                for i in range(len(characters)):
                    letter = random.choice(characters)
                    attempt += letter
                    if attempt == password:
                        end = time.time()
                        banana(start, end, password)
                        break
                    else:
                        for i in range(len(characters)):
