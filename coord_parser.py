import csv

def parse_csv(file_path):

    coordinates = []

    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert each value from string to float
            coords = {key: float(value) for key, value in row.items()}
            coordinates.append(coords)

    return coordinates