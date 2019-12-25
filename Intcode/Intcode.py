class Intcode:
    def __init__(self, filename, display=True):
        self.filename = filename
        self.display = display

    def opcodeFunc(self, op, vals):
        if op == 1:
            return self.opcodes[vals[0]] + self.opcodes[vals[1]]
        elif op == 2:
            return self.opcodes[vals[0]] * self.opcodes[vals[1]]

    def run(self, resetVals):
        with open(self.filename) as file:
            opPtr = 0
            self.opcodes = list(map(lambda op:int(op), file.readline().split(',')))
            self.opcodes[1], self.opcodes[2] = resetVals
            op = self.opcodes[opPtr]
            while op != 99:
                self.opcodes[self.opcodes[opPtr + 3]] = self.opcodeFunc(op, self.opcodes[opPtr+1:opPtr+3])
                opPtr += 4
                op = self.opcodes[opPtr]
        if self.display:
            print("Final value at index 0: {}".format(self.opcodes[0]))

        return self.opcodes[0]
