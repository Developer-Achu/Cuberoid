import random

import CubeConstants

random.seed(CubeConstants.seed)


class DefineStates:
    def __init__(self, _n):
        self.cube_slices_list = list(range(1, (_n + 1)))
        self.axes_list = ['x', 'y', 'z']
        self.rotations_list = [1, 2, 3]

    def get_a_state_change(self):
        return random.choice(self.cube_slices_list), random.choice(self.axes_list), random.choice(self.rotations_list)
