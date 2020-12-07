input = open("input", "r")
inputLines = input.readlines()
input.close()
inputLines.append("") # add blank line so last group will get flushed

currentAnswers = "abcdefghijklmnopqrstuvwxyz"
totalSum = 0
for line in inputLines:
    if line.rstrip() == "":
        totalSum += len(currentAnswers)
        currentAnswers = "abcdefghijklmnopqrstuvwxyz"
        continue
    currentAnswers = [c for c in line.rstrip() if c in currentAnswers]
            
print(totalSum)