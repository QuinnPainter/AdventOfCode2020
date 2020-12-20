input = open("input", "r")
inputLines = input.readlines()
input.close()

ranges = []
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
    ranges.append([range1num1, range1num2])
    ranges.append([range2num1, range2num2])
    
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
    for n in ticketNumsString:
        ticketNums.append(int(n))
    nearTickets.append(ticketNums)
    
ticketErrorRate = 0
for ticket in nearTickets:
    for num in ticket:
        numValid = False
        for r in ranges:
            if num >= r[0] and num <= r[1]:
                numValid = True
        if numValid == False:
            ticketErrorRate += num
print (ticketErrorRate)