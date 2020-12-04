import string

input = open("input", "r")
inputLines = input.readlines()
input.close()

eyeColours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

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
    attribDict = {}
    for a in passport.split():
        s = a.split(":")
        attribDict[s[0]] = s[1]
    numValidAttribs = 0
    if "byr" in attribDict:
        if int(attribDict["byr"]) >= 1920 and int(attribDict["byr"]) <= 2002:
            numValidAttribs += 1
    if "iyr" in attribDict:
        if int(attribDict["iyr"]) >= 2010 and int(attribDict["iyr"]) <= 2020:
            numValidAttribs += 1
    if "eyr" in attribDict:
        if int(attribDict["eyr"]) >= 2020 and int(attribDict["eyr"]) <= 2030:
            numValidAttribs += 1
    if "hgt" in attribDict:
        measure = attribDict["hgt"][-2:]
        height = attribDict["hgt"][:-2]
        if measure == "cm":
            if int(height) >= 150 and int(height) <= 193:
                numValidAttribs += 1
        if measure == "in":
            if int(height) >= 59 and int(height) <= 76:
                numValidAttribs += 1
    if "hcl" in attribDict:
        if attribDict["hcl"][0] == "#" and len(attribDict["hcl"]) == 7:
            if all(c in string.hexdigits for c in attribDict["hcl"][1:]):
                numValidAttribs += 1
    if "ecl" in attribDict:
        if attribDict["ecl"] in eyeColours:
            numValidAttribs += 1
    if "pid" in attribDict:
        if len(attribDict["pid"]) == 9 and all(c in string.digits for c in attribDict["pid"]):
            numValidAttribs += 1
    if numValidAttribs == 7:
        validPasses += 1

print(validPasses)