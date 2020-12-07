input = open("input", "r")
inputLines = input.readlines()
input.close()

currentBagsSearch = ["shiny gold"]
numAddedThisPass = 999

while numAddedThisPass > 0:
    numAddedThisPass = 0
    for bagRule in inputLines:
        bagType = bagRule.split(" bags")[0]
        containRule = bagRule.split(" contain ")[1].rstrip()
        containTypes = []
        if containRule != "no other bags.":
            containRuleSplit = containRule.split(" ")
            for i in range(0, len(containRuleSplit)):
                if "bag" in containRuleSplit[i]:
                    containTypes.append(containRuleSplit[i-2] + " " + containRuleSplit[i-1])
        if any(c in currentBagsSearch for c in containTypes) and bagType not in currentBagsSearch:
            currentBagsSearch.append(bagType)
            numAddedThisPass += 1
            
# -1 to remove "shiny gold"
print(len(currentBagsSearch) - 1)