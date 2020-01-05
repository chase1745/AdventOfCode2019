from collections import defaultdict


globalCount = 0

def recursiveOrbit(planet, orbitMap, seenMap):
    global globalCount

    if seenMap[planet] > 0:
        globalCount += seenMap[planet]
        return seenMap[planet]

    localCount = 0
    for orbitedPlanet in orbitMap[planet]:
        orbitedCount = recursiveOrbit(orbitedPlanet, orbitMap, seenMap)
        globalCount += orbitedCount + 1
        localCount += orbitedCount

    seenMap[planet] = localCount
    return localCount


with open('input.txt') as file:
    orbits = list(map(lambda x:x.rstrip().split(')'), file.readlines()))

orbitMap = defaultdict(list)
seenMap = defaultdict(int)
for x, y in orbits:
    orbitMap[y].append(x)
    if orbitMap[x]:
        pass

for planet, directOrbits in orbitMap.items():
    recursiveOrbit(planet, orbitMap, seenMap)

print('final count: {}'.format(globalCount))
