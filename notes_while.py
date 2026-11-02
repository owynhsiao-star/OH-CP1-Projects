#While loops continue repeating until a condition is met
import random
import time
goose=random.randint(1,20)
duck=1
#Duck is the start point, takes place outside of the loop
while goose>duck:
    #while is of course the keyword for a while loop
    # the boolean after while is the end point, once it is false, the while loop ends
    print("duck",duck)
    time.sleep(.1)
    duck+=1
    #duck+=1 is the incrementer
    #Incrementers are used to change the iterator
    #Iterator keeps track of current iteration of the loop
    #Removing the incrementer makes the loop infinite
    if duck==15:
        print("Gameover")
        break
else: #If you break out of a loop it wont do the else after it because the loop becoming false automatically activates and else that isn't written
    print("AHHH, AHHH, I\'M BURNING, AHHH, I NEED TYLENOL")

#simpler loop
count=1
while count<=3:
    print(count)
    time.sleep(.0000001,)
    count+=1
    

number=random.randint(1,101)
#while True:
#    while True:
#        try:
#            guess=int(input('Number between 1 and 100'))
#            if guess==number:
#                print("YAHAH, YAHAHAHAH, YAHAHA")
#                continue
#            break
#        except: 
##            print("A NUMBER")
#     guess>number:
#        print("lower")
#        guess=int(input('Number between 1 and 100'))
#    elif guess<number:
#        print("Higher")
#        guess=int(input('Number between 1 and 100'))
#    else:
#        print("What number did you enter????????")
#        guess=int(input('Number between 1 and 100'))
            