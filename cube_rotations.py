import numpy as np

import cube_constants as constants
from cube_mapping_dictionary import cube_mapping_dictionary


def rotate_side(sides, rotating_side, rotation, is_clockwise):
    rotating_matrix = sides[rotating_side]
    if is_clockwise:
        for i in range(rotation):
            rotating_matrix = rotating_matrix.T
            rotating_matrix = np.flip(rotating_matrix, 1)
    else:
        for i in range(rotation):
            rotating_matrix = np.flip(rotating_matrix, 1)
            rotating_matrix = rotating_matrix.T

    sides[rotating_side] = rotating_matrix


def split_data(n, moving_side, cube_slice, is_all):
    if is_all:
        return moving_side[0] * cube_slice, moving_side[1], moving_side[2], moving_side[3], moving_side[4]
    else:
        return moving_side[0] * cube_slice, moving_side[1]


def get_side_slice(is_row, _slice, sides, key):
    if is_row:
        if _slice > 0:
            side_slice = sides[key][(_slice - 1):_slice, :]
        elif _slice < -1:
            side_slice = sides[key][_slice:(_slice + 1), :]
        else:
            side_slice = sides[key][-1:, :]
    else:
        if _slice > 0:
            side_slice = sides[key][:, (_slice - 1):_slice]
        elif _slice < -1:
            side_slice = sides[key][:, _slice:(_slice + 1)]
        else:
            side_slice = sides[key][:, -1:]

    return side_slice


def insert_side_slice(sides, inserting_slice, inserting_is_row, side_slice, to_side):
    if inserting_is_row:
        if inserting_slice > 0:
            sides[to_side][(inserting_slice - 1): inserting_slice, :] = side_slice
        elif inserting_slice < -1:
            sides[to_side][inserting_slice:(inserting_slice + 1), :] = side_slice
        else:
            sides[to_side][-1:, :] = side_slice
    else:
        if inserting_slice > 0:
            sides[to_side][:, (inserting_slice - 1): inserting_slice] = side_slice
        elif inserting_slice < -1:
            sides[to_side][:, inserting_slice:(inserting_slice + 1)] = side_slice
        else:
            sides[to_side][:, -1:] = side_slice


def move_colors(n, sides, moving_sides, cube_slice, rotation):
    is_first_key = True
    first_key = 0

    for key in moving_sides.keys():
        moving_side = moving_sides[key]
        if is_first_key:
            is_first_key = False
            first_key = key
        else:
            _slice, is_row, take_transpose, do_flip, to_side = split_data(n, moving_side, cube_slice, True)
            side_slice = get_side_slice(is_row, _slice, sides, key)
            if take_transpose:
                side_slice = side_slice.T
            if do_flip:
                side_slice = np.flip(side_slice)
            inserting_slice, inserting_is_row = split_data(n, moving_sides[to_side], cube_slice, False)
            insert_side_slice(sides, inserting_slice, inserting_is_row, side_slice, to_side)


def perform_cube_operations(n, sides, cube_slice, axis, rotation):
    is_clockwise = False
    cube_map = cube_mapping_dictionary[axis]

    if cube_slice == 1:
        rotating_side = cube_map[constants.rotating_sides][0]
        is_clockwise = True
    elif cube_slice == n:
        rotating_side = cube_map[constants.rotating_sides][1]
    else:
        rotating_side = None

    if rotating_side is not None:
        pass
        # rotate_side(sides, rotating_side, rotation, is_clockwise)

    moving_sides = cube_map[constants.moving_sides]
    move_colors(n, sides, moving_sides, cube_slice, rotation)
