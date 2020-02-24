import random

import numpy as np

from cube_rotations import perform_cube_operations

random.seed(183890)


def get_side_matrix(color, n):
    entire_side = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(color)
        entire_side.append(row)
    return np.array(entire_side)


def generate_solved_cube_matrix(n):
    generated_sides = {}
    color_list = ['w', 'r', 'g', 'o', 'b', 'y']
    for index, color in enumerate(color_list):
        generated_sides.update({index: get_side_matrix(color, n)})
    return generated_sides


# if len(sys.argv) == 3:
#     n = sys.argv[1]
#     total_states = sys.argv[2]
# else:
#     print("Invalid argument count")
#     exit(0)

n = 3
total_states = 1

cube_slices_list = list(range(1, (n + 1)))
axes_list = ['x', 'y', 'z']
rotations_list = [1, 2, 3]
sides = generate_solved_cube_matrix(n)

for state in range(total_states):
    # scramble_size = random.randint(1, 100)
    scramble_size = 1
    for scramble in range(scramble_size):
        cube_slice = random.choice(cube_slices_list)
        axis = random.choice(axes_list)
        rotation = random.choice(rotations_list)
        perform_cube_operations(n, sides, cube_slice, axis, rotation)
