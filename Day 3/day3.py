input = open("input", "r")
inputLines = input.readlines()
input.close()

strippedLines = []
for line in inputLines:
    strippedLines.append(line.rstrip())

x = 0
mapWidth = len(strippedLines[0])
mapHeight = len(strippedLines)

numTrees = 0
for y in range(0, mapHeight):
    x %= mapWidth
    if strippedLines[y][x] == '#':
        numTrees += 1
    x += 3
    
print(numTrees)