#OH, period 1, ceaser cypher

while True:
    whichone = input("Would you like to Encode or decode a ceaser cypher? ").title()
    while True:
        try:
            shift = int(input("How far would you like to shift the number: "))
        except:
            print("A number")
        else:
            break
    code1 = list(input("What is your code you wanna code with a code? "))

    if whichone == "Encode":
        def cypher(cy):
            encodedchars = []
            for i in cy:
                numv = ord(i)
                numv2 = numv + shift
                if numv2 > 122: 
                    numv2 = 97 + ((numv2 - 97) % 26)
                charr = chr(numv2)
                encodedchars.append(charr)
            print(*encodedchars)

        cypher(code1)
    if whichone == "Decode":
        def cypher(cy):
            encodedchars = []
            for i in cy:
                numv = ord(i)
                numv2 = numv - shift
                if numv2 < 97:
                    numv2 = 122 - ((121 - numv2) % 26)
                charr = chr(numv2)
                encodedchars.append(charr)
            print("".join(encodedchars))
        cypher(code1)
    elif whichone=="Done":
        break
    else:
        print("Encode, Decode, or Done")