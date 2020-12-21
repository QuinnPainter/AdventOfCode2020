input = open("input", "r")
inputLines = input.readlines()
input.close()

def doOperation(num1, num2, operator):
    if operator == "*":
        return num1 * num2
    if operator == "+":
        return num1 + num2
    print ("Invalid Operator: " + operator)
    return 0
    
def evaluateExpression(expr):
    brktDepth = 0
    currentBrktExpr = ""
    expr = expr + "*" # add op to the end so the last number gets counted
    # First pass - evaluates brackets
    exprBracketsDone = ""
    for c in expr:
        if c == '(':
            brktDepth += 1
            if brktDepth > 1:
                currentBrktExpr += c
        elif c == ')':
            brktDepth -= 1
            if brktDepth > 0:
                currentBrktExpr += c
            if brktDepth == 0:
                exprBracketsDone += str(evaluateExpression(currentBrktExpr))
                currentBrktExpr = ""
        elif brktDepth < 1:
            exprBracketsDone += c
        else:
            currentBrktExpr += c
    # Second - splits into 2 arrays, numbers and operators
    numArr = []
    opArr = []
    currentNum = 0
    for c in exprBracketsDone:
        if c == '*' or c == '+':
            numArr.append(currentNum)
            currentNum = 0
            opArr.append(c)
        else:
            currentNum = (currentNum * 10) + int(c)
    #print(numArr)
    #print(opArr)
    # Third - evaluates adds
    newNumArr = []
    runningAdd = 0
    for i in range(0, len(opArr)):
        if opArr[i] == '*':
            newNumArr.append(runningAdd + numArr[i])
            runningAdd = 0
        else:
            runningAdd += numArr[i]
    #print(newNumArr)
    # Fourth - evaluates multiplies
    returnValue = 1
    for num in newNumArr:
        returnValue *= num
    return returnValue

inputData = []
for line in inputLines: # Remove all newlines and spaces
    cleaned = line.rstrip().replace(" ", "")
    if cleaned != "":
        inputData.append(cleaned)
        
totalSum = 0
for line in inputData:
    totalSum += evaluateExpression(line)
    #print(evaluateExpression(line))
print("total: " + str(totalSum))