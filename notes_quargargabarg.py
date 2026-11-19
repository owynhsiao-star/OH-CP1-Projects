def hello(lastame, *firstname):
    for first in firstname:
        print(f"hello {first} {lastame}")
    
    
def hello(name, *args): #For when you are unsure of the number of arguements being takes in, it always gives you a tuple, tuples are not changeable, args are dealing with positional arguements, you know the parameters based on location in list, args must be the last thing in the positional arguements
    for i in args:
        print(args)
        print("Hello", i)
        return #to the slime
hello(1,2,3,4,5,6,7,8,9,0)
hello('g','g','h','j')
def clean(type, data):
    if type == "str":
        return data.strip().lower()
    elif type == "int":
        return int(data)
    elif type == "float":
        return round(float(data), 2)
    elif type == "list":
        return str(f"{x}, " for x in data)
    elif type == "bool":
        return f"{data}"


print(clean("int", "12345"))
print(clean(data="utah", type="str"))#Keyword arguements let you put crap in any order because you're directly telling the code whats what

def clean(**kwargs):#kwargs is like args as it makes it so that I can have as many keyword arguements as I want, kwargs builds a dictionary called kwargs (keyword arguements) then It builts the said dictionary 
    if kwargs["type"] == "str":
        return kwargs["data"].strip().lower()
    elif kwargs["type"] == "int":
        return int(kwargs["data"])
    elif kwargs["type"] == "float":
        return round(float(kwargs["data"]), kwargs["decimals"])
    elif kwargs["type"] == "list":
        return str(f"{x}, " for x in kwargs["data"])
    elif kwargs["type"] == "bool":
        return f"{kwargs["data"]}"
    #in this case the dictionary is 
    #kwargs={
    #    "type":"float",
    #    "data":"3.141596",
    #    "decimals": 3
    #    }


print(clean(data="3.141596", type="float", decimals=3))
def clean(data, decimals=0, **kwargs): #you can set standard values but it has to be before the quargs #Keyword arguements can be paired with psotional arguements but they need to be last #You don't actually have to write kwargs or args, you only need the star and anything becomes args and or kwargs
    if kwargs.get("type") == "str":
        return data.strip().lower()
    elif kwargs.get("type") == "int":
        return int(data)
    elif kwargs.get("type") == "float":
        if kwargs.get("decimals"):
            decimals-kwargs.get("decimals")
        return round(float(data), decimals)
    elif kwargs.get("type") == "list":
        return str(f"{x}, " for x in data)
    elif kwargs.get("type") == "bool":
        return f"{data}"
    else:
        return "No data type given"
print(clean(1,2))




