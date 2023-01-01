def compare_coordinates(coordinates_1, coordinates_2):
    if len(coordinates_1) != len(coordinates_2):
        return "Error: Mismatched number of coordinates"
    diffs = []
    for i in range(len(coordinates_1)):
        diffs.append(abs(coordinates_1[i] - coordinates_2[i]))
    return diffs

def read_maps(filename):
    maps = []
    with open(filename, "r") as f:
        lines = f.readlines()
    current_map = {}
    for line in lines:
        if line.strip() == "---":
            maps.append(current_map)
            current_map = {}
        else:
            key, value = line.strip().split(": ")
            current_map[key] = value
    return maps
