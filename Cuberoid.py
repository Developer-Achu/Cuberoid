import sys

from Chromosome import *
from DefineStates import *

random.seed(CubeConstants.seed)


class Cuberoid:
    def __init__(self, _configuration, _n, _chromosome_length, _population_size, _mutation_rate, _max_iterations,
                 _slice_change_probability, _axis_change_probability, _rotation_change_probability,
                 _config_combination):
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
        self.config_combination = _config_combination

        self.init_population()

    def init_population(self):
        for i in range(0, self.population_size):
            chromosome = Chromosome(self.sides, self.chromosome_length, self.n)
            chromosome.compute_fitness()
            self.update_best_child(chromosome)
            self.population.append(chromosome)

        if self.config_combination < 10:
            for i in range(self.population_size):
                count = ((((self.n ** 2) * 6) - self.population[i].get_fitness()) * 100)
                for _ in range(0, count):
                    self.updated_mating_pool.append(self.population[i])
        else:
            for i in range(self.population_size):
                chromosome_1 = self.population[random.randint(0, self.population_size - 1)]
                chromosome_2 = self.population[random.randint(0, self.population_size - 1)]
                if chromosome_1.get_fitness() > chromosome_2.get_fitness():
                    self.updated_mating_pool.append(chromosome_1)
                else:
                    self.updated_mating_pool.append(chromosome_2)

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

    def one_point_crossover(self, parent_1, parent_2):
        child = Chromosome(self.sides, self.chromosome_length, self.n)

        random_point = random.randint(0, self.chromosome_length - 1)
        child.genes = parent_1.genes[:]

        for i in range(random_point, self.chromosome_length):
            child.genes[i] = parent_2.genes[i]

        return child

    def two_point_crossover(self, parent_1, parent_2):
        child = Chromosome(self.sides, self.chromosome_length, self.n)

        random_indices = random.sample(range(self.chromosome_length), 2)
        start_index = min(random_indices)
        end_index = max(random_indices)

        child.genes = parent_1.genes[:]

        for i in range(start_index, end_index + 1):
            child.genes[i] = parent_2.genes[i]

        return child

    def uniform_crossover(self, parent_1, parent_2):
        child = Chromosome(self.sides, self.chromosome_length, self.n)

        number_of_random_points = random.randint(int(self.chromosome_length / 4), int(self.chromosome_length / 2) - 1)
        random_indices = random.sample(range(self.chromosome_length), number_of_random_points)

        child.genes = parent_1.genes[:]
        for index in random_indices:
            child.genes[index] = parent_2.genes[index]

        return child

    def random_mutation(self, child):
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

    def inversion_mutation(self, child):
        if random.random() < self.mutation_rate:
            random_indices = random.sample(range(self.chromosome_length), 2)
            start_index = min(random_indices)
            end_index = max(random_indices)

            child.genes[start_index:end_index + 1] = child.genes[start_index:end_index + 1][::-1]

        child.compute_fitness()
        self.update_best_child(child)

    def scramble_mutation(self, child):
        if random.random() < self.mutation_rate:
            random_indices = random.sample(range(self.chromosome_length), 2)
            start_index = min(random_indices)
            end_index = max(random_indices)
            indices_list = list(range(start_index, end_index + 1))
            random.shuffle(indices_list)
            new_gene = child.genes[:]
            for index in range(start_index, end_index + 1):
                new_gene[index] = child.genes[indices_list[index - start_index]]
            child.set_genes(new_gene)

        child.compute_fitness()
        self.update_best_child(child)

    def update_mating_pool(self):
        self.mating_pool = self.updated_mating_pool

    def config_1(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            count = ((((self.n ** 2) * 6) - self.best.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.one_point_crossover(parents[0], parents[1])
            self.random_mutation(child)
            new_population.append(child)
            count = ((((self.n ** 2) * 6) - child.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(child)

        self.population = new_population

    def config_2(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            count = ((((self.n ** 2) * 6) - self.best.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.one_point_crossover(parents[0], parents[1])
            self.inversion_mutation(child)
            new_population.append(child)
            count = ((((self.n ** 2) * 6) - child.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(child)

        self.population = new_population

    def config_3(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            count = ((((self.n ** 2) * 6) - self.best.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.one_point_crossover(parents[0], parents[1])
            self.scramble_mutation(child)
            new_population.append(child)
            count = ((((self.n ** 2) * 6) - child.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(child)

        self.population = new_population

    def config_4(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            count = ((((self.n ** 2) * 6) - self.best.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.two_point_crossover(parents[0], parents[1])
            self.random_mutation(child)
            new_population.append(child)
            count = ((((self.n ** 2) * 6) - child.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(child)

        self.population = new_population

    def config_5(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            count = ((((self.n ** 2) * 6) - self.best.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.two_point_crossover(parents[0], parents[1])
            self.inversion_mutation(child)
            new_population.append(child)
            count = ((((self.n ** 2) * 6) - child.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(child)

        self.population = new_population

    def config_6(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            count = ((((self.n ** 2) * 6) - self.best.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.two_point_crossover(parents[0], parents[1])
            self.scramble_mutation(child)
            new_population.append(child)
            count = ((((self.n ** 2) * 6) - child.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(child)

        self.population = new_population

    def config_7(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            count = ((((self.n ** 2) * 6) - self.best.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.uniform_crossover(parents[0], parents[1])
            self.random_mutation(child)
            new_population.append(child)
            count = ((((self.n ** 2) * 6) - child.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(child)

        self.population = new_population

    def config_8(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            count = ((((self.n ** 2) * 6) - self.best.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.uniform_crossover(parents[0], parents[1])
            self.inversion_mutation(child)
            new_population.append(child)
            count = ((((self.n ** 2) * 6) - child.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(child)

        self.population = new_population

    def config_9(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            count = ((((self.n ** 2) * 6) - self.best.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.uniform_crossover(parents[0], parents[1])
            self.scramble_mutation(child)
            new_population.append(child)
            count = ((((self.n ** 2) * 6) - child.get_fitness()) * 100)
            for _ in range(0, count):
                self.updated_mating_pool.append(child)

        self.population = new_population

    def config_10(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.one_point_crossover(parents[0], parents[1])
            self.random_mutation(child)
            new_population.append(child)

        self.population = new_population

        for i in range(self.population_size):
            chromosome_1 = self.population[random.randint(0, self.population_size - 1)]
            chromosome_2 = self.population[random.randint(0, self.population_size - 1)]
            if chromosome_1.get_fitness() > chromosome_2.get_fitness():
                self.updated_mating_pool.append(chromosome_1)
            else:
                self.updated_mating_pool.append(chromosome_2)

    def config_11(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.one_point_crossover(parents[0], parents[1])
            self.inversion_mutation(child)
            new_population.append(child)

        self.population = new_population

        for i in range(self.population_size):
            chromosome_1 = self.population[random.randint(0, self.population_size - 1)]
            chromosome_2 = self.population[random.randint(0, self.population_size - 1)]
            if chromosome_1.get_fitness() > chromosome_2.get_fitness():
                self.updated_mating_pool.append(chromosome_1)
            else:
                self.updated_mating_pool.append(chromosome_2)

    def config_12(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.one_point_crossover(parents[0], parents[1])
            self.scramble_mutation(child)
            new_population.append(child)

        self.population = new_population

        for i in range(self.population_size):
            chromosome_1 = self.population[random.randint(0, self.population_size - 1)]
            chromosome_2 = self.population[random.randint(0, self.population_size - 1)]
            if chromosome_1.get_fitness() > chromosome_2.get_fitness():
                self.updated_mating_pool.append(chromosome_1)
            else:
                self.updated_mating_pool.append(chromosome_2)

    def config_13(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.two_point_crossover(parents[0], parents[1])
            self.random_mutation(child)
            new_population.append(child)

        self.population = new_population

        for i in range(self.population_size):
            chromosome_1 = self.population[random.randint(0, self.population_size - 1)]
            chromosome_2 = self.population[random.randint(0, self.population_size - 1)]
            if chromosome_1.get_fitness() > chromosome_2.get_fitness():
                self.updated_mating_pool.append(chromosome_1)
            else:
                self.updated_mating_pool.append(chromosome_2)

    def config_14(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.two_point_crossover(parents[0], parents[1])
            self.inversion_mutation(child)
            new_population.append(child)

        self.population = new_population

        for i in range(self.population_size):
            chromosome_1 = self.population[random.randint(0, self.population_size - 1)]
            chromosome_2 = self.population[random.randint(0, self.population_size - 1)]
            if chromosome_1.get_fitness() > chromosome_2.get_fitness():
                self.updated_mating_pool.append(chromosome_1)
            else:
                self.updated_mating_pool.append(chromosome_2)

    def config_15(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.two_point_crossover(parents[0], parents[1])
            self.scramble_mutation(child)
            new_population.append(child)

        self.population = new_population

        for i in range(self.population_size):
            chromosome_1 = self.population[random.randint(0, self.population_size - 1)]
            chromosome_2 = self.population[random.randint(0, self.population_size - 1)]
            if chromosome_1.get_fitness() > chromosome_2.get_fitness():
                self.updated_mating_pool.append(chromosome_1)
            else:
                self.updated_mating_pool.append(chromosome_2)

    def config_16(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.uniform_crossover(parents[0], parents[1])
            self.random_mutation(child)
            new_population.append(child)

        self.population = new_population

        for i in range(self.population_size):
            chromosome_1 = self.population[random.randint(0, self.population_size - 1)]
            chromosome_2 = self.population[random.randint(0, self.population_size - 1)]
            if chromosome_1.get_fitness() > chromosome_2.get_fitness():
                self.updated_mating_pool.append(chromosome_1)
            else:
                self.updated_mating_pool.append(chromosome_2)

    def config_17(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.uniform_crossover(parents[0], parents[1])
            self.inversion_mutation(child)
            new_population.append(child)

        self.population = new_population

        for i in range(self.population_size):
            chromosome_1 = self.population[random.randint(0, self.population_size - 1)]
            chromosome_2 = self.population[random.randint(0, self.population_size - 1)]
            if chromosome_1.get_fitness() > chromosome_2.get_fitness():
                self.updated_mating_pool.append(chromosome_1)
            else:
                self.updated_mating_pool.append(chromosome_2)

    def config_18(self):
        length = self.population_size

        new_population = []
        self.updated_mating_pool = []

        if self.best is not None:
            new_population.append(self.best)
            length -= 1

        for _ in range(length):
            parents = self.random_selection()
            child = self.uniform_crossover(parents[0], parents[1])
            self.scramble_mutation(child)
            new_population.append(child)

        self.population = new_population

        for i in range(self.population_size):
            chromosome_1 = self.population[random.randint(0, self.population_size - 1)]
            chromosome_2 = self.population[random.randint(0, self.population_size - 1)]
            if chromosome_1.get_fitness() > chromosome_2.get_fitness():
                self.updated_mating_pool.append(chromosome_1)
            else:
                self.updated_mating_pool.append(chromosome_2)

    def create_new_generation(self):
        if config_combination == 1:
            self.config_1()
        elif config_combination == 2:
            self.config_2()
        elif config_combination == 3:
            self.config_3()
        elif config_combination == 4:
            self.config_4()
        elif config_combination == 5:
            self.config_5()
        elif config_combination == 6:
            self.config_6()
        elif config_combination == 7:
            self.config_7()
        elif config_combination == 8:
            self.config_8()
        elif config_combination == 9:
            self.config_9()
        elif config_combination == 10:
            self.config_10()
        elif config_combination == 11:
            self.config_11()
        elif config_combination == 12:
            self.config_12()
        elif config_combination == 13:
            self.config_13()
        elif config_combination == 14:
            self.config_14()
        elif config_combination == 15:
            self.config_15()
        elif config_combination == 16:
            self.config_16()
        elif config_combination == 17:
            self.config_17()
        elif config_combination == 18:
            self.config_18()

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

        return self.best.get_fitness() == 0


n = 3

if len(sys.argv) == 11:
    re_initializations = int(sys.argv[1])
    retry = int(sys.argv[2])
    chromosome_length = int(sys.argv[3])
    population_size = int(sys.argv[4])
    mutation_rate = float(sys.argv[5])
    iterations = int(sys.argv[6])
    slice_change_probability = float(sys.argv[7])
    axis_change_probability = float(sys.argv[8])
    rotation_change_probability = float(sys.argv[9])
    config_combination = int(sys.argv[10])
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
# config_combination = 1

if config_combination == 1:
    print("Roulette selection --> one-point crossover --> random mutation")
elif config_combination == 2:
    print("Roulette selection --> one-point crossover --> inversion mutation")
elif config_combination == 3:
    print("Roulette selection --> one-point crossover --> scramble mutation")
elif config_combination == 4:
    print("Roulette selection --> two-point crossover --> random mutation")
elif config_combination == 5:
    print("Roulette selection --> two-point crossover --> inversion mutation")
elif config_combination == 6:
    print("Roulette selection --> two-point crossover --> scramble mutation")
elif config_combination == 7:
    print("Roulette selection --> uniform crossover --> random mutation")
elif config_combination == 8:
    print("Roulette selection --> uniform crossover --> inversion mutation")
elif config_combination == 9:
    print("Roulette selection --> uniform crossover --> scramble mutation")
elif config_combination == 10:
    print("Tournament selection --> one-point crossover --> random mutation")
elif config_combination == 11:
    print("Tournament selection --> one-point crossover --> inversion mutation")
elif config_combination == 12:
    print("Tournament selection --> one-point crossover --> scramble mutation")
elif config_combination == 13:
    print("Tournament selection --> two-point crossover --> random mutation")
elif config_combination == 14:
    print("Tournament selection --> two-point crossover --> inversion mutation")
elif config_combination == 15:
    print("Tournament selection --> two-point crossover --> scramble mutation")
elif config_combination == 16:
    print("Tournament selection --> uniform crossover --> random mutation")
elif config_combination == 17:
    print("Tournament selection --> uniform crossover --> inversion mutation")
elif config_combination == 18:
    print("Tournament selection --> uniform crossover --> scramble mutation")

file_name = str(n) + "x" + str(n) + ".npy"
read_dict = np.load(file_name, allow_pickle=True).item()
list_of_configurations = read_dict[CubeConstants.sides_dict_key]

for configuration in list_of_configurations:
    cube_solved = False
    for initialization in range(re_initializations):
        CubeConstants.seed = CubeConstants.seed + (initialization * 1000)
        print("initialization: " + str(initialization))
        print("seed value: " + str(CubeConstants.seed))
        for r in range(retry):
            print("retry: " + str(r))
            print("chromosome length: " + str(chromosome_length))
            print("\n")

            cuberoid = Cuberoid(
                configuration,
                n,
                chromosome_length,
                population_size,
                mutation_rate,
                iterations,
                slice_change_probability,
                axis_change_probability,
                rotation_change_probability,
                config_combination
            )
            cube_solved = cuberoid.solve()
            if cube_solved:
                break

        if cube_solved:
            break
