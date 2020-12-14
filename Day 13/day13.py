input = open("input", "r")
inputLines = input.readlines()
input.close()

targetTime = int(inputLines[0])
currentEarliestBus = 999
currentEarliestBusTime = 99999999999999999

for bus in inputLines[1].split(","):
    if bus == "x":
        continue
    busID = int(bus)
    thisBusTime = 0
    while thisBusTime < targetTime:
        thisBusTime += busID
    if thisBusTime < currentEarliestBusTime:
        currentEarliestBusTime = thisBusTime
        currentEarliestBus = busID
        
waitTime = currentEarliestBusTime - targetTime
print (currentEarliestBus * waitTime)