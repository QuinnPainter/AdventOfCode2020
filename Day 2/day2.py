input = open("input", "r")
inputLines = input.readlines()
input.close()

numValid = 0
for line in inputLines:
    splitSpaces = line.split(" ")
    ranges = splitSpaces[0].split("-")
    startRange = int(ranges[0])
    endRange = int(ranges[1])
    charNeeded = splitSpaces[1][0]
    password = splitSpaces[2].rstrip()
    numNeededChars = password.count(charNeeded)
    if numNeededChars >= startRange and numNeededChars <= endRange:
        numValid += 1
        
print(numValid)