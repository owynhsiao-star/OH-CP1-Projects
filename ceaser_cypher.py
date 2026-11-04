#OH, period 1, ceaser cypher

alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

whichone=input("Would you like to code or decode a ceaser cypher? ").title()

if whichone=="Code":
    puserkayut=list(input("What is your code you wanna code with a code?"))
    
def cypher(userkaput):
    """this cyphers the code"""
    for i in userkaput:
        userkaput=list(userkaput)
        wachamacallit=alpha.index(i)
        userkaput.remove(i)
        userkaput.insert(alpha[wachamacallit+1])
        print (userkaput)
        return userkaput

cypher(puserkayut)
