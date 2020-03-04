from Chromosome import *
from DefineStates import *

random.seed(CubeConstants.seed)


class Cuberoid:
    def __init__(self, _configuration, _n, _chromosome_length, _population_size, _mutation_rate, _max_iterations,
                 _slice_change_probability, _axis_change_probability, _rotation_change_probability):
        self.population = np.empty(_population_size, dtype=Chromosome)
        self.mating_pool = np.empty(_population_size, dtype=Chromosome)
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
        self.slice_change_probability = slice_change_probability
        self.axis_change_probability = _axis_change_probability
        self.rotation_change_probability = _rotation_change_probability

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

    def update_best_child(self, child):
        if self.best is None or child.get_fitness() < self.best.get_fitness():
            self.best = child.get_chromosome_copy()
            self.all_best_fitness.append(self.best.get_fitness())
            self.iteration_list.append(self.iteration)
            print("Iteration: ", self.iteration, " Cost: ", self.best.get_fitness())

    def random_selection(self):
        parent_1 = self.mating_pool[random.randint(0, self.population_size - 1)]
        parent_2 = self.mating_pool[random.randint(0, self.population_size - 1)]
        return [parent_1, parent_2]

    def uniform_crossover(self, parent_1, parent_2):
        number_of_random_points = random.randint(int(self.chromosome_length / 4), int(self.chromosome_length / 2))
        random_indices = random.sample(range(self.chromosome_length), number_of_random_points)

        child_1 = copy.deepcopy(parent_2)
        child_2 = copy.deepcopy(parent_1)

        child_1.genes[random_indices] = parent_1.genes[random_indices]
        child_2.genes[random_indices] = parent_2.genes[random_indices]

        return random.choice((child_1, child_2))

    def inversion_mutation(self, child):
        if random.random() > self.mutation_rate:
            return
        else:
            random_indices = random.sample(range(self.chromosome_length), 2)
            start_index = min(random_indices)
            end_index = max(random_indices)
            child.genes[start_index:end_index + 1] = child.genes[start_index:end_index + 1][::-1]

            child.compute_fitness()
            self.update_best_child(child)

    def update_mating_pool(self):
        self.mating_pool = np.copy(self.population)

    def create_new_generation(self):
        new_population = np.empty(self.population_size, dtype=Chromosome)

        for length in range(self.population_size):
            parents = self.random_selection()
            child = self.uniform_crossover(parents[0], parents[1])
            self.inversion_mutation(child)
            new_population[length] = child

        self.population = np.copy(new_population)

    def genetic_algorithm(self):
        self.update_mating_pool()
        self.create_new_generation()

    def solve(self):
        self.iteration = 0
        while self.iteration < self.max_iterations:
            self.genetic_algorithm()
            self.iteration += 1

        self.all_best_fitness.append(self.best.get_fitness())
        print("Population size:", self.population_size)
        print("Total iterations: ", self.iteration)
        print("Best fitness: ", self.best.get_fitness())
        # print("Best solution moves: ", self.best.genes)
        print("=======================================")
        print("\n")


n = 3
re_initializations = 10
retry = 10
chromosome_length = 25
population_size = 250
mutation_rate = 0.4
iterations = 1000
slice_change_probability = 0.4
axis_change_probability = 0.4
rotation_change_probability = 0.4

# re_initializations = 1
# chromosome_length = 20
# population_size = 10
# mutation_rate = 0.4
# iterations = 1
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
    CubeConstants.seed = seed
