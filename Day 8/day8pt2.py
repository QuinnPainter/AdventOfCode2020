input = open("input", "r")
inputLines = input.readlines()
input.close()

def checkPatchWorked(patch):
    executedInstructions = []
    progCounter = 0
    accumulator = 0
    while True:
        if progCounter == len(patch):
            return [True, accumulator]
        instr = patch[progCounter][:3]
        arg = int(patch[progCounter].rstrip()[4:])
        if progCounter in executedInstructions:
            return [False, accumulator]
        executedInstructions.append(progCounter)
        if instr == "nop":
            progCounter += 1
        elif instr == "acc":
            accumulator += arg
            progCounter += 1
        elif instr == "jmp":
            progCounter += arg

for i in range(0, len(inputLines)):
    patchedInput = inputLines.copy()
    if "acc" in patchedInput[i]:
        continue
    elif "nop" in patchedInput[i]:
        patchedInput[i] = patchedInput[i].replace("nop", "jmp")
    elif "jmp" in patchedInput[i]:
        patchedInput[i] = patchedInput[i].replace("jmp", "nop")
    result = checkPatchWorked(patchedInput)
    if result[0]:
        print(result[1])
        break