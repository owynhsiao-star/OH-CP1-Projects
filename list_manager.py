# OH period 1 Shopping List Manager

shoplist=["Eggs", "Hydrocortisol", "Milk", "\"Five guys sign\""]
while True:
    action = input("What would you like to do? (add, remove, view, exit) ").strip().capitalize()
    if action=="Add":
        listnew=input("What would you like to add to the shopping list? ").capitalize()
        shoplist.append(listnew)
        print(*shoplist)
    elif action=="Remove":
        print(*shoplist)
        removal=input("What do you wanna remove? ").capitalize()
        while True:
            if removal in shoplist:
                shoplist.remove(removal)
                print(*shoplist)
                break
            else:
                print("Please input something in the list")
                removal=input("What do you wanna remove? ").capitalize()
    elif action=="View":
        print(*shoplist)
    elif action=="Exit":       
        break
    else: 
        print("Please input one of the predetermined options")
        action=input("What would you like to do? (add, remove, view, exit)").strip().capitalize
print("Have a nice trip to walmart")
    