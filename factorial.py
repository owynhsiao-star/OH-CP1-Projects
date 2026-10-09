#OH, period 1, factorial calculator assignment
import math
def facto(number):
    return math.factorial(number)
while True:
    try:
        numme=int(input("What number do you want? (positive) "))
    except: 
        print("Positive number please                                                                                                                                                                                                                                                                                                                                 ")        
    else:
        break
if numme<0:
    print("Positive number please")
    numme=int(input("What number do you want? (positive) "))
if numme==0:
    print("1")
if numme>0:
    nummer=(math.factorial(map((0,numme))))

    print(nummer[numme-1])