input = open("input", "r")
inputLines = input.readlines()
input.close()

strippedLines = []
for line in inputLines:
    strippedLines.append(line.rstrip())

slopesToCheck = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

mapWidth = len(strippedLines[0])
mapHeight = len(strippedLines)

multipliedTotal = 1

for slope in slopesToCheck:
    numTrees = 0
    x = 0
    for y in range(0, mapHeight, slope[1]):
        x %= mapWidth
        if strippedLines[y][x] == '#':
            numTrees += 1
        x += slope[0]
    multipliedTotal *= numTrees
    
print(multipliedTotal)