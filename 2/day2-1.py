def opcodeFunc(op, vals, opcodes):
    if op == 1:
        return opcodes[vals[0]] + opcodes[vals[1]]
    elif op == 2:
        return opcodes[vals[0]] * opcodes[vals[1]]


with open('input.txt') as file:
    opPtr = 0
    opcodes = list(map(lambda op:int(op), file.readline().split(',')))
    op = opcodes[opPtr]
    while op != 99:
        opcodes[opcodes[opPtr + 3]] = opcodeFunc(op, opcodes[opPtr+1:opPtr+3], opcodes)
        opPtr += 4
        op = opcodes[opPtr]

print("Final value at index 0: {}".format(opcodes[0]))
