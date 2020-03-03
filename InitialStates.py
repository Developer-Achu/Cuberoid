import sys

import numpy as np

from CubeRotations import perform_cube_operations
from DefineStates import *

random.seed(CubeConstants.seed)


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


if len(sys.argv) == 4:
    n = int(sys.argv[1])
    total_states = int(sys.argv[2])
    max_scramble_size = int(sys.argv[3])
else:
    print("Invalid argument count")
    exit(0)

'''
    Note: slice and rotation starts from 1
    sides are counted from 0
'''
define_state = DefineStates(n)

sides_list = []
with open(CubeConstants.moves_file_name, "w") as file:
    for state in range(total_states):
        moves_performed = []
        sides = generate_solved_cube_matrix(n)
        scramble_size = random.randint(1, max_scramble_size)
        for scramble in range(scramble_size):
            cube_slice, axis, rotation = define_state.get_a_state_change()
            if cube_slice != 0 and rotation != 0:
                moves_performed.append((cube_slice, axis, rotation))
                perform_cube_operations(n, sides, cube_slice, axis, rotation)
        file.write("\nstate: " + str(state))
        file.write("\nmoves: " + str(moves_performed))
        sides_list.append(sides)
file.close()

sides_dict = {CubeConstants.sides_dict_key: sides_list}
file_name = str(n) + "x" + str(n) + ".npy"
np.save(file_name, sides_dict)
