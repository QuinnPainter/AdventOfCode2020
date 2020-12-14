input = open("input", "r")
inputLines = input.readlines()
input.close()

currentX = 0
currentY = 0
waypointX = 10
waypointY = 1

for line in inputLines:
    actionChar = line[0]
    actionNum = int(line[1:].rstrip())
    if actionChar == 'N':
        waypointY += actionNum
    elif actionChar == 'S':
        waypointY -= actionNum
    elif actionChar == 'E':
        waypointX += actionNum
    elif actionChar == 'W':
        waypointX -= actionNum
    elif actionChar == 'L':
        for i in range(actionNum, 0, -90):
            temp = waypointX
            waypointX = waypointY * -1
            waypointY = temp
    elif actionChar == 'R':
        for i in range(actionNum, 0, -90):
            temp = waypointX
            waypointX = waypointY
            waypointY = temp * -1
    elif actionChar == 'F':
        for i in range(0, actionNum):
            currentX += waypointX
            currentY += waypointY
            
print(abs(currentX) + abs(currentY))