input = open("input", "r")
inputLines = input.readlines()
input.close()
inputNums = [int(i) for i in inputLines]

ret = 0

for i in inputNums:
    for j in inputNums:
        for x in inputNums:
            if i != j and j != x:
                if i + j + x == 2020:
                    ret = i * j * x
                
if ret == 0:
    print("No result")
else:
    print(ret)