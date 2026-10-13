#OH, period 1,Escape room (text based)
code=8105
guessnum=0
while guessnum<=3:
    guess=input("There is a code, it is a number between 1 and 10000 what is the code? ")
    if guess==code:
        win=True
    if not guess==code:
        win=False
        guessnum+=guessnum+1
        if guessnum==1:
            print("first hint: There is a sticky note next to you, the sticky note has a question on it. \"How many sides do I have?\" (All senses of side)")
        if guessnum==2:
            print("There were 3 castles, each castle has 3 royal families, each royal family had three children, one day, another child arrived from the forest and he was taken into one of the castles, but the child was cursed, not by a witch or a warlock but by a man, a  horrible man, and one day all the children, and the husbands and wives, walked into a dark room, an empty room, a room without a man, a man who wasn't looking at something, who didn't look like he knew something, and then they left, the castle, it's families, and its children, how many children are there?")
        if guessnum==3:
            print("")
        if win==True:
            print("Congrats!")
        break
else:
    print("You lose")
            

