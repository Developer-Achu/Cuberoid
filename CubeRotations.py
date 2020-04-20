import numpy as np

import CubeConstants as constants
from CubeMappingDictionary import cube_mapping_dictionary


def rotate_side(sides, rotating_side, rotation, is_clockwise):
    rotating_matrix = sides[rotating_side]

    for i in range(rotation):
        rotating_matrix = rotating_matrix.T
        rotating_matrix = np.flip(rotating_matrix, is_clockwise)

    sides[rotating_side] = rotating_matrix


def split_data(n, moving_side, cube_slice, is_all):
    if is_all:
        return moving_side[0] * cube_slice, moving_side[1], moving_side[2], moving_side[3], moving_side[4]
    else:
        return moving_side[0] * cube_slice, moving_side[1]


def get_side_slice(is_row, _slice, side):
    if is_row:
        if _slice > 0:
            side_slice = side[(_slice - 1):_slice, :]
        elif _slice < -1:
            side_slice = side[_slice:(_slice + 1), :]
        else:
            side_slice = side[-1:, :]
    else:
        if _slice > 0:
            side_slice = side[:, (_slice - 1):_slice]
        elif _slice < -1:
            side_slice = side[:, _slice:(_slice + 1)]
        else:
            side_slice = side[:, -1:]

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
    for i in range(rotation):
        is_first_key = True
        first_key = 0
        first_side = np.zeros((n, n))

        for key in moving_sides.keys():
            moving_side = moving_sides[key]
            if is_first_key:
                is_first_key = False
                first_key = key
                first_side = np.copy(sides[key])
            else:
                _slice, is_row, take_transpose, do_flip, to_side = split_data(n, moving_side, cube_slice, True)
                side_slice = get_side_slice(is_row, _slice, sides[key])
                if take_transpose:
                    side_slice = side_slice.T
                if do_flip:
                    side_slice = np.flip(side_slice)
                inserting_slice, inserting_is_row = split_data(n, moving_sides[to_side], cube_slice, False)
                insert_side_slice(sides, inserting_slice, inserting_is_row, side_slice, to_side)

        _slice, is_row, take_transpose, do_flip, to_side = split_data(n, moving_sides[first_key], cube_slice, True)
        side_slice = get_side_slice(is_row, _slice, first_side)
        if take_transpose:
            side_slice = side_slice.T
        if do_flip:
            side_slice = np.flip(side_slice)
        inserting_slice, inserting_is_row = split_data(n, moving_sides[to_side], cube_slice, False)
        insert_side_slice(sides, inserting_slice, inserting_is_row, side_slice, to_side)


def perform_cube_operations(n, sides, cube_slice, axis, rotation):
    cube_map = cube_mapping_dictionary[axis]
    side_direction_tuple = cube_map[cube_slice]
    rotating_side = side_direction_tuple[0]
    is_clockwise = side_direction_tuple[1]

    if rotating_side is not None:
        rotate_side(sides, rotating_side, rotation, is_clockwise)

    moving_sides = cube_map[constants.moving_sides]
    move_colors(n, sides, moving_sides, cube_slice, rotation)
