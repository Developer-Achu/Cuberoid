import os
import pickle
import sys

import matplotlib.pyplot as plt

from Chromosome import *
from DefineStates import *

random.seed(CubeConstants.seed)


class Cuberoid:
    def __init__(self, _configuration, _n, _chromosome_length, _population_size, _mutation_rate, _max_iterations,
                 _elite, _config_combination):
        self.population = []
        self.initial_population = []
        self.mating_pool = []
        self.updated_mating_pool = []
        self.best = None
        self.best_iteration = 0
        self.iteration = 0
        self.all_best_fitness = []
        self.iteration_list = []
        self.all_avg_fitness = []
        self.each_best_fitness = []

        self.side_0 = _configuration[0]
        self.side_1 = _configuration[1]
        self.side_2 = _configuration[2]
        self.side_3 = _configuration[3]
        self.side_4 = _configuration[4]
        self.side_5 = _configuration[5]
        self.n = _n
        self.chromosome_length = _chromosome_length
        self.population_size = _population_size
        self.mutation_rate = _mutation_rate
        self.max_iterations = _max_iterations
        self.elite = _elite
        self.config_combination = _config_combination
        self.config_dict = {
            1: (self.roulette_wheel, self.one_point_crossover, self.random_mutation),
            2: (self.roulette_wheel, self.one_point_crossover, self.inversion_mutation),
            3: (self.roulette_wheel, self.one_point_crossover, self.scramble_mutation),
            4: (self.roulette_wheel, self.two_point_crossover, self.random_mutation),
            5: (self.roulette_wheel, self.two_point_crossover, self.inversion_mutation),
            6: (self.roulette_wheel, self.two_point_crossover, self.scramble_mutation),
            7: (self.roulette_wheel, self.uniform_crossover, self.random_mutation),
            8: (self.roulette_wheel, self.uniform_crossover, self.inversion_mutation),
            9: (self.roulette_wheel, self.uniform_crossover, self.scramble_mutation),
            10: (self.tournament, self.one_point_crossover, self.random_mutation),
            11: (self.tournament, self.one_point_crossover, self.inversion_mutation),
            12: (self.tournament, self.one_point_crossover, self.scramble_mutation),
            13: (self.tournament, self.two_point_crossover, self.random_mutation),
            14: (self.tournament, self.two_point_crossover, self.inversion_mutation),
            15: (self.tournament, self.two_point_crossover, self.scramble_mutation),
            16: (self.tournament, self.uniform_crossover, self.random_mutation),
            17: (self.tournament, self.uniform_crossover, self.inversion_mutation),
            18: (self.tournament, self.uniform_crossover, self.scramble_mutation),
            19: (self.no_selection, self.one_point_crossover, self.random_mutation),
            20: (self.no_selection, self.one_point_crossover, self.inversion_mutation),
            21: (self.no_selection, self.one_point_crossover, self.scramble_mutation),
            22: (self.no_selection, self.two_point_crossover, self.random_mutation),
            23: (self.no_selection, self.two_point_crossover, self.inversion_mutation),
            24: (self.no_selection, self.two_point_crossover, self.scramble_mutation),
            25: (self.no_selection, self.uniform_crossover, self.random_mutation),
            26: (self.no_selection, self.uniform_crossover, self.inversion_mutation),
            27: (self.no_selection, self.uniform_crossover, self.scramble_mutation)
        }
        self.mating_pool_updation = self.config_dict[self.config_combination][0]
        self.crossover = self.config_dict[self.config_combination][1]
        self.mutation = self.config_dict[self.config_combination][2]

        self.create_population()

    def create_population(self):
        for i in range(0, self.population_size):
            chromosome = Chromosome(self.side_0, self.side_1, self.side_2, self.side_3, self.side_4, self.side_5,
                                    self.chromosome_length, self.n)
            chromosome.compute_fitness()
            self.initial_population.append(chromosome)

    def initialize_generation(self):
        self.population = []
        self.mating_pool = []
        self.updated_mating_pool = []
        self.best = None
        self.best_iteration = 0
        self.iteration = 0

        for chromosome in self.initial_population:
            chromosome_copy = chromosome.get_chromosome_copy()

            self.update_best_child(chromosome_copy)
            self.population.append(chromosome_copy)

    def update_best_child(self, child):
        if self.best is None or child.get_fitness() < self.best.get_fitness():
            self.best = child.get_chromosome_copy()
            self.best_iteration = self.iteration
            self.all_best_fitness.append(self.best.get_fitness())
            self.iteration_list.append(self.iteration)
            sys.stdout.write(
                "\r%s%d%s%d%s" % ("Iteration : ", self.iteration, " Cost: ", self.best.get_fitness(), "\n"))
            sys.stdout.flush()

    def random_selection(self):
        parent_1 = self.mating_pool[random.randint(0, len(self.mating_pool) - 1)].get_chromosome_copy()
        parent_2 = self.mating_pool[random.randint(0, len(self.mating_pool) - 1)].get_chromosome_copy()
        return [parent_1, parent_2]

    def one_point_crossover(self, parent_1, parent_2):
        random_point = random.randint(0, self.chromosome_length - 1)

        for i in range(random_point, self.chromosome_length):
            parent_1.genes[i] = parent_2.genes[i]

        return parent_1

    def two_point_crossover(self, parent_1, parent_2):
        random_indices = random.sample(range(self.chromosome_length), 2)
        start_index = min(random_indices)
        end_index = max(random_indices)

        for i in range(start_index, end_index + 1):
            parent_1.genes[i] = parent_2.genes[i]

        return parent_1

    def uniform_crossover(self, parent_1, parent_2):
        for i in range(self.chromosome_length):
            if random.random() < 0.5:
                parent_1.genes[i] = parent_2.genes[i]

        return parent_1

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
            new_gene = []
            for gene in child.genes:
                ng = []
                for pos in range(len(gene)):
                    ng.append(gene[pos])
                new_gene.append(ng)
            for index in range(start_index, end_index + 1):
                new_gene[index] = child.genes[indices_list[index - start_index]]
            child.set_genes(new_gene)

        child.compute_fitness()
        self.update_best_child(child)

    def roulette_wheel(self):
        self.mating_pool = []
        for chromosome in self.population:
            count = (((self.n ** 2) * 6) - chromosome.get_fitness())
            for _ in range(count):
                self.mating_pool.append(chromosome)

    def tournament(self):
        self.mating_pool = []
        for i in range(self.population_size):
            chromosome_1 = self.population[random.randint(0, self.population_size - 1)]
            chromosome_2 = self.population[random.randint(0, self.population_size - 1)]
            if chromosome_1.get_fitness() < chromosome_2.get_fitness():
                self.mating_pool.append(chromosome_1)
            else:
                self.mating_pool.append(chromosome_2)

    def no_selection(self):
        self.mating_pool = self.population

    def gen_replacement(self, new_population):
        x = int(self.population_size * self.elite / 100)

        best_x = []
        worst_in_best = 0
        worst_in_best_pos = 0

        worst_x = []
        best_in_worst = (self.n ** 2) * 6
        best_in_worst_pos = 0

        for i in range(x):
            best_x.append(self.population[i])
            if self.population[i].get_fitness() > worst_in_best:
                worst_in_best = self.population[i].get_fitness()
                worst_in_best_pos = i

            worst_x.append(new_population[i])
            if new_population[i].get_fitness() < best_in_worst:
                best_in_worst = new_population[i].get_fitness()
                best_in_worst_pos = i

        for i in range(x, self.population_size):
            if self.population[i].get_fitness() < worst_in_best:
                best_x[worst_in_best_pos] = self.population[i]
                worst_in_best = self.population[i].get_fitness()
                for best_pos in range(0, x):
                    if best_x[best_pos].get_fitness() > worst_in_best:
                        worst_in_best = best_x[best_pos].get_fitness()
                        worst_in_best_pos = best_pos

            if new_population[i].get_fitness() > best_in_worst:
                worst_x[best_in_worst_pos] = new_population[i]
                best_in_worst = new_population[i].get_fitness()
                for worst_pos in range(0, x):
                    if worst_x[worst_pos].get_fitness() < best_in_worst:
                        best_in_worst = worst_x[worst_pos].get_fitness()
                        best_in_worst_pos = worst_pos

        pos = 0
        for i in range(self.population_size):
            if new_population[i].get_fitness() >= best_in_worst:
                new_population[i] = best_x[pos]
                pos += 1
                if pos == x:
                    break

        self.population = new_population

    def create_new_generation(self):
        length = self.population_size

        new_population = []

        for _ in range(length):
            parents = self.random_selection()
            child = self.crossover(parents[0], parents[1])
            self.mutation(child)
            new_population.append(child)

        self.gen_replacement(new_population)

    def genetic_algorithm(self):
        self.mating_pool_updation()
        self.create_new_generation()

    def find_average_fitness(self):
        total = 0
        for chromosome in self.population:
            total += chromosome.get_fitness()

        return total / len(self.population)

    def solve(self):
        self.iteration = 0
        self.each_best_fitness = []
        self.all_avg_fitness = []
        while self.best.get_fitness() != 0 and self.iteration < self.max_iterations:
            if self.iteration % 100 == 0:
                sys.stdout.write("\r%s%d" % ("Iteration : ", self.iteration))
                sys.stdout.flush()
            self.genetic_algorithm()
            self.each_best_fitness.append(self.best.get_fitness())
            self.all_avg_fitness.append(self.find_average_fitness())
            self.iteration += 1

        # self.all_best_fitness.append(self.best.get_fitness())
        print("\nPopulation size:", self.population_size)
        print("Total iterations: ", self.iteration)
        print("Best fitness: ", self.best.get_fitness())
        # print("Average fitness of the final generation: ", self.find_average_fitness())
        if self.best.get_fitness() == 0:
            print("Best solution moves: ", print_moves(self.best.genes))
        print("=======================================")
        print("\n")

        return self.best.get_fitness()


def write_to_file(fitness_across_initializations, config_combination, population_size, mutation_rate, iterations,
                  elite):
    try:
        os.mkdir(CubeConstants.directory_name)
    except:
        pass

    data_dict = {}
    data_dict.update({
        "init": ["init-" + str(i) for i in range(len(fitness_across_initializations))]
    })

    for item in fitness_across_initializations:
        for r in range(len(item)):
            retries = []
            for i in range(len(fitness_across_initializations)):
                retries.append(fitness_across_initializations[i][r])
            data_dict.update({
                "r-" + str(r): retries
            })
    file_name = CubeConstants.directory_name + CubeConstants.file_name + str(population_size) + "-" + str(
        mutation_rate) + "-" + str(iterations) + "-" + str(elite) + "-" + str(config_combination)
    # file_name = CubeConstants.directory_name + CubeConstants.file_name + str(config_combination)
    with open(file_name, 'w') as file:
        for key in data_dict.keys():
            file.write(key)
            item = data_dict[key]
            for element in item:
                file.write(" " + str(element))
            file.write("\n")
    file.close()


def plot_graph(each_best_fitness, all_avg_fitness, current_path, initialization, retry):
    plt.figure()
    plt.plot(np.arange(0, len(all_avg_fitness)), all_avg_fitness, label="Average fitness")
    plt.plot(np.arange(0, len(each_best_fitness)), each_best_fitness,
             label="Best fitness = " + str(each_best_fitness[-1]))
    plt.legend()
    plt.savefig(current_path + "fig-i" + str(initialization) + "r" + str(retry))
    plt.close()


# def write_evaluation_results(best_fitness_across_initializations, best_iteration_across_initializations,
#                              population_size, mutation_rate, iterations, elite):
#     try:
#         os.mkdir(CubeConstants.evaluation_directory_name)
#     except:
#         pass
#
#     file_name = CubeConstants.evaluation_directory_name + CubeConstants.file_name + str(population_size) + "-" + str(
#         mutation_rate) + "-" + str(iterations) + "-" + str(elite) + "-" + str(config_combination)
#     with open(file_name, 'w') as file:
#         for i in range(len(best_fitness_across_initializations)):
#             file.write("i:" + str(i))
#             file.write("\n")
#             for j in range(len(best_fitness_across_initializations[i])):
#                 file.write(
#                     str(best_iteration_across_initializations[i][j]) + ":" + str(
#                         best_fitness_across_initializations[i][j]))
#                 file.write("\n")
#             file.write("plot:" + str(i))
#             file.write("\n")
#     file.close()


n = 3
if len(sys.argv) == 9:
    re_initializations = int(sys.argv[1])
    retries = int(sys.argv[2])
    chromosome_length = int(sys.argv[3])
    population_size = int(sys.argv[4])
    mutation_rate = float(sys.argv[5])
    iterations = int(sys.argv[6])
    elite = float(sys.argv[7])
    config_combination = int(sys.argv[8])
else:
    print("Invalid argument count")
    exit(0)

# re_initializations = 1
# retries = 1
# chromosome_length = 5
# population_size = 10
# mutation_rate = 0.05
# iterations = 1
# elite = 0
# config_combination = 4

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
elif config_combination == 19:
    print("No selection --> one point crossover --> random mutation")
elif config_combination == 20:
    print("No selection --> one-point crossover --> inversion mutation")
elif config_combination == 21:
    print("No selection --> one-point crossover --> scramble mutation")
elif config_combination == 22:
    print("No selection --> two-point crossover --> random mutation")
elif config_combination == 23:
    print("No selection --> two-point crossover --> inversion mutation")
elif config_combination == 24:
    print("No selection --> two-point crossover --> scramble mutation")
elif config_combination == 25:
    print("No selection --> uniform crossover --> random mutation")
elif config_combination == 26:
    print("No selection --> uniform crossover --> inversion mutation")
elif config_combination == 27:
    print("No selection --> uniform crossover --> scramble mutation")

file_name = str(n) + "x" + str(n)
file = open(file_name, "rb")
list_of_configurations = pickle.load(file)

try:
    os.mkdir(CubeConstants.evaluation_directory_name)
except:
    pass

for index, configuration in enumerate(list_of_configurations):
    current_path = CubeConstants.evaluation_directory_name + "Orientation-" + str(index + 1) + "/"
    try:
        os.mkdir(current_path)
    except:
        pass
    best_fitness_across_initializations = []
    best_iteration_across_initializations = []
    best_fitness = 0
    seed_value = CubeConstants.seed
    print("Cube orientation: " + str(index + 1))
    for initialization in range(re_initializations):
        CubeConstants.seed = seed_value
        print("initialization: " + str(initialization))
        print("chromosome length: " + str(chromosome_length))

        cuberoid = Cuberoid(
            configuration,
            n,
            chromosome_length,
            population_size,
            mutation_rate,
            iterations,
            elite,
            config_combination
        )

        best_fitness_across_retries = []
        for retry in range(retries):
            CubeConstants.seed = seed_value + (retry * 1000)
            random.seed(CubeConstants.seed)
            print("seed value: " + str(CubeConstants.seed))
            print("retry: " + str(retry))
            print("\n")
            cuberoid.initialize_generation()
            best_fitness = cuberoid.solve()
            # best_fitness_across_retries.append(best_fitness)

            plot_graph(cuberoid.each_best_fitness, cuberoid.all_avg_fitness, current_path, initialization, retry)
            if best_fitness == 0:
                # pass
                break
        # best_fitness_across_initializations.append(best_fitness_across_retries)
        # best_fitness_across_initializations.append(cuberoid.all_best_fitness)
        # best_iteration_across_initializations.append(cuberoid.iteration_list)
        if best_fitness == 0:
            # pass
            break
    # write_evaluation_results(best_fitness_across_initializations, best_iteration_across_initializations,
    #                          population_size, mutation_rate, iterations, elite)
    # write_to_file(best_fitness_across_initializations, config_combination, population_size, mutation_rate, iterations,
    #               elite)
