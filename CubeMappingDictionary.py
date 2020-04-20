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

# cube_mapping_dictionary = {
#     'x': {
#         constants.rotating_sides: (0, 5),
#         constants.moving_sides: {
#             1: (1, True, True, False, 2),
#             4: (1, False, True, True, 1),
#             3: (-1, True, True, False, 4),
#             2: (-1, False, True, True, 3),
#         },
#     },
#
#     'y': {
#         constants.rotating_sides: (1, 3),
#         constants.moving_sides: {
#             0: (-1, True, False, False, 4),
#             2: (-1, True, False, False, 0),
#             5: (-1, True, False, False, 2),
#             4: (-1, True, False, False, 5),
#         },
#     },
#
#     'z': {
#         constants.rotating_sides: (2, 4),
#         constants.moving_sides: {
#             0: (1, False, False, False, 1),
#             3: (1, False, False, False, 0),
#             5: (-1, False, False, True, 3),
#             1: (1, False, False, True, 5),
#         },[0]
#     }
# }

cube_mapping_dictionary = {
    1: {
        1: (0, 1),
        2: (None, 0),
        3: (5, 0),
        # constants.rotating_sides: (0, 5),
        constants.moving_sides: {
            1: (1, True, True, False, 2),
            4: (1, False, True, True, 1),
            3: (-1, True, True, False, 4),
            2: (-1, False, True, True, 3),
        },
    },

    2: {
        1: (1, 1),
        2: (None, 0),
        3: (3, 0),
        # constants.rotating_sides: (1, 3),
        constants.moving_sides: {
            0: (-1, True, False, False, 4),
            2: (-1, True, False, False, 0),
            5: (-1, True, False, False, 2),
            4: (-1, True, False, False, 5),
        },
    },

    3: {
        1: (2, 1),
        2: (None, 0),
        3: (4, 0),
        # constants.rotating_sides: (2, 4),
        constants.moving_sides: {
            0: (1, False, False, False, 1),
            3: (1, False, False, False, 0),
            5: (-1, False, False, True, 3),
            1: (1, False, False, True, 5),
        },
    }
}
