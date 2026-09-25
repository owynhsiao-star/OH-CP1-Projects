#OH, period 1, usersignin assignment
username="I'm groovy and never glooby"
pasword="Beegee"
ask=input("What is you username? ")
aske=input("What is you password? ")
if ask==username:
    proceedings=True
    print("Username is correct")
else:
    print("Ah ah ah, thats not it, no siree bob")
if aske==pasword:
    proceedenings=True
    print("Password is correct")
else:
    print("Learn your own password")
if bool(proceedings)==True and bool(proceedenings)==True:
    print("Welcome " + username)
else:
    print("NOT welcome")


