input = open("input", "r")
inputLines = input.readlines()
input.close()

def getNumberOfBags(inputBag):
    for bagRule in inputLines:
        bagType = bagRule.split(" bags")[0]
        if bagType != inputBag:
            continue
        containRule = bagRule.split(" contain ")[1].rstrip()
        containTypes = []
        if containRule == "no other bags.":
            return 1
        containRuleSplit = containRule.split(" ")
        for i in range(0, len(containRuleSplit)):
            if "bag" in containRuleSplit[i]:
                containTypes.append([containRuleSplit[i-2] + " " + containRuleSplit[i-1], int(containRuleSplit[i-3])])
        returnVal = 1
        for c in containTypes:
            returnVal += c[1] * getNumberOfBags(c[0])
        return returnVal

# -1 to remove "shiny gold"  
print(getNumberOfBags("shiny gold") - 1)