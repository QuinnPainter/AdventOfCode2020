import queue

input = open("input", "r")
inputLines = input.readlines()
input.close()

prevNums = queue.Queue() # FIFO
for i in range(0, 25):
    prevNums.put(int(inputLines[i].rstrip()))
    
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
        print (currentNum)
        break
    prevNums.get()
    prevNums.put(currentNum)