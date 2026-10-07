
def times(number):
    return number*2
#This is how you create a function btw
#Times is the function name
nums=range(1,6)
multiplied_numbers=map(times, nums)
#Mapping is the process of running an operation on each item in a list
#it takes in whatever function name we're running
#If you have map you don't need to write like print(int(list)), just print(int, list)
#It's primary purpose is altering a list, it always returns a new value and leaves original data alone, happens on EVERY item in the list no matter what
print (*list(multiplied_numbers))
nunums=[]
for num in nums:
    nunums.append(num*2)
print(*nunums)
#Mapping is commonly used for accumulator patters
#Accumulator patters are when you start with an empty list and repeatedly add values through loops


sib=["Mirai", "Irene", "vivi", "me"]
length=list(map(len, sib))
print(*length)