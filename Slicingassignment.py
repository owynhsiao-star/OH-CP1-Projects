sentence="The quick brown fox jumps over the lazy dog"
word=input("what word do you want")
start=sentence.find(word)
length=len(word)
print(sentence[start:start+length])