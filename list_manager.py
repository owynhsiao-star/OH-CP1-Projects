# OH period 1 Shopping List Manager

shoplist=["Eggs", "hydrocortisol", "milk", "five guys sign"]
while True:
    action = input("What would you like to do? (add, remove, view, exit) ")
    if action=="add":
        listnew=input("What would you like to add to the shopping list? ")
        shoplist.append(listnew)
        print(*shoplist)
    elif action=="remove":
        print(*shoplist)
        removal=input("What do you wanna remove? ")
        shoplist.remove(removal)
        print(*shoplist)
    elif action=="view":
        print(*shoplist)
    elif action==exit:
        print("Have a nice trip to walmart")
