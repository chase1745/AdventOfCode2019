def fuelNeeded(mass):
    return (mass//3) - 2


with open('input1.txt') as file:
    fuel = 0
    for mass in file.readlines():
        fuel += fuelNeeded(int(mass))

print("Total fuel needed: {}".format(fuel))