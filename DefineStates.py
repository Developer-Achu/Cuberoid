import random

import CubeConstants

random.seed(CubeConstants.seed)


def get_a_state_change():
    return_list = []
    for i in range(6):
        return_list.append(random.choice((0, 1)))
    return return_list


# def get_cube_slice(v1, v2):
#     return (v1 * 2) + v2


# def get_cube_axis(v1, v2):
#     return (v1 * 2) + v2


# def get_cube_rotation(v1, v2):
#     return (v1 * 2) + v2


def print_moves(genes):
    converted_moves = []
    for move in genes:
        cube_slice = (move[0] * 2) + move[1]
        axis = (move[2] * 2) + move[3]
        rotation = (move[4] * 2) + move[5]
        if cube_slice != 0 and axis != 0 and rotation != 0:
            converted_moves.append((cube_slice, axis, rotation))
    return converted_moves
