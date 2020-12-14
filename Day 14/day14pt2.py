input = open("input", "r")
inputLines = input.readlines()
input.close()

memDict = {}
currentBitmask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def writeValue(startIndex, addr, value):
    #if startIndex == len(addr):
    #    memDict["".join(addr)] = value
    #    return
    for i in range(startIndex, len(addr)):
        if addr[i] == 'X':
            addr0 = addr.copy()
            addr0[i] = '0'
            addr1 = addr.copy()
            addr1[i] = '1'
            writeValue(i + 1, addr0, value)
            writeValue(i + 1, addr1, value)
            return
    memDict["".join(addr)] = value

for line in inputLines:
    instrValue = line.split(" = ")[1].rstrip()
    if line.startswith("mask"):
        currentBitmask = instrValue
    elif line.startswith("mem"):
        memAddrInput = int(line.split("]")[0][4:])
        memAddrBinary = list(format(memAddrInput, 'b').zfill(36))
        for i in range(0, len(memAddrBinary)):
            if currentBitmask[i] == '1' or currentBitmask[i] == 'X':
                memAddrBinary[i] = currentBitmask[i]
        writeValue(0, memAddrBinary, int(instrValue))
        print ("".join(memAddrBinary) + " " + instrValue)
        
totalValue = 0
for key in memDict:
    totalValue += memDict[key]
print(totalValue)