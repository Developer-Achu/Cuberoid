import copy

import numpy as np

from CubeRotations import perform_cube_operations
from DefineStates import *


class Chromosome:
    def __init__(self, _sides, _length, _n):
        self.fitness = 0
        self.sides = _sides
        self.n = _n
        self.chromosome_length = _length
        self.define_states = DefineStates(_n)
        self.genes = np.empty(_length, dtype=tuple)

        for i in range(self.chromosome_length):
            cube_slice, axis, rotation = self.define_states.get_a_state_change()
            self.genes[i] = (cube_slice, axis, rotation)

    def compute_fitness(self):
        sides = copy.deepcopy(self.sides)
        for gene in self.genes:
            cube_slice = gene[0]
            axis = gene[1]
            rotation = gene[2]

            if cube_slice != 0 and rotation != 0:
                perform_cube_operations(self.n, sides, cube_slice, axis, rotation)

        for key in sides.keys():
            count_dict = dict(zip(*np.unique(sides[key], return_counts=True)))
            try:
                count = count_dict[key]
            except:
                count = 0
            self.fitness += ((self.n ** 2) - count)

    def get_fitness(self):
        return self.fitness

    def get_chromosome_copy(self):
        chromosome = Chromosome(self.sides, self.chromosome_length, self.n)
        chromosome.genes = np.copy(self.genes)
        chromosome.fitness = self.get_fitness()
        return chromosome

    def set_genes(self, genes):
        self.genes = np.copy(genes)
