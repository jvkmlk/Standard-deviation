import math
d = [95, 98, 98, 100, 119, 125, 130, 211 ]

sum,totalN=0,len(d)

for i in d:
    sum = sum + int(i)

mean = sum/totalN

print("The Mean-->",mean)

newList=[]

for i in d:
    a = int(i) - mean
    a = a**2
    newList.append(a)

SUM = 0

for i in newList:
    SUM = SUM+i

result = SUM/(totalN-1) 

std = math.sqrt(result)

print("Standard Divison--->",std)