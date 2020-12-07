input = open("input", "r")
inputLines = input.readlines()
input.close()
inputLines.append("") # add blank line so last group will get flushed

currentAnswers = ""
totalSum = 0
for line in inputLines:
    if line.rstrip() == "":
        totalSum += len(currentAnswers)
        currentAnswers = ""
        continue
    for c in line.rstrip():
        if c not in currentAnswers:
            currentAnswers += c
            
print(totalSum)