import cube_constants as constants

cube_mapping_dictionary = {
    'x': {
        constants.rotating_sides: (0, 5),
        constants.moving_sides: {
            1: (1, 0),
            2: (-1, 1),
            3: (-1, 0),
            4: (1, 1)
        },
    },

    'y': {
        constants.rotating_sides: (1, 3),
        constants.moving_sides: {
            0: (-1, 0),
            4: (-1, 0),
            5: (-1, 0),
            2: (-1, 0)
        },
    },

    'z': {
        constants.rotating_sides: (2, 4),
        constants.moving_sides: {
            0: (1, 1),
            1: (1, 1),
            5: (-1, 1),
            3: (1, 1)
        },
    }
}
