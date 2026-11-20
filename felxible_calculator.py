#OH, period 1, Fexible calculator
endloop=False
while endloop==False:
    nums=[1,2,3,4,5,6,7]
    ch=str(input("Would you like to add all numbers, find the average, find the maximum of all the numbers, the minimum n of all the numbers, or multiply them"))
    def calc(*r):
        if r["choice"]=="Minimum":
                for i in nums:
                    for num in nums:
                        if i<num:
                            lowest=i-1
                        else:
                            break
                    break
                print(nums(lowest))
        if r["choice"]=="Maximum":
            for i in nums:
                for num in nums:
                    if i>num:
                        highest=i-1
                break
            print(highest)
        if r["choice"]=="Add":
            for i in nums:
                for num in nums:
                    sum=i+num
            print(sum)
            break
        if r["choice"]=="Average":
            for i in nums:
                for num in nums:
                    sum=i+num
            average=sum/(len(nums))
            print(average)
            break
while True:
    print(nums)
    c=(input("Would you like to add more numbers to the list? "))
    if c == "No":
        print(calc(choice=ch))
        ch2=input("Wanna do it again?")
        if ch2=="Yes":
            endloop=False
        if ch2=="No":
            endloop=True     
