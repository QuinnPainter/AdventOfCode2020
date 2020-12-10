input = open("input", "r")
inputLines = input.readlines()
input.close()

inputNums = []
for line in inputLines:
    inputNums.append(int(line.rstrip()))
    
inputNums.sort()

inputNums.insert(0, 0) # insert 0 at beginning for charging input
inputNums.append(inputNums[-1] + 3)

pathsPerNum = [0] * len(inputNums)
pathsPerNum[0] = 1
for n in range(0, len(inputNums)):
    for i in range(1, 4):
        if n + i < len(inputNums):
            if inputNums[n + i] - inputNums[n] <= 3:
                pathsPerNum[n + i] += pathsPerNum[n]

print(pathsPerNum[-1])
    
# This recursion based approach would have worked, but it took
# WAY TOO LONG. Some estimation math shows this would have taken
# AT LEAST a year to complete.
#def getNumPaths(input):
#    numPaths = 0
#    numPathsThisIteration = 0
#    for n in inputNums:
#        if n - input > 0 and n - input <= 3:
#            numPaths += getNumPaths(n)
#            numPathsThisIteration += 1
#        if n - input > 3:
#            break
#    if numPathsThisIteration == 0:
#        return 1 # we're on the last number, end the recursion chain
#    return numPaths
#    
#print(getNumPaths(0))