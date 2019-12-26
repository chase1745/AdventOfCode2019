def containsExactDoubleDigit(num):
    prev = None
    groupLen = 0
    for n in str(num):
        if n == prev:
            groupLen += 1
        elif groupLen == 1:
            return True
        else:
            groupLen = 0

        prev = n
    if groupLen == 1:
        return True
    return False

def isIncreasing(num):
    return sorted(list(str(num))) == list(str(num))

passRange = (372304, 847060+1)

numPasses = 0
for num in range(*passRange):
    if containsExactDoubleDigit(num) and isIncreasing(num):
        numPasses += 1

print("Number of possible passwords: {}".format(numPasses))