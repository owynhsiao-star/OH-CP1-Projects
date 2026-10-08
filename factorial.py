#OH, period 1, factorial calculator assignment
import math
def facto(number):
    return math.factorial(number)
while True:
    try:
        numme=int(input("What number do you want? (positive) "))
    except: 
        print("Positive number please")        
    else:
        break
if numme<0:
    print("Positive number please")
    numme=int(input("What number do you want? (positive) "))
if numme==0:
    print("1")
if numme>0:
    numme2=range(1,(numme+1)) 
    for num in range(1, numme+1):
        print(num, end=" ")
numme2=map(facto, numme)
print(list(numme2))