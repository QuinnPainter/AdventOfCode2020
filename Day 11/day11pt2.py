from copy import deepcopy

input = open("input", "r")
inputLines = input.readlines()
input.close()

inputArray = []
for line in inputLines:
    inputArray.append(list(line.rstrip()))
    
def getAdjacentOccupied(x, y):
    relevantSeats = []
    maxRight = len(inputArray[0])
    maxDown = len(inputArray)
    for newX in range(x + 1, maxRight): # right
        if inputArray[y][newX] != '.':
            relevantSeats.append(inputArray[y][newX])
            break
    for newX in range(x - 1, -1, -1): # left
        if inputArray[y][newX] != '.':
            relevantSeats.append(inputArray[y][newX])
            break
    for newY in range(y + 1, maxDown): # down
        if inputArray[newY][x] != '.':
            relevantSeats.append(inputArray[newY][x])
            break
    for newY in range(y - 1, -1, -1): # up
        if inputArray[newY][x] != '.':
            relevantSeats.append(inputArray[newY][x])
            break
    newY = y
    for newX in range(x + 1, maxRight): # right up
        newY -= 1
        if newY >= 0:
            if inputArray[newY][newX] != '.':
                relevantSeats.append(inputArray[newY][newX])
                break
    newY = y
    for newX in range(x + 1, maxRight): # right down
        newY += 1
        if newY < maxDown:
            if inputArray[newY][newX] != '.':
                relevantSeats.append(inputArray[newY][newX])
                break
    newY = y
    for newX in range(x - 1, -1, -1): # left up
        newY -= 1
        if newY >= 0:
            if inputArray[newY][newX] != '.':
                relevantSeats.append(inputArray[newY][newX])
                break
    newY = y
    for newX in range(x - 1, -1, -1): # left down
        newY += 1
        if newY < maxDown:
            if inputArray[newY][newX] != '.':
                relevantSeats.append(inputArray[newY][newX])
                break
    occupiedSeats = 0
    for s in relevantSeats:
        if s == '#':
            occupiedSeats += 1
    return occupiedSeats
    
timesStateChanged = 999
while (timesStateChanged > 0):
    #for y in inputArray:
    #    print("".join(y))
    #print("")
    timesStateChanged = 0
    newArray = deepcopy(inputArray)
    for y in range(0, len(inputArray)):
        for x in range(0, len(inputArray[0])):
            occupied = getAdjacentOccupied(x, y)
            seatState = inputArray[y][x]
            if seatState == 'L' and occupied == 0:
                timesStateChanged += 1
                newArray[y][x] = '#'
            elif seatState == '#' and occupied >= 5:
                timesStateChanged += 1
                newArray[y][x] = 'L'
    inputArray = deepcopy(newArray)

finalOccupied = 0  
for y in range(0, len(inputArray)):
    for x in range(0, len(inputArray[0])):
        if inputArray[y][x] == '#':
            finalOccupied += 1
print(finalOccupied)