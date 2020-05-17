import os
import sys

import matplotlib.pyplot as plt
import CubeConstants

if len(sys.argv) == 2:
    directory_name = sys.argv[1]
else:
    print("Invalid argument count")
    exit(0)

# directory_name = "/home/achu/MyComputer/Entertainment/Studies/CIT/Semester2/Project/Evaluation_Data"
files = os.listdir(directory_name)

for file in files:
    with open(directory_name + "/" + file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(":")
            if line[0] == "i":
                # plt.figure()
                best_fitness = []
                iterations = []
            elif line[0] == "plot":
                plt.plot(iterations, best_fitness, label='initialization: ' + str(line[1]))
            else:
                iterations.append(int(line[0]))
                best_fitness.append(int(line[1]))
        plt.xlabel("Generations")
        plt.ylabel("Best fitness")
        plt.legend()
        # plt.show()
        plt.savefig(CubeConstants.image_save_directory_name + file + ".png")
    f.close()
