from Chromosome import *
from DefineStates import *

random.seed(CubeConstants.seed)


class Cuberoid:
    def __init__(self, _configuration, _n, _chromosome_length, _population_size, _mutation_rate, _max_iterations):
        self.population = np.empty(_population_size, dtype=Chromosome)
        self.mating_pool = np.empty(_population_size, dtype=Chromosome)
        self.best = None
        self.n = _n
        self.chromosome_length = _chromosome_length
        self.population_size = _population_size
        self.mutation_rate = _mutation_rate
        self.max_iterations = _max_iterations
        self.iteration = 0
        self.sides = _configuration
        self.all_best_fitness = []

        self.init_population()

    def init_population(self):
        for i in range(self.population_size):
            chromosome = Chromosome(self.sides, self.chromosome_length, self.n)
            chromosome.compute_fitness()
            self.population[i] = chromosome

            if i == 0:
                self.best = self.population[i].get_chromosome_copy()
            else:
                if chromosome.get_fitness() < self.best.get_fitness():
                    self.best = chromosome.get_chromosome_copy()


n = 3
file_name = str(n) + "x" + str(n) + ".npy"
read_dict = np.load(file_name, allow_pickle=True).item()
list_of_configurations = read_dict[CubeConstants.sides_dict_key]

for configuration in list_of_configurations:
    cuberoid = Cuberoid(configuration, n, 20, 100, 0.4, 1000)
