import time

def banana(start, end, descripted, attempt):
        descripted = descripted.rstrip()
        print("Password cracked. Password is: " + descripted)
        print("Time for cracking: " + str(end - start))
        print("Total attempts: " + str(attempt))

password = input("Enter the password to crack: ")  
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:',.<>?/`~" + " "
attempt = 0
start = time.time()
descripted = ""
path = 0

for i in range(len(password)):
    for j in characters:
        attempt += 1
        if descripted == password:
            end = time.time()
            banana(start, end, descripted, attempt)
            break
        elif j == password[path]:
            descripted += j
            path += 1
