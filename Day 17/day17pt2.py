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

state = [[[["." for _ in range(boardSize)] for _ in range(boardSize)] for _ in range(boardSize)] for _ in range(boardSize)]

def getNeighboursActive(x, y, z, w):
    numActive = 0
    for checkW in range(w - 1, w + 2):
        for checkX in range(x - 1, x + 2):
            for checkY in range(y - 1, y + 2):
                for checkZ in range(z - 1, z + 2):
                    if checkX == x and checkY == y and checkZ == z and checkW == w:
                        continue
                    try:
                        if state[checkW][checkZ][checkY][checkX] == '#':
                            numActive += 1
                    except IndexError:
                        pass
    return numActive

for y in range(0, len(inputData)):
    for x in range(0, len(inputData[y])):
        state[int(len(state) / 2)][int(len(state[0]) / 2)][int(len(state[0][0]) / 2) + y][int(len(state[0][0][0]) / 2) + x] = inputData[y][x]
        
for i in range(0, 6):
    print(i)
    newState = deepcopy(state)
    for w in range(0, len(state)):
        for z in range(0, len(state[0])):
            for y in range(0, len(state[0][0])):
                for x in range(0, len(state[0][0][0])):
                    nActive = getNeighboursActive(x, y, z, w)
                    if state[w][z][y][x] == '#':
                        if nActive != 2 and nActive != 3:
                            newState[w][z][y][x] = '.'
                    elif nActive == 3:
                        newState[w][z][y][x] = '#'
    state = deepcopy(newState)
    
numActiveAtEnd = 0
for w in range(0, len(state)):
    for z in range(0, len(state[0])):
        for y in range(0, len(state[0][0])):
            for x in range(0, len(state[0][0][0])):
                if state[w][z][y][x] == '#':
                    numActiveAtEnd += 1
print(numActiveAtEnd)