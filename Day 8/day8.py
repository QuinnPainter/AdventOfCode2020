input = open("input", "r")
inputLines = input.readlines()
input.close()

executedInstructions = []
progCounter = 0
accumulator = 0
while True:
    instr = inputLines[progCounter][:3]
    arg = int(inputLines[progCounter].rstrip()[4:])
    if progCounter in executedInstructions:
        break
    executedInstructions.append(progCounter)
    if instr == "nop":
        progCounter += 1
    elif instr == "acc":
        accumulator += arg
        progCounter += 1
    elif instr == "jmp":
        progCounter += arg
        
print (accumulator)