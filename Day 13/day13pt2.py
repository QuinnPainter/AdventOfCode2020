input = open("testinput", "r")
inputLines = input.readlines()
input.close()

def getFirstCascade(num1, num2, cDiff):
    i = 0
    while(True):
        if (((num2 * i) - cDiff) % num1) == 0:
            return (num2 * i)
        i += 1

cascadeDiff = 1
runningCascade = 0
for bus in inputLines[1].split(","):
    if bus == "x":
        cascadeDiff += 1
        continue
    busID = int(bus)
    if runningCascade == 0:
        runningCascade = busID
        continue
    runningCascade = getFirstCascade(runningCascade, busID, cascadeDiff)
    cascadeDiff = 1
    
print(runningCascade)