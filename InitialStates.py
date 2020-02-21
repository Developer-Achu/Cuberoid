import random

import numpy as np

from CubeRotations import rotate_cube

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

if n == 2:
    cube_slices_list = list(range(1, 3))
elif n == 3:
    cube_slices_list = list(range(1, 4))
elif n == 4:
    cube_slices_list = list(range(1, 5))
elif n == 5:
    cube_slices_list = list(range(1, 6))
else:
    cube_slices_list = []
    print("Invalid cube dimension")
    exit(0)

axes_list = ['x', 'y', 'z']
rotations_list = [90, 180, 270]
sides = generate_solved_cube_matrix(n)

for state in range(total_states):
    # scramble_size = random.randint(1, 100)
    scramble_size = 1
    for scramble in range(scramble_size):
        cube_slice = random.choice(cube_slices_list)
        axis = random.choice(axes_list)
        rotation = random.choice(rotations_list)
        rotate_cube(sides, cube_slice, axis, rotation)
