#OH, period 1, order up assignment
endloop=False
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
        value=foods[i][key]
        print(value)
while True:
    dorder=input("What drink do you want: ")
    morder=input("What would you like as your main dish: ")
    sorder=input("What would you like as a side: ")
    if endloop==True:
        break
    for i in thelistylisty:
        if dorder==i:
            dorder=foods[i][key] #Figure out how to make this not screw up
            endloop=True
        else:
            print("Please order things that are on the menu")