def containsDoubleDigit(num):
    prev = None
    for n in str(num):
        if n == prev:
            return True

        prev = n

    return False

def isIncreasing(num):
    return sorted(list(str(num))) == list(str(num))

passRange = (372304, 847060+1)

numPasses = 0
for num in range(*passRange):
    if containsDoubleDigit(num) and isIncreasing(num):
        numPasses += 1

print("Number of possible passwords: {}".format(numPasses))