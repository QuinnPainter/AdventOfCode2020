from copy import deepcopy

input = open("input", "r")
inputLines = input.readlines()
input.close()

inputArray = []
for line in inputLines:
    inputArray.append(list(line.rstrip()))
    
def getAdjacentOccupied(x, y):
    relevantSeats = []
    spaceLeft = x > 0
    spaceRight = x < (len(inputArray[0]) - 1)
    spaceUp = y > 0
    spaceDown = y < (len(inputArray) - 1)
    if spaceLeft:
        relevantSeats.append(inputArray[y][x - 1]) # left
    if spaceRight:
        relevantSeats.append(inputArray[y][x + 1]) # right
    if spaceUp:
        relevantSeats.append(inputArray[y - 1][x]) # up
    if spaceDown:
        relevantSeats.append(inputArray[y + 1][x]) # down
    if spaceUp and spaceLeft:
        relevantSeats.append(inputArray[y - 1][x - 1]) # up left
    if spaceUp and spaceRight:
        relevantSeats.append(inputArray[y - 1][x + 1]) # up right
    if spaceDown and spaceLeft:
        relevantSeats.append(inputArray[y + 1][x - 1]) # down left
    if spaceDown and spaceRight:
        relevantSeats.append(inputArray[y + 1][x + 1]) # down right
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
            elif seatState == '#' and occupied >= 4:
                timesStateChanged += 1
                newArray[y][x] = 'L'
    inputArray = deepcopy(newArray)

finalOccupied = 0  
for y in range(0, len(inputArray)):
    for x in range(0, len(inputArray[0])):
        if inputArray[y][x] == '#':
            finalOccupied += 1
print(finalOccupied)