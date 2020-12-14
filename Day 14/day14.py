input = open("input", "r")
inputLines = input.readlines()
input.close()

memDict = {}
currentBitmask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

for line in inputLines:
    instrValue = line.split(" = ")[1].rstrip()
    if line.startswith("mask"):
        currentBitmask = instrValue
    elif line.startswith("mem"):
        memAddr = int(line.split("]")[0][4:])
        instrBinary = list(format(int(instrValue), 'b').zfill(36))
        for i in range(0, len(instrBinary)):
            if currentBitmask[i] == '0' or currentBitmask[i] == '1':
                instrBinary[i] = currentBitmask[i]
        outputValue = int("".join(instrBinary), 2)
        memDict[memAddr] = outputValue
        
totalValue = 0
for key in memDict:
    totalValue += memDict[key]
print(totalValue)