import random

import CubeConstants

random.seed(CubeConstants.seed)


def get_a_state_change():
    return_list = []
    for i in range(6):
        return_list.append(random.choice((0, 1)))
    return return_list


def get_cube_slice(v1, v2):
    if v1 == 0:
        if v2 == 0:
            return 1
        else:
            return 2
    else:
        if v2 == 0:
            return 3
        else:
            return 0


def get_cube_axis(v1, v2):
    if v1 == 0:
        if v2 == 0:
            return 'x'
        else:
            return 'y'
    else:
        if v2 == 0:
            return 'z'
        else:
            return None


def get_cube_rotation(v1, v2):
    if v1 == 0:
        if v2 == 0:
            return 1
        else:
            return 2
    else:
        if v2 == 0:
            return 3
        else:
            return 0


def print_moves(genes):
    converted_moves = []
    for move in genes:
        cube_slice = get_cube_slice(move[0], move[1])
        axis = get_cube_axis(move[2], move[3])
        rotation = get_cube_rotation(move[4], move[5])
        if cube_slice != 0 and axis is not None and rotation != 0:
            converted_moves.append((cube_slice, axis, rotation))
    print(converted_moves)
