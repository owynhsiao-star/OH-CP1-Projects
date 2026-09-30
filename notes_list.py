siblingeysiblingey=["Mirai", "Irene", "Vivi"]
#Lists are varuables that contain multiple things, of course, you need to save it
#A list needs brackets [] and each item between the brackets is separated by a comma ,
#Every item must be a proper data type
#Lists are a complex data type
#Lists also have index, each item has it's own index, so Mirai would be 0 irene would be 1 and vivi would be 2
#To print an item from a list you say the name of the variable, then brackets, and then the index number if the thing you wanna print
print(siblingeysiblingey[1])
print(*siblingeysiblingey)
#if you add an * in front of it it prints each item in the variable individually
#This is called unpacking^^^^
print(f"The youngest is {siblingeysiblingey[-1]}")
#- makes it go backwards
length=len(siblingeysiblingey)
#Gets length
siblingeysiblingey.append("Me")
#Adds something to the end of the list
print(*siblingeysiblingey)
siblingeysiblingey.insert(3, "dog")
print(*siblingeysiblingey)
#Adds something ANYWHERE in the list
siblingeysiblingey.extend(["diva", "Kitten", "ripley", "lady"])
#Adds multiple things to ther end
siblingeysiblingey.remove("Me")
#Removes what is in the parenthesis
siblingeysiblingey.pop(2)
#Removes something based on index or the last thing if there is no index given
print(*siblingeysiblingey)


characters=("Kris", "Susie", "Ralsei", "Katti")
#This is a Tuple
print(characters[0])
print(*characters)
#These are the same as lists
'characters.append("Flowery")'
#Doesn't work as Tuples are immutable/unchangable whil lists are mutable and changable
#Tuples are to be used when you don't want a user or other coder to change the items inside of them
#Lists are for when you want the items to be changable
#Both can be duplicated, so you can have the same thing in both of them
#Lists use [], can have duplicates, and is ordered
#Tuples use(), can have duplicates, and is ordered
#Sets use {}, mutable but hates duplicates, unordered
ardenschvarden={"Kartoffel", "Fluegzorg", "Hamburger", "Leibenschirt"}
print(*ardenschvarden)
#Can be unpacked
#Can't be used with index as it has no order and will print in random order if not unpacked
print(len(ardenschvarden))
ardenschvarden.add("Megapurple")
ardenschvarden.update({"Oh yeah", "Ah ah ah, thats not it, no sirree bob"})
ardenschvarden.remove("Oh yeah")
print(*ardenschvarden)
#It's essentially just a not ordered list
wachamacallit=set(siblingeysiblingey)
#You can convert collections between these things
print(wachamacallit)
#They can go inside each other, listseption, a list of lists, tuples, and sets
