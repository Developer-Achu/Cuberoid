import sys

from Chromosome import *
from DefineStates import *

random.seed(CubeConstants.seed)


class Cuberoid:
    def __init__(self, _configuration, _n, _chromosome_length, _population_size, _mutation_rate, _max_iterations,
                 _slice_change_probability, _axis_change_probability, _rotation_change_probability):
        self.population = []
        self.mating_pool = []
        self.updated_mating_pool = []
        self.best = None
        self.iteration = 0
        self.all_best_fitness = []
        self.iteration_list = []

        self.sides = _configuration
        self.n = _n
        self.chromosome_length = _chromosome_length
        self.population_size = _population_size
        self.mutation_rate = _mutation_rate
        self.max_iterations = _max_iterations
        self.slice_change_probability = _slice_change_probability
        self.axis_change_probability = _axis_change_probability
        self.rotation_change_probability = _rotation_change_probability

        self.init_population()

    def init_population(self):
        for i in range(0, self.population_size):
            chromosome = Chromosome(self.sides, self.chromosome_length, self.n)
            chromosome.compute_fitness()
            self.update_best_child(chromosome)
            self.population.append(chromosome)
        self.updated_mating_pool = self.population

    def update_best_child(self, child):
        if self.best is None or child.get_fitness() < self.best.get_fitness():
            self.best = child.get_chromosome_copy()
            self.all_best_fitness.append(self.best.get_fitness())
            self.iteration_list.append(self.iteration)
            sys.stdout.write(
                "\r%s%d%s%d%s" % ("Iteration : ", self.iteration, " Cost: ", self.best.get_fitness(), "\n"))
            sys.stdout.flush()

    def random_selection(self):
        parent_1 = self.mating_pool[random.randint(0, len(self.mating_pool) - 1)]
        parent_2 = self.mating_pool[random.randint(0, len(self.mating_pool) - 1)]
        return [parent_1, parent_2]

    def uniform_crossover(self, parent_1, parent_2):
        child = Chromosome(self.sides, self.chromosome_length, self.n)

        number_of_random_points = random.randint(int(self.chromosome_length / 4), int(self.chromosome_length / 2))
        random_indices = random.sample(range(self.chromosome_length), number_of_random_points)

        child.genes = parent_2.genes[:]
        for index in random_indices:
            child.genes[index] = parent_1.genes[index]

        return child

    def mutation(self, child):
        if random.random() < self.mutation_rate:
            if random.random() < 0.5:
                # random new gene
                random_index = random.randint(0, self.chromosome_length - 1)
                child.genes[random_index] = get_a_state_change()
            else:
                # flip a random bit on the gene
                random_index = random.randint(0, self.chromosome_length - 1)
                random_index_of_gene = random.randint(0, 5)
                child.genes[random_index][random_index_of_gene] = (1 - child.genes[random_index][random_index_of_gene])

        child.compute_fitness()
        self.update_best_child(child)

    def update_mating_pool(self):
        self.mating_pool = self.updated_mating_pool
        # self.mating_pool = self.population

        # for chromosome in self.population:
        #     count = ((((self.n ** 2) * 6) - chromosome.get_fitness()) * 10)
        #     for _ in range(0, count):
        #         self.mating_pool.append(chromosome)

    def create_new_generation(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            count = ((((self.n ** 2) * 6) - self.best.get_fitness()) * 10)
            for _ in range(0, count):
                self.updated_mating_pool.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.uniform_crossover(parents[0], parents[1])
            self.mutation(child)
            new_population.append(child)
            count = ((((self.n ** 2) * 6) - child.get_fitness()) * 10)
            for _ in range(0, count):
                self.updated_mating_pool.append(child)

        self.population = new_population

    def genetic_algorithm(self):
        self.update_mating_pool()
        self.create_new_generation()

    def solve(self):
        self.iteration = 0
        while self.best.get_fitness() != 0 and self.iteration < self.max_iterations:
            if self.iteration % 100 == 0:
                sys.stdout.write("\r%s%d" % ("Iteration : ", self.iteration))
                sys.stdout.flush()
            self.genetic_algorithm()
            self.iteration += 1

        self.all_best_fitness.append(self.best.get_fitness())
        print("\nPopulation size:", self.population_size)
        print("Total iterations: ", self.iteration)
        print("Best fitness: ", self.best.get_fitness())
        if self.best.get_fitness() == 0:
            print("Best solution moves: ", print_moves(self.best))
        print("=======================================")
        print("\n")


n = 3

if len(sys.argv) == 10:
    re_initializations = int(sys.argv[1])
    retry = int(sys.argv[2])
    chromosome_length = int(sys.argv[3])
    population_size = int(sys.argv[4])
    mutation_rate = float(sys.argv[5])
    iterations = int(sys.argv[6])
    slice_change_probability = float(sys.argv[7])
    axis_change_probability = float(sys.argv[8])
    rotation_change_probability = float(sys.argv[9])
else:
    print("Invalid argument count")
    exit(0)

# re_initializations = 1
# retry = 1
# chromosome_length = 20
# population_size = 100
# mutation_rate = 0.5
# iterations = 10
# slice_change_probability = 0.5
# axis_change_probability = 0.5
# rotation_change_probability = 0.5

file_name = str(n) + "x" + str(n) + ".npy"
read_dict = np.load(file_name, allow_pickle=True).item()
list_of_configurations = read_dict[CubeConstants.sides_dict_key]

for initialization in range(re_initializations):
    seed = CubeConstants.seed
    for r in range(retry):
        CubeConstants.seed = CubeConstants.seed + (r * 1000)
        print("seed value: " + str(CubeConstants.seed))
        print("retry: " + str(r))
        print("initialization: " + str(initialization))
        print("chromosome length: " + str(chromosome_length))
        print("\n")

        for configuration in list_of_configurations:
            cuberoid = Cuberoid(
                configuration,
                n,
                chromosome_length,
                population_size,
                mutation_rate,
                iterations,
                slice_change_probability,
                axis_change_probability,
                rotation_change_probability
            )
            cuberoid.solve()

    chromosome_length += 1
    CubeConstants.seed = seed
