import copy
import random

import CubeConstants

random.seed(CubeConstants.seed)


def get_a_state_change():
    return_list = []
    for i in range(6):
        return_list.append(random.choice((0, 1)))
    return return_list


def get_a_state_change_with_probability(previous_list, slice_prob_param, axis_prob_param, rotation_prob_param):
    return_list = copy.deepcopy(previous_list)
    if random.random() > slice_prob_param:
        return_list[0] = random.choice((0, 1))
        return_list[1] = random.choice((0, 1))

    if random.random() > axis_prob_param:
        return_list[2] = random.choice((0, 1))
        return_list[3] = random.choice((0, 1))

    if random.random() > rotation_prob_param:
        return_list[4] = random.choice((0, 1))
        return_list[5] = random.choice((0, 1))

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
