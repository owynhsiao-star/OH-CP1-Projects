#OH, period 1 debugger notes
grades = [85, 90, 78, 92, 88]

total=0
count= len(grades)


for grade in grades:      
        total = total+grade
    #breakpoint makes the debugger stop at the breakpoint   
average=total/count

print(f"the average grade is {average}")
#A debugger is a tool that is pre equipped into most IDE's to let you observe what a program is doing while it runs

scores=[12,45,7,68,90,21]

runningtotal=0
highestscore=0

for score in scores: 
        runningtotal+= score 
        if score>highestscore:
                highestscore=score

print(f"total: {runningtotal}")
print(f"Highest score: {highestscore}")
