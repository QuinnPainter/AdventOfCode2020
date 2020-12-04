input = open("input", "r")
inputLines = input.readlines()
input.close()

attribsNeeded = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

passportStrings = []
passportIndex = 0
for line in inputLines:
    if line.rstrip() == "":
        passportIndex += 1
        continue
    if len(passportStrings) <= passportIndex:
        passportStrings.append("")
    passportStrings[passportIndex] += line
    
validPasses = 0
for passport in passportStrings:
    attribs = passport.split()
    attribNames = []
    for attrib in attribs:
        attribNames.append(attrib.split(":")[0])
    if all(x in attribNames for x in attribsNeeded):
        validPasses += 1

print(validPasses)