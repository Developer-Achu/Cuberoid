import numpy as np

from CubeRotations import perform_cube_operations
from DefineStates import *


class Chromosome:
    def __init__(self, _side_0, _side_1, _side_2, _side_3, _side_4, _side_5, _length, _n):
        self.fitness = 0
        self.sides = []
        self.genes = None

        self.side_0 = _side_0
        self.side_1 = _side_1
        self.side_2 = _side_2
        self.side_3 = _side_3
        self.side_4 = _side_4
        self.side_5 = _side_5
        self.chromosome_length = _length
        self.n = _n

        self.sides.append(np.reshape(self.side_0, (self.n, self.n)))
        self.sides.append(np.reshape(self.side_1, (self.n, self.n)))
        self.sides.append(np.reshape(self.side_2, (self.n, self.n)))
        self.sides.append(np.reshape(self.side_3, (self.n, self.n)))
        self.sides.append(np.reshape(self.side_4, (self.n, self.n)))
        self.sides.append(np.reshape(self.side_5, (self.n, self.n)))

        self.genes = get_n_state_change(self.chromosome_length)

    def compute_fitness(self):
        self.fitness = 0
        for i in range(0, len(self.genes), 6):
            cube_slice = get_cube_slice(self.genes[i], self.genes[i + 1])
            axis = get_cube_axis(self.genes[i + 2], self.genes[i + 3])
            rotation = get_cube_rotation(self.genes[i + 4], self.genes[i + 5])
            if cube_slice != 0 and axis is not None and rotation != 0:
                perform_cube_operations(self.n, self.sides, cube_slice, axis, rotation)

        for i in range(0, len(self.sides)):
            count_dict = dict(zip(*np.unique(self.sides[i], return_counts=True)))
            try:
                count = count_dict[i]
            except:
                count = 0
            self.fitness += ((self.n ** 2) - count)

    def get_fitness(self):
        return self.fitness

    def get_chromosome_copy(self):
        chromosome = Chromosome(self.side_0, self.side_1, self.side_2, self.side_3, self.side_4, self.side_5,
                                self.chromosome_length, self.n)
        chromosome.genes = self.genes[:]
        chromosome.fitness = self.get_fitness()
        return chromosome

    def set_genes(self, genes):
        self.genes = genes[:]
