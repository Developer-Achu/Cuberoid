import random

import numpy as np

from cube_rotations import perform_cube_operations

random.seed(183890)


def get_side_matrix(color, n):
    entire_side = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(color)
        entire_side.append(row)
    return np.array(entire_side)


def generate_solved_cube_matrix(n):
    generated_sides = {}
    color_list = list(range(1, 7))
    for index, color in enumerate(color_list):
        generated_sides.update({index + 1: get_side_matrix(color, n)})
    return generated_sides


# if len(sys.argv) == 3:
#     n = sys.argv[1]
#     total_states = sys.argv[2]
# else:
#     print("Invalid argument count")
#     exit(0)

n = 3
total_states = 1

'''
    Note: slice and rotation starts from 1
    sides are counted from 0
'''
cube_slices_list = list(range(1, (n + 1)))
axes_list = ['x', 'y', 'z']
rotations_list = [1, 2, 3]
sides = generate_solved_cube_matrix(n)

for state in range(total_states):
    # scramble_size = random.randint(1, 100)
    scramble_size = 5
    for scramble in range(scramble_size):
        cube_slice = random.choice(cube_slices_list)
        axis = random.choice(axes_list)
        rotation = random.choice(rotations_list)
        perform_cube_operations(n, sides, cube_slice, axis, rotation)
