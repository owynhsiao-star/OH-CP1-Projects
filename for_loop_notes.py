#Bugelstrudel
import time

#iteration is every item in a list or collection in general
bugelstrudel=["cat", "dog", "rat", "mouse"]
for bugelstrudelo in bugelstrudel:
#For is the keyword for for loops
#Bugelstrudelo is the iterator variable which is essentially a singular version of items in lists instead of the entire list
#in lets you tell the program that it's in a certain list by stating the list name after in
    if bugelstrudelo== "cat":
        bugelstrudelo=579345
        print(f"How animal you {bugelstrudelo}")
hundreds=[6, 12, 18, 24, 30, 36]
average=0
for hundred in hundreds:
    average += hundred
    print(f"{hundred} was added")

average=average/len(hundreds)
print(F"The average hundred is {average:.2f}")
for i in range(2,21,2):
    print(i)
    time.sleep(.000001)
for i in range(1,90000000000000000000,1):
    print(i)
    time.sleep(.00000001)
    if i==90000000000:
        print("WAIT, PLEASE WAIT")
        break