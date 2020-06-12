
firstList = ["2",3,4,5,6,1,3,5,5,2,3,6,67,7,2,3,5,6,2]
rangeOfList = len(firstList)
print(firstList)

#int(firstList)

#print(firstList)

for x in range(firstList):
    firstList[x] = int(firstList[x])

for z in range(0, len(firstList)):
    firstList[z] += 1


print(firstList)


for x in range(0, len(firstList)):
    firstList[x] = firstList[x] + 1


print(firstList)