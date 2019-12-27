class Intcode:
    def __init__(self, filename, display=True):
        self.filename = filename
        self.display = display
        self.opPtr = 0
        self.opcodes = []

    def op(self):
        return int(str(self.opcodes[self.opPtr]).rjust(5, '0')[-2:])

    def saveNewVal(self, index, val):
        print('saving new val')
        print('index: {}'.format(index))
        print('val: {}'.format(val))
        self.opcodes[index] = val

    def getVal(self, index, mode=0):
        # print('mode: {}'.format(mode))
        # print('index: {}'.format(index))
        if mode == 0:
            # print(self.opcodes[index])
            # print('val: {}'.format(self.opcodes[self.opcodes[index]]))
            return self.opcodes[self.opcodes[index]]
        elif mode == 1:
            return self.opcodes[index]
        else:
            raise ValueError("Invalid mode: {}".format(mode))

    def getParamModes(self, instruction, length):
        # print(str(instruction))
        # print(str(instruction).rjust(length, '0'))
        # print('modes: {}'.format(list(reversed(str(instruction).rjust(length, '0')[:-2]))))
        return list(map(lambda x:int(x), reversed(str(instruction).rjust(length, '0')[:-2])))

    def getParams(self, modes, op):
        if op == 1 or op == 2:
            return [
                self.getVal(self.opPtr+1, modes[0]),
                self.getVal(self.opPtr+2, modes[1]),
                self.getVal(self.opPtr+3, 1)
                ]
        elif op == 3 or op == 4:
            return [
                self.getVal(self.opPtr+1, 1)
            ]
        else:
            raise ValueError("Invalid op: {}".format(op))

    def opcodeFunc(self, op):
        paramModes = self.getParamModes(self.opcodes[self.opPtr], 5)
        # print('opptr: {}'.format(self.opPtr))
        print('op: {}'.format(op))
        print('modes: {}'.format(paramModes))
        params = self.getParams(paramModes, op)
        print('params: {}'.format(params))

        if op == 1:
            newVal = params[0] + params[1]
            self.saveNewVal(params[2], newVal)
            return 4
        elif op == 2:
            newVal = params[0] * params[1]
            self.saveNewVal(params[2], newVal)
            return 4
        elif op == 3:
            inputVal = input("Input integer: ")
            self.saveNewVal(params[0], int(inputVal))
            return 2
        elif op == 4:
            print(self.opcodes[params[0]])
            return 2
        else:
            raise ValueError("Invalid op: {}".format(op))


    def run(self, resetVals=None):
        with open(self.filename) as file:
            self.opcodes = list(map(lambda op:int(op), file.readline().split(',')))
            if resetVals is not None:
                self.opcodes[1], self.opcodes[2] = resetVals

            while self.op() != 99:
                print(self.opcodes[self.opPtr:self.opPtr+10])
                print(self.opPtr)
                incNum = self.opcodeFunc(self.op())
                self.opPtr += incNum

        if self.display:
            print("Final value at index 0: {}".format(self.opcodes[0]))

        return self.opcodes[0]
