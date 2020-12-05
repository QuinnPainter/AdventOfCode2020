input = open("input", "r")
inputLines = input.readlines()
input.close()

ids = []

for boardpass in inputLines:
    rowInfo = boardpass.rstrip()[:-3]
    colInfo = boardpass.rstrip()[-3:]
    rowLowerRange = 0
    rowUpperRange = 127
    lastSelection = 0
    for c in rowInfo:
        midpoint = int(((rowUpperRange - rowLowerRange) / 2) + rowLowerRange)
        if c == 'F':
            rowUpperRange = midpoint
            lastSelection = rowUpperRange
        elif c == 'B':
            rowLowerRange = midpoint + 1
            lastSelection = rowLowerRange
    row = lastSelection
    colLowerRange = 0
    colUpperRange = 7
    for c in colInfo:
        midpoint = int(((colUpperRange - colLowerRange) / 2) + colLowerRange)
        if c == 'L':
            colUpperRange = midpoint
            lastSelection = colUpperRange
        elif c == 'R':
            colLowerRange = midpoint + 1
            lastSelection = colLowerRange
    col = lastSelection
    seatID = (row * 8) + col
    ids.append(seatID)
    
ids.sort()
minID = ids[0]
maxID = ids[len(ids) - 1]
   
mySeat = 0   
for i in range(minID, maxID):
    if i not in ids:
        if i + 1 in ids and i - 1 in ids:
            mySeat = i
            
print(mySeat)