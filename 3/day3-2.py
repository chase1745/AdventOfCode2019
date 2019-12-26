with open('input.txt') as file:
    wire1Moves = file.readline().split(',')
    wire2Moves = file.readline().split(',')


wireMovesList = [wire1Moves, wire2Moves]
wire1Coords, wire2Coords = set(), set()
wireCoordList = [wire1Coords, wire2Coords]
wire1StepMap, wire2StepMap = {}, {}
wireStepMapList = [wire1StepMap, wire2StepMap]

for wireMoves, wireCoords, wireStepMap in zip(wireMovesList, wireCoordList, wireStepMapList):
    curr = (0,0)
    steps = 0
    for move in wireMoves:
        direction = move[0]
        amount = int(move[1:])

        if direction == 'R':
            for i in range(amount):
                curr = (curr[0] + 1, curr[1])
                steps += 1
                wireStepMap[curr] = steps
                wireCoords.add(curr)
        elif direction == 'L':
            for i in range(amount):
                curr = (curr[0] - 1, curr[1])
                steps += 1
                wireStepMap[curr] = steps
                wireCoords.add(curr)
        elif direction == 'U':
            for i in range(amount):
                curr = (curr[0], curr[1] + 1)
                steps += 1
                wireStepMap[curr] = steps
                wireCoords.add(curr)
        elif direction == 'D':
            for i in range(amount):
                curr = (curr[0], curr[1] - 1)
                steps += 1
                wireStepMap[curr] = steps
                wireCoords.add(curr)

intersections = wire1Coords.intersection(wire2Coords)
minSignal = float('inf')
for coord in intersections:
    signal = wire1StepMap[coord] + wire2StepMap[coord]
    minSignal = min(minSignal, signal)

print("Min signal: {}".format(minSignal))