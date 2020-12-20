input = open("input", "r")
inputLines = input.readlines()
input.close()

ranges1 = []
ranges2 = []
for i in inputLines:
    line = i.rstrip()
    if line == "":
        break
    rangeText = line.split(": ")[1]
    rangeTexts = rangeText.split(" or ")
    range1num1 = int(rangeTexts[0].split("-")[0])
    range1num2 = int(rangeTexts[0].split("-")[1])
    range2num1 = int(rangeTexts[1].split("-")[0])
    range2num2 = int(rangeTexts[1].split("-")[1])
    ranges1.append([range1num1, range1num2])
    ranges2.append([range2num1, range2num2])
    
nearTickets = []
foundNearTickets = False
for i in inputLines:
    if "nearby tickets:" in i:
        foundNearTickets = True
        continue
    if foundNearTickets == False:
        continue
    ticketNumsString = i.split(",")
    ticketNums = []
    ticketValid = True
    for n in ticketNumsString:
        num = int(n)
        numValid = False
        for r in ranges1 + ranges2:
            if num >= r[0] and num <= r[1]:
                numValid = True
        if numValid == False:
            ticketValid = False
        ticketNums.append(num)
    if ticketValid:
        nearTickets.append(ticketNums)
    
possibleFields = []
for i in nearTickets[0]:
    possibleFields.append(list(range(0, len(ranges1))))

for ticket in nearTickets:
    for ticketFieldNum in range(0, len(ticket)):
        tNum = ticket[ticketFieldNum]
        newPossibleFieldsForNum = []
        for fieldNum in possibleFields[ticketFieldNum]:
            r1 = ranges1[fieldNum]
            r2 = ranges2[fieldNum]
            if (tNum >= r1[0] and tNum <= r1[1]) or (tNum >= r2[0] and tNum <= r2[1]):
                newPossibleFieldsForNum.append(fieldNum)
        possibleFields[ticketFieldNum] = newPossibleFieldsForNum

# Based on this observation:
# https://www.reddit.com/r/adventofcode/comments/keiy95/2020_day_16_part_2_an_interesting_regularity_in/
# we know that, if you sort possibleFields by the number of elements
# in each element the number of possible fields for each ticket position
# increases by 1 every time.

possibleFieldsSorted = sorted(possibleFields, key=lambda x: len(x))

fieldCorrelations = [0] * len(possibleFields)

prevItem = []
for i in possibleFieldsSorted:
    for n in i:
        if n not in prevItem:
            fieldCorrelations[possibleFields.index(i)] = n
    prevItem = i
    
# We need the 6 fields that start with "departure"
# They happen to be the first 6 fields, 0 - 5.

myTicket = []

for i in range(0, len(inputLines)):
    if "your ticket:" in inputLines[i]:
        for num in inputLines[i+1].rstrip().split(","):
            myTicket.append(int(num))
        break
        
multiplyTotal = 1        
for i in range(0, len(myTicket)):
    if fieldCorrelations[i] < 6:
        multiplyTotal *= myTicket[i]
print(multiplyTotal)