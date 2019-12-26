with open('input.txt') as file:
    wire1Moves = file.readline().split(',')
    wire2Moves = file.readline().split(',')


wireMovesList = [wire1Moves, wire2Moves]
wire1Coords, wire2Coords = set(), set()
wireCoordList = [wire1Coords, wire2Coords]

for wireMoves, wireCoords in zip(wireMovesList, wireCoordList):
    curr = (0,0)
    for move in wireMoves:
        direction = move[0]
        amount = int(move[1:])

        if direction == 'R':
            for i in range(amount):
                curr = (curr[0] + 1, curr[1])
                wireCoords.add(curr)
        elif direction == 'L':
            for i in range(amount):
                curr = (curr[0] - 1, curr[1])
                wireCoords.add(curr)
        elif direction == 'U':
            for i in range(amount):
                curr = (curr[0], curr[1] + 1)
                wireCoords.add(curr)
        elif direction == 'D':
            for i in range(amount):
                curr = (curr[0], curr[1] - 1)
                wireCoords.add(curr)

overlapping = wire1Coords.intersection(wire2Coords)
minDist = float('inf')
for x, y in overlapping:
    dist = abs(x) + abs(y)
    minDist = min(minDist, dist)

print("Min manhattan distance: {}".format(minDist))