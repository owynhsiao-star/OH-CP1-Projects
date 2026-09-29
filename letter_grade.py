# OH, period 1 Grade lettering assignment
while True:
    try:
        grade=float(input("Tell me your grade O child, in decimals please: "))
    except:
        print("Please child of light give me a number (with a decimal) and not this devilspeak")
    else:
        break
if grade == 0:
    print(str("Dost thine teacher even know the name your mother bestowed upon you with the grade of "+str(grade)+"? The F you have?"))
elif grade>0 and not grade>59:
    print("My my child you must pay more attention in the classes you attend to raise that grade from a lowly " +str(grade)+  ", and an F, and you must attend more if I had to guess")
elif grade>59 and not grade>63:
    print("Mine child you have a D- grade, that sucks, why do you have a " +str(grade)+ ".")
elif grade>63 and not grade>66:
    print("A grade of D is nothing above detestable! raise it from a simple 80" +str(grade)+".")
elif grade>66 and not grade>69:
    print("A D+! Surely you jest, no man woman or child should have a " +str(grade)+ ".")
elif grade>69 and not grade>73:
    print("Ah, a C-, it is passing but by no enchantment or meddling should it be as low as a " +str(grade)+".")
elif grade>73 and not grade>76:
    print("A C, one step above barely passing is one step below lackluster! I know you are netter than a " +str(grade) + ".")
elif grade>76 and not grade>79:
    print("I said a C was one step below lackluster, meaning this C+ is lackluster, a mere " +str(grade)+ " is not worthy of you!")
elif grade>79 and not grade>83:
    print("A " +str(grade)+ " and a B-, it is respectable, but should you not strive to raise it further you will dislike what the future holds")
elif grade>83 and not grade>86:
    print("Please work harder my child, a B is simply a sign of potential waiting to be released, you could be so much better than just " +str(grade)+".")
elif grade>86 and not grade>89:
    print("A B+ is just short of th second best grade to be gotten, just a little more than " +str(grade)+ " and you'd have an A.")
elif grade>89 and not grade>93:
    print("An A-. I shall let you pass with a " +str(grade)+".")
elif grade>=100 and grade<=150:
    print("My child, nothing short of perfection I see with an A grade above 100, " +str(grade)+" even.")
elif grade>150:
    print("We does thee lie to me with a grade of \"" +str(grade)+"\"?")
elif grade>93 and not grade>99:
    print('A '+str(grade)+' and an A, very good, this is the optimal grade to aquire')
else:
    print("A positive number, child")