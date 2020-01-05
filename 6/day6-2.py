from collections import defaultdict

def recursiveOrbit(planet, orbitMap, seen, count):
    seen.add(planet)
    santasOrbit = orbitMap['SAN'][0]
    if planet == santasOrbit:
        return count

    for orbitedPlanet in orbitMap[planet]:
        if orbitedPlanet in seen:
            continue

        seen.add(orbitedPlanet)
        orbit = recursiveOrbit(orbitedPlanet, orbitMap, seen, count + 1)
        if orbit >= 0: return orbit
    return -1


with open('input.txt') as file:
    orbits = list(map(lambda x:x.rstrip().split(')'), file.readlines()))

orbitMap = defaultdict(list)
for x, y in orbits:
    orbitMap[y].append(x)
    orbitMap[x].append(y)

you = 'YOU'
seen = set()
orbits = recursiveOrbit(orbitMap[you][0], orbitMap, seen, 0)

print('number of orbits to get to santa: {}'.format(orbits))
