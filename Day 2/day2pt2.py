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
    needed1 = password[startRange - 1] == charNeeded
    needed2 = password[endRange - 1] == charNeeded
    if (needed1 or needed2) and not (needed1 and needed2):
        numValid += 1
        
print(numValid)