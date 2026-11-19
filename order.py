#OH, period 1, order up assignment
endloop=False
value=0
foods={
    "Main":{
        "Burger": 3.00,
        "Steak": 5.00,
        "Fifty five fig flavored fat fried shrimp": 55.00,
        "Oh boy hot dog": 1.50,
        "wednesday": 2.00,
        'Oh and I guess theres pizza': 9.00
    },
    "Side":{
        "The one on the left": 1.11,
        "The other one on the left": 1.22,
        "A little more to the right": 3.00,
        "No not that one the other one": 17.00
    },
    'Drink':{
        "Beverage":15.00,
        "Vanilla extract":3.00,
        "Who drinks vanilla extract?":4.00,
        "Flavor propaganda":0.01
    }
}
thelisty=list(foods.keys())
for i in thelisty:
    print(i, end="\n--------------------------------\n")
    thelistylisty=list(foods[i].keys())
    for key in thelistylisty:
        print(f"{key}: {foods[i][key]}")
while True:
    if endloop==True:
        break
    dorder=input("What drink do you want: ").capitalize()
    morder=input("What would you like as your main dish: ").capitalize()
    sorder=input("What would you like as a side: ").capitalize()
    sorder2=input("What would you like as a side (the sequel): ")
    for i in thelisty:
        thelistylisty=list(foods[i].keys())
        for key in thelistylisty:
            if dorder==key or morder==key or sorder==key or sorder2==key:
                value+=foods[i][key]
                endloop=True
            else:
                break
        break
    print("Please order things on the menu")
print (morder, ", ", dorder, ", ", sorder, ", ", sorder2, ", ", value, " Dollars")

        