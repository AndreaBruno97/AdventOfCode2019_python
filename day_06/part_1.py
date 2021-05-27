class Planet:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.level = 0

def assign_level(planets, parent):
    for child in planets[parent].children:
        planets[child].level = planets[parent].level + 1
        planets = assign_level(planets, child)
    return planets

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

    parent.children.append(cur_planet_name)

center_of_mass = "COM"
planets[center_of_mass].level = 0
planets = assign_level(planets, center_of_mass)
total_orbits = sum([x.level for x in planets.values()])

print("The total number of direct and indirect orbits is: " + str(total_orbits))