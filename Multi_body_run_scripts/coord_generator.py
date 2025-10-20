import random
import csv


random_seed = 10
random.seed(random_seed)
mean_separation = 100  # mm
separation_deviation = 30 # mm

n_samples = 20

coord_code = f'{random_seed}_{n_samples}_{mean_separation}_{separation_deviation}'

output_file = 'three_bernard_coords_' + coord_code + '.csv'

def random_sign():
    return random.choice([-1, 1])

def  random_separation():
    return random.gauss(mean_separation, separation_deviation)

def random_coord():
    return random_separation() * random_sign()

file_header = ["x2", "y2", "z2", "x3", "y3", "z3"]


with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(file_header)  # Header row
    for _ in range(n_samples):
        writer.writerow([random_coord() for _ in range(len(file_header))])


