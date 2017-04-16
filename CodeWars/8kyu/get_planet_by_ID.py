def get_planet_name(id):
    name = ""
    planet_id = [
        [1, "Mercury"],
        [2, "Venus"],
        [3, "Earth"],
        [4, "Mars"],
        [5, "Jupiter"],
        [6, "Saturn"],
        [7, "Uranus"],
        [8, "Neptune"],
        ]
    for planet in planet_id:
        if id == planet[0]:
            name = str(planet[1])
            return name


get_planet_name(3)
