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
    runningTotal = 0
    brktDepth = 0
    currentBrktExpr = ""
    currentNum = 0
    currentOperator = ""
    expr = expr + "+" # add op to the end so the last number gets counted
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
                currentNum = evaluateExpression(currentBrktExpr)
                currentBrktExpr = ""
        elif brktDepth > 0:
            currentBrktExpr += c
        elif c == '+' or c == '*':
            if currentOperator != "":
                runningTotal = doOperation(runningTotal, currentNum, currentOperator)
            else:
                runningTotal = currentNum # first number in expression
            currentOperator = c
            currentNum = 0
        else:
            # this handles multi-char numbers, but these never
            # actually occur in the given data
            currentNum = (currentNum * 10) + int(c)
    return runningTotal

inputData = []
for line in inputLines: # Remove all newlines and spaces
    cleaned = line.rstrip().replace(" ", "")
    if cleaned != "":
        inputData.append(cleaned)
        
totalSum = 0
for line in inputData:
    totalSum += evaluateExpression(line)
    print(evaluateExpression(line))
print("total: " + str(totalSum))