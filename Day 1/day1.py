input = open("input", "r")
inputLines = input.readlines()
input.close()
inputNums = [int(i) for i in inputLines]

ret = 0

for i in inputNums:
    for j in inputNums:
        if i != j:
            if i + j == 2020:
                ret = i * j
                
if ret == 0:
    print("No result")
else:
    print(ret)