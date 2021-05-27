CENTER_OF_MASS = "COM"
SANTA = "SAN"
YOU = "YOU"


class Planet:
    def __init__(self, name):
        self.name = name
        self.parent = ""


''' Open file '''
filename = 'input.txt'
with open(filename) as f:
    content = f.read()

planets = {}

for line in content.split("\n"):
    parent_name, cur_planet_name = line.split(")")

    if parent_name in planets:
        parent = planets[parent_name]
    else:
        parent = Planet(parent_name)
        planets[parent_name] = parent

    if cur_planet_name in planets:
        new_planet = planets[cur_planet_name]
    else:
        new_planet = Planet(cur_planet_name)
        planets[cur_planet_name] = new_planet

    new_planet.parent = parent_name

santa_orbital_chain = [SANTA]
i = 0
while santa_orbital_chain[i] != CENTER_OF_MASS:
    santa_orbital_chain.append(planets[santa_orbital_chain[i]].parent)
    i += 1

i = 1
common_ancestor = YOU
while common_ancestor != CENTER_OF_MASS and common_ancestor not in santa_orbital_chain:
    common_ancestor = planets[common_ancestor].parent
    i += 1

santa_orbital_transfers_num = santa_orbital_chain.index(common_ancestor) - 1
you_orbital_transfers_num = i - 2

total_transfers = santa_orbital_transfers_num + you_orbital_transfers_num

print("The total number of orbital transfers is: " + str(total_transfers))
