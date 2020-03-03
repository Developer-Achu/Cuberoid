import CubeConstants as constants

'''
    for moving sides,
    2: (1, True, True, False, 3) => <side>: (<slice>, <is_row>, <take_transpose>, <do_flip>, <to_side>)
    For is_row:
        True => row-wise
        False => column-wise
    
    to_side represents the side to which the current side row goes
    
    ***** 
        NB: all the operations performing on slice n is counter-clockwise since the clockwise rotations are given to slice = 1
    *****
'''

cube_mapping_dictionary = {
    'x': {
        constants.rotating_sides: (1, 6),
        constants.moving_sides: {
            2: (1, True, True, False, 3),
            5: (1, False, True, True, 2),
            4: (-1, True, True, False, 5),
            3: (-1, False, True, True, 4),
        },
    },

    'y': {
        constants.rotating_sides: (2, 4),
        constants.moving_sides: {
            1: (-1, True, False, False, 5),
            3: (-1, True, False, False, 1),
            6: (-1, True, False, False, 3),
            5: (-1, True, False, False, 6),
        },
    },

    'z': {
        constants.rotating_sides: (3, 5),
        constants.moving_sides: {
            1: (1, False, False, False, 2),
            4: (1, False, False, False, 1),
            6: (-1, False, False, True, 4),
            2: (1, False, False, True, 6),
        },
    }
}
