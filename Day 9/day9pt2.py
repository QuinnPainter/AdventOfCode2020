import queue

input = open("input", "r")
inputLines = input.readlines()
input.close()

prevNums = queue.Queue() # FIFO
for i in range(0, 25):
    prevNums.put(int(inputLines[i].rstrip()))
    
invalidNumber = 0    

for i in range(25, len(inputLines)):
    prevNumsList = list(prevNums.queue)
    currentNum = int(inputLines[i].rstrip())
    validNum = False
    for x in range(0, len(prevNumsList)):
        for y in range(0, len(prevNumsList)):
            if x == y:
                continue
            if (prevNumsList[x] + prevNumsList[y]) == currentNum:
                validNum = True
    if validNum == False:
        invalidNumber = currentNum
        break
    prevNums.get()
    prevNums.put(currentNum)
    
    
for i in range(0, len(inputLines)):
    runningList = []
    runningSum = 0
    for x in range(i, len(inputLines)):
        currentNum = int(inputLines[x].rstrip())
        runningList.append(currentNum)
        runningSum += currentNum
        if runningSum > invalidNumber:
            break
        elif runningSum == invalidNumber and len(runningList) > 1:
            runningList.sort()
            smallest = runningList[0]
            biggest = runningList[-1]
            print (str(smallest + biggest))
            break