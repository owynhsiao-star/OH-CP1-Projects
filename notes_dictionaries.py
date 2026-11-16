#A dictionary is a collection of key and value pairs
dictionary={
    "make": "jeep",
    "model": "Wrangler",
    "color": "red",
    "year": 2023
    #key : value, cannot use booleans as keys
}

print(dictionary["make"]) #This is how I'd get a certain value in the dictionary
print(dictionary.keys()) #This is how you get the keys in a dictionary, you can do the same with values and len will give you the number of key and value pairs
if "transmission" in dictionary:
    print(dictionary["transmission"])
else: 
    dictionary["transmission"]="automatic"
    print(dictionary.items())#Prints it all as tuples
keys=list(dictionary.keys())
for key in keys:
    print(f"{key} is {dictionary[key]}")
numbers={ #This is putting dictionaries in dictionaries
    1:{
        "n":1.1,
        "e":1.2,
        "r":1.3,
    },
    2:{
        "y":2.1,
        "p":2.2,
        "g":2.3,
    }
}
print (numbers[1]["n"]) #This is how you call an item in a dictionary in a dictionary
print (numbers.get(1).get("o")) #This makes sure your code does screw up when you ask for something that doesn't exist