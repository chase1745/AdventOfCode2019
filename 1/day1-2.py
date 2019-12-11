def fuelNeeded(mass):
    return (mass//3) - 2


with open('input1.txt') as file:
    fuel = 0
    for mass in file.readlines():
        mass = int(mass)
        while mass > 0:
            mass = fuelNeeded(int(mass))
            if mass >= 0:
                fuel += mass

print("Total fuel needed: {}".format(fuel))