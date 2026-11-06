#OH, period 1, ceaser cypher

alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

whichone=input("Would you like to code or decode a ceaser cypher? ").title()
valienter=int(input("How far would you like to shift the number: "))
puserkayut=list(input("What is your code you wanna code with a code? "))

if whichone=="Code":
    def cypher(userkaput):
        userkaput=list(userkaput)
        for i in userkaput:
            numbervali=ord(i)
            nunumvali=numbervali+valienter
            if nunumvali>114:
                nunumvali-=114
                break
            charvali=chr(nunumvali)
            idex=userkaput.index(i)
            userkaput.insert(idex+1, charvali)
            userkaput.remove(i)
        print(*userkaput)
        return userkaput


cypher(puserkayut)
