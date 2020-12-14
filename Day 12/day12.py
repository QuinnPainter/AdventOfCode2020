input = open("input", "r")
inputLines = input.readlines()
input.close()

currentX = 0
currentY = 0
currentDir = 0 # 0 to 3, 0 = E, 1 = S, 2 = W, 3 = N

for line in inputLines:
    actionChar = line[0]
    actionNum = int(line[1:].rstrip())
    if actionChar == 'N':
        currentY += actionNum
    elif actionChar == 'S':
        currentY -= actionNum
    elif actionChar == 'E':
        currentX += actionNum
    elif actionChar == 'W':
        currentX -= actionNum
    elif actionChar == 'L':
        currentDir = (currentDir - (actionNum / 90)) % 4
    elif actionChar == 'R':
        currentDir = (currentDir + (actionNum / 90)) % 4
    elif actionChar == 'F':
        if currentDir == 3:
            currentY += actionNum
        elif currentDir == 1:
            currentY -= actionNum
        elif currentDir == 0:
            currentX += actionNum
        elif currentDir == 2:
            currentX -= actionNum
            
print(abs(currentX) + abs(currentY))