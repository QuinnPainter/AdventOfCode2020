from copy import deepcopy

input = open("input", "r")
inputLines = input.readlines()
input.close()

boardSize = 30

inputData = []

for line in inputLines:
    lStrip = line.rstrip()
    if lStrip != "":
        inputData.append(lStrip)

state = [[["." for _ in range(boardSize)] for _ in range(boardSize)] for _ in range(boardSize)]

def getNeighboursActive(x, y, z):
    numActive = 0
    for checkX in range(x - 1, x + 2):
        for checkY in range(y - 1, y + 2):
            for checkZ in range(z - 1, z + 2):
                if checkX == x and checkY == y and checkZ == z:
                    continue
                try:
                    if state[checkZ][checkY][checkX] == '#':
                        numActive += 1
                except IndexError:
                    pass
    return numActive

for y in range(0, len(inputData)):
    for x in range(0, len(inputData[y])):
        #print ("[" + str(int(len(state) / 2)) + "][" + str(int(len(state[0]) / 2) + y) + "]["  + str(int(len(state[0][0]) / 2) + x) + "] = " + str(inputData[y][x]))
        state[int(len(state) / 2)][int(len(state[0]) / 2) + y][int(len(state[0][0]) / 2) + x] = inputData[y][x]
        
#for y in state[50]:
#    print ("".join(y))
        
for i in range(0, 6):
    newState = deepcopy(state)
    for z in range(0, len(state)):
        for y in range(0, len(state[0])):
            for x in range(0, len(state[0][0])):
                nActive = getNeighboursActive(x, y, z)
                if state[z][y][x] == '#':
                    if nActive != 2 and nActive != 3:
                        newState[z][y][x] = '.'
                elif nActive == 3:
                    newState[z][y][x] = '#'
    state = deepcopy(newState)
    
numActiveAtEnd = 0
for z in range(0, len(state)):
    for y in range(0, len(state[0])):
        for x in range(0, len(state[0][0])):
            if state[z][y][x] == '#':
                numActiveAtEnd += 1
print(numActiveAtEnd)