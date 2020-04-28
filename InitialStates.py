import pickle
import sys

import numpy as np

from CubeRotations import perform_cube_operations
from DefineStates import *

random.seed(CubeConstants.seed)


def convert_sides(_sides):
    flattened_list = []
    for _side in _sides:
        flattened_list.append(_side.flatten().tolist())

    return flattened_list


if len(sys.argv) == 3:
    # n = int(sys.argv[1])
    total_states = int(sys.argv[1])
    max_scramble_size = int(sys.argv[2])
else:
    print("Invalid argument count")
    exit(0)

'''
    Note: slice and rotation starts from 1
    sides are counted from 0
'''

n = 3
sides_list = []

states = []  #
list_of_sides = []
for state in range(total_states):
    details = []  #
    moves = []  #

    sides = []
    actual_moves = 0  #

    sides.append(np.reshape([0 for _ in range(n ** 2)], (n, n)))
    sides.append(np.reshape([1 for _ in range(n ** 2)], (n, n)))
    sides.append(np.reshape([2 for _ in range(n ** 2)], (n, n)))
    sides.append(np.reshape([3 for _ in range(n ** 2)], (n, n)))
    sides.append(np.reshape([4 for _ in range(n ** 2)], (n, n)))
    sides.append(np.reshape([5 for _ in range(n ** 2)], (n, n)))

    scramble_size = random.randint(1, max_scramble_size)
    for scramble in range(scramble_size):
        cube_parameters = get_a_state_change()
        cube_slice = (cube_parameters[0] * 2) + cube_parameters[1]
        axis = (cube_parameters[2] * 2) + cube_parameters[3]
        rotation = (cube_parameters[4] * 2) + cube_parameters[5]
        if cube_slice != 0 and axis != 0 and rotation != 0:
            actual_moves += 1  #
            moves.append((cube_slice, axis, rotation))  #
            perform_cube_operations(n, sides, cube_slice, axis, rotation)
    details.append("state: " + str(state))  #
    details.append("max scrambles: " + str(scramble_size))  #
    details.append("actual moves: " + str(actual_moves))  #
    details.append("moves: " + str(moves))  #
    states.append(details)  #
    list_of_sides.append(convert_sides(sides))

file_name = str(n) + "x" + str(n)
with open(file_name, "wb") as file:
    pickle.dump(list_of_sides, file)
file.close()

#
with open(CubeConstants.moves_file_name, "w") as file:
    for state in states:
        file.write("\n" + str(state[0]))
        file.write("\n" + str(state[1]))
        file.write("\n" + str(state[2]))
        file.write("\n" + str(state[3]) + "\n")
file.close()
#
