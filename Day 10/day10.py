input = open("input", "r")
inputLines = input.readlines()
input.close()

inputNums = []
for line in inputLines:
    inputNums.append(int(line.rstrip()))
    
inputNums.sort()
# targetJolts = inputNums[-1] + 3

oneDiffs = 0
threeDiffs = 0

inputNums.insert(0, 0) # insert 0 at beginning for charging input

for n in range(0, len(inputNums)):
    if n + 1 == len(inputNums):
        threeDiffs += 1
        break
    currentAdapter = inputNums[n]
    nextAdapter = inputNums[n + 1]
    adapterDifference = nextAdapter - currentAdapter
    if adapterDifference == 1:
        oneDiffs += 1
    elif adapterDifference == 3:
        threeDiffs += 1
        
print(oneDiffs * threeDiffs)