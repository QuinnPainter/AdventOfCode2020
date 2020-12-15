input = open("input", "r")
inputLines = input.readlines()
input.close()

# Naive list solution. Worked for part 1, too slow for part 2
#inputNums = []
#for i in inputLines[0].split(","):
#    inputNums.append(int(i))
#
#turns = []
#for i in range(0, 2020):
#    if i % 10000 == 0:
#        print (i)
#    if i < len(inputNums):
#        turns.append(inputNums[i])
#        continue
#    prevNum = turns[i - 1]
#    lastOccurence = 0
#    try:
#        lastOccurence = len(turns) - 2 - turns[-2::-1].index(prevNum)
#    except ValueError:
#        turns.append(0)
#        continue
#    turns.append((i - 1) - lastOccurence)
#    
#print (turns[-1])

inputSplit = inputLines[0].split(",")
indexDict = {}
indexDictBeforeLast = {}
for i in range(0, len(inputSplit)):
    indexDict[int(inputSplit[i])] = i
    if i < len(inputSplit) - 1:
        indexDictBeforeLast[int(inputSplit[i])] = i
lastNum = int(inputSplit[-1])

# For part 2, change 2020 to 30000000
for i in range(len(inputSplit), 30000000):
    if (i % 100000) == 0: # progress
        print(i)
    lastIndex = 0
    try:
        lastIndex = indexDictBeforeLast[lastNum]
    except KeyError:
        indexDictBeforeLast[lastNum] = i - 1
        indexDict[0] = i
        lastNum = 0
        continue
    indexDictBeforeLast[lastNum] = i - 1
    indexDict[i - (lastIndex + 1)] = i
    lastNum = i - (lastIndex + 1)
    
print(lastNum) 