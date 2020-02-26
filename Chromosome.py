from CubeRotations import perform_cube_operations
from DefineStates import *


class Chromosome:
    def __init__(self, _sides, _length, _n):
        self.fitness = 0
        self.sides = _sides
        self.n = _n
        self.chromosome_length = _length
        self.define_states = DefineStates(_n)
        self.genes = []

        for i in range(self.chromosome_length):
            cube_slice, axis, rotation = self.define_states.get_a_state_change()
            self.genes.append((cube_slice, axis, rotation))

    def compute_fitness(self):
        sides = self.sides.copy()
        for gene in self.genes:
            cube_slice = gene[0]
            axis = gene[1]
            rotation = gene[2]
            perform_cube_operations(self.n, sides, cube_slice, axis, rotation)
        print(self.sides)

    def get_fitness(self):
        return self.fitness

    def copy(self):
        chromosome = Chromosome(self.sides, self.chromosome_length, self.n)
        chromosome.genes = self.genes.copy()
        chromosome.fitness = self.get_fitness()
        return chromosome

    def set_genes(self, genes):
        self.genes = genes.copy()
