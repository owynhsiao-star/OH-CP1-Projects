#OH, 1st period, dice roller assignment
import random
while True:
    try:
        while True:
                answer=int(input("what dice would you like: "))
                if answer==4:
                    dice=random.randint(1,answer)    

                    break
                if answer==6:
                    dice=random.randint(1,answer)    

                    break
                if answer==8:
                    dice=random.randint(1,answer)    

                    break
                if answer==10:
                    dice=random.randint(1,answer)    

                    break
                if answer==12:
                    dice=random.randint(1,answer)    
                    break
                if answer==20:
                    dice=random.randint(1,answer)    
                    break
                else:
                    print(f"Please input 4, 6, 8, 10, 12, or 20")
    except:
        print("No characters besides numbers")
    else:
        print("You rolled" , dice)
        break