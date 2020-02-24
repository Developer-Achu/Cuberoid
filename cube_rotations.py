import numpy as np

import cube_constants as constants
from cube_mapping_dictionary import cube_mapping_dictionary


def rotate_side(sides, rotating_side, rotation):
    rotating_matrix = sides[rotating_side]
    for i in range(rotation):
        np.flip(rotating_matrix.T, 1)


def move_colors():
    pass


def perform_cube_operations(n, sides, cube_slice, axis, rotation):
    cube_map = cube_mapping_dictionary[axis]
    if cube_slice == 1:
        rotating_side = cube_map[constants.rotating_sides][0]
    elif cube_slice == n:
        rotating_side = cube_map[constants.rotating_sides][1]
    else:
        rotating_side = None
    if rotating_side is not None:
        rotate_side(sides, rotating_side, rotation)
