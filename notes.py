#oh, notes


sentence="The quick brown fox jumps over the lazy dog"

word=input("what word do you want").strip().lower()
new_word=input("what word should be in the sentence").strip().lower()
location=sentence.find(word)
new_sentence=sentence.replace(word,new_word)
print(new_sentence)
print(sentence.find("over"))















firstname=input("what is your name ").strip().title()
lastname=input("what is your last name ").strip().title()
firstseperated=firstname.split()
firstfixed="".join(firstseperated)
lastseperated=lastname.split()
lastfixed="".join(lastseperated)
fullname=firstfixed.title() + " " +lastfixed.title()
print("Hello " + fullname)

print(fullname.isalpha())
print(fullname.isnumeric())
print(fullname.isupper())
# isalpha makes sure everything is part of the alphabet
# isnumeric checks if its all numbers
# isupper checks for all uppercase