import matplotlib.pyplot as plt
import sys
import os

if len(sys.argv) == 2:
    directory_name = sys.argv[1]
else:
    print("Invalid input")
    exit(0)

files = os.listdir(directory_name)

for file in files:
    folder_name = directory_name + "/" + file[0:-4]
    try:
        os.mkdir(folder_name)
    except:
        pass

    with open(directory_name + "/" + file) as f:
        print("==================================================")
        lines = f.readlines()
        generations = []
        best_fitness = []
        i = 0
        r = 0
        for line in lines:
            line = line.split(" ")
            if line[0] == 'i':
                i = int(line[1])
                plt.figure()
            elif line[0] == 'r':
                r = int(line[1])
                generations = []
                best_fitness = []
            elif line[0] == 'save':
                plt.xlabel("Generations")
                plt.ylabel("Fitness value")
                plt.legend()
                plt.savefig(folder_name + "/" + "i-" + str(i))
            elif line[0] != '\n':
                generations.append(int(line[0].split(":")[1]))
                best_fitness.append(int(line[1].split(":")[1]))
            else:
                plt.plot(generations, best_fitness, label='retry: ' + str(r))
    f.close()
