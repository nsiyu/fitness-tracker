import re

def compare_coordinates(coordinates_1, coordinates_2):
    if len(coordinates_1) != len(coordinates_2):
        return "Error: Mismatched number of coordinates"
    diffs = []
    for i in range(len(coordinates_1)):
        diffs.append(abs(coordinates_1[i] - coordinates_2[i]))
    return diffs

def parse_input(input_file: str):
    # Read the input file
    with open(input_file, 'r') as f:
        input_string = f.read()
    
    # Use regular expressions to extract the landmarks
    landmarks = re.findall(r"landmark {[\s\S]*?}", input_string)
    
    # Parse the landmarks and return them as a list of dictionaries
    result = []
    for landmark in landmarks:
        x = re.search(r"x: ([\d.-]+)", landmark).group(1)
        y = re.search(r"y: ([\d.-]+)", landmark).group(1)
        z = re.search(r"z: ([\d.-]+)", landmark).group(1)
        visibility = re.search(r"visibility: ([\d.-]+)", landmark).group(1)
        x = float(x)
        y = float(y)
        z = float(z)
        visibility = float(visibility)
        result.append({'x': x, 'y': y, 'z': z, 'visibility': visibility})
    return result

