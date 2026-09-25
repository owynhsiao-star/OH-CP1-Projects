#OH, period 1, usersignin assignment
username="Micheal Jordan"
pasword="Beegee"
ask=input("What is you username? ")
aske=input("What is you password? ")
if ask==username:
    print("Username is correct")
else:
    print("Ah ah ah, thats not it, no siree bob")
if aske==pasword:
    print("Password is correct")
else:
    print("Learn your own password")
if ask==username and aske == pasword:
    print("Welcome to the program " + username+"!")
else:
    print("NOT welcome")


