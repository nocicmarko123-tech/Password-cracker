import time

def banana(start, end, descripted):
        descripted = descripted.rstrip()
        print("Password cracked. Password is: " + descripted)
        print("Time for cracking: " + str(round(time.time() - start)))

password = input("Enter the password to crack: ")  
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:',.<>?/`~"
attempt = 0
start = time.time()
descripted = ""

while True:
    for j in characters:
        attempt += 1
        if j == str(password):
            end = time.time()
            banana(start, end, descripted)
            print("Total attempts: " + str(attempt))
            break
        if j == password(attempt -1):
            descripted += j
