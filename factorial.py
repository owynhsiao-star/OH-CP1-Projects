#OH, period 1, factorial calculator assignment
import math
def facto(number):
    return math.factorial(number)
while True:
    try:
        numme=int(input("What number do you want? (positive) "))
    except: 
        print("Number please")        
    else:
        break
if numme==0:
    print("1")
elif numme<0:
    print("Positive number please")
    numme=int(input("What number do you want? (positive) "))
if numme>0:
    nummeral=(0, numme)
    nummer=list(map(math.factorial, nummeral))
    for num in range(1,numme+1):
        if num<numme:
            print(num, end="*")
        if num==numme:
            print(num, end="=")
    print(nummer[1])
   