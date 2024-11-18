import random
import time
import string

print("Program started \n ")
time.sleep(0.5) 
print("Initializing variables \n")
Password_massive = []
password = str
lenght = int
iterations = int
time.sleep(0.5)
print("Password generator v 0.1 \n")
time.sleep(0.5)
print("Do you want to generate password? \n")
time.sleep(0.5)

answer = input("y/n: ")
if answer == "y":
    print("Program initialized \n")
else:
    print("And why you open password generator if u don't want to? \n")
    time.sleep(0.5)
    exit()
print("Choose lenght of password \n")
lenght = int(input("Lenght of password: \n"))
time.sleep(0.5)
iterations = int(input("How many times do you want to generate password: \n"))
time.sleep(0.5)

def password_generator(lenght):
    password = ""
    print("Generating password \n")
    while len(password) < lenght:
        password += random.choice(string.ascii_letters)
    return password

def main(iterations):
    while iterations > 0:
        password = password_generator(lenght)
        print("Your password is: ", password)
        Password_massive.append(password)
        iterations -= 1
        time.sleep(0.2)
    print("would you like to save it to file? \n")
    time.sleep(0.5)
    answer = input("y/n: ")
    if answer == "y":
        save_to_file(Password_massive)
    else:
        print("Program finished \n")
        time.sleep(0.5)
        
def save_to_file(Password_massive):
    print("Save it to file \n")
    time.sleep(0.5)
    file = open("password.txt", "w")
    for password in Password_massive:
        file.write(password + "\n")
    file.close()
    print("Password saved \n")
    time.sleep(0.5)
    print("Program finished \n")
    time.sleep(0.5)

main(iterations)