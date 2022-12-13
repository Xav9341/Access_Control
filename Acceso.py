from datetime import datetime
import time

Users =["Maria", "Diana", "Fernando", "Ivan"]
Passwords =["ADA234", "ADA568", "ADA980", "ADA259"]

UserState="Unknown"
PasswordState="Unknown"
UserGeneralState="Unknown"

print(datetime.today())

print("WELCOME TO RIGLINK")
for y in range(5):
    time.sleep(1)
    print("Loading...")


Uentry = input("\nTYPE YOUR USER: ")
for i in Users:
    Pos1 = Users.index(i)
    if Uentry == i:
        UserState="Correct"
        break
    else:
        UserState="Incorrect"

while UserState == "Incorrect":
    print("USER NOT FOUND PLEASE VERIFY")
    Uentry = input("TYPE YOUR USER: ")
    for i in Users:
        Pos1 = Users.index(i)
        if Uentry == i:
            UserState = "Correct"
            break
        else:
            UserState = "Incorrect"

Pentry = input("TYPE YOUR PASSWORD: ")
for ii in Passwords:
    Pos2 = Passwords.index(ii)
    if Pentry == ii:
        PasswordState="Correct"
        break
    else:
        PasswordState="Incorrect"

if Pos1 - Pos2 == 0:
    UserGeneralState="Permited"
else:
    UserGeneralState="Forbidden"

while PasswordState == "Incorrect" or UserGeneralState=="Forbidden":
    print("BAD CREDENTIALS TRY AGAIN OR TYPE >Exit< TO QUIT THE PROGRAM")
    Pentry = input("TYPE YOUR PASSWORD: ")
    for ii in Passwords:
        Pos2 = Passwords.index(ii)
        if Pentry == ii:
            PasswordState = "Correct"
            break
        else:
            PasswordState = "Incorrect"
    if Pos1 - Pos2 == 0:
        UserGeneralState = "Permited"
    else:
        UserGeneralState = "Forbidden"
        if Pentry == "Exit":
            print("Bye...")
            quit()

if UserGeneralState == "Permited":
    time.sleep(5)
    print("\nAccess Sucessfully")
    print("\nSession starts at: ", datetime.today().strftime('%A, %B %d, %Y %H:%M:%S'))
    time.sleep(3)
    print("\nWelcome",i)