import sys

def getFirstCascade(num1, num2, cDiff):
    i = 0
    while(True):
        if (((num2 * i) - cDiff) % num1) == 0:
            return (num2 * i) - cDiff
        i += 1
        
def getFirstCascade2(meshP, cPDiff, num2, cDiff):
    i = 0
    while(True):
        num1 = ((meshP * i) + cPDiff)
        if ((num1 + cDiff) % num2) == 0:
            retMeshP = num1 * num2
            retCPDiff = (num1 - retMeshP) + cDiff
            return [retMeshP, retCPDiff]
        i += 1

#print (getFirstCascade(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
print (getFirstCascade2(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])))