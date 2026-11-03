#OH, period 1, ceaser cypher

alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

whichone=input("Would you like to code or decode a ceaser cypher? ")
if whichone=="Code" or whichone=="code":
    code=list(input("Write you SECRET CODE "))
    for i in code:
        if str.isalpha(i):
            indox=code.index(i)
            code.remove(indox)
            code.insert(indox, )
            alpha[indox]=alpha[indox+1]
            print(alpha[indox])