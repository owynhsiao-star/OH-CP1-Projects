#OH, period 1, order up assignment

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
    "Drink":{
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
        print(f"{key}: {i.keys()}")

