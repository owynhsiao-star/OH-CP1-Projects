#oh, notes


sentence="The quick brown fox jumps over the lazy dog"

word=input("what word do you want").strip().lower()
new_word=input("what word should be in the sentence").strip().lower()
location=sentence.find(word)
new_sentence=sentence.replace(word,new_word)
print(new_sentence)
print(sentence.find("over"))
#.strip().lower() makes the entire sentence lowercase with no extra whitespace
#.find() find's whetever is in the parenthesis
#.replace() is fairly self explanatory
#.find()finds index of something





firstname=input("what is your name ").strip().title()
lastname=input("what is your last name ").strip().title()
firstseperated=firstname.split()
firstfixed="".join(firstseperated)
lastseperated=lastname.split()
#takes the string and breaks it into two pieces
lastfixed="".join(lastseperated)
fullname=firstfixed.title() + " " +lastfixed.title()
print("Hello " + fullname)

print(fullname.isalpha())
print(fullname.isnumeric())
print(fullname.isupper())
# isalpha makes sure everything is part of the alphabet
# isnumeric checks if its all numbers
# isupper checks for all uppercase
#join joins strings together

#fstring is shortened formatting string and it allows us to more easily control outputs
print(f"Hello world or something {fullname} welcome")
#making something an fstring removes the need for commas and + and such as that

#""" multi line string/comment

letter = input ("give me a letter: ")
letter=letter[0].lower
#[0] takes the index of number in brackets
numbervalue=ord(letter)
#every key on keyboard has numeric value, ord grabs the number value
numbervalue+=2
newletter=chr(numbervalue)
print(f"your letter was {letter} now its {newletter}")
#if you += a letter you can use chr to make it a letter again, according to its new numerical value, so if b is 1 and t is three, and b is letter, letter += 2 is t


