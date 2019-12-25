from Intcode.Intcode import Intcode

intcode = Intcode('2/input.txt', False)


search = 19690720
for i in range(100):
    for j in range(100):
        val = intcode.run((i, j))
        if val == search:
            print("Vals: {}, {} = {}".format(i, j, 100*i+j))
            exit()
