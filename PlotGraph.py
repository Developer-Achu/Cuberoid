import os
import sys

# import xlrd
import matplotlib.pyplot as plt
import pandas as pd

import CubeConstants

if len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    print("Invalid argument count")
    exit(0)
# file_name = '/home/achu/MyComputer/Entertainment/Studies/CIT/Semester2/Project/Data/data.xlsx'
# xls = xlrd.open_workbook(file_name, on_demand=True)
# sheet_names = xls.sheet_names()
# sheet_names_map = {
#     "selection": {
#         "Combination of selections (one-point and random)": {
#             "sheet_names": [
#                 "Config-1",
#                 "Config-10",
#                 "Config-19",
#             ],
#             "config_labels": [
#                 "Roulette\nOne-point\nRandom",
#                 "Tournament\nOne-point\nRandom",
#                 "No\nOne-point\nRandom",
#             ]
#         },
#
#         "Combination of selections (one-point and inversion)": {
#             "sheet_names": [
#                 "Config-2",
#                 "Config-11",
#                 "Config-20",
#             ],
#             "config_labels": [
#                 "Roulette\nOne-point\nInversion",
#                 "Tournament\nOne-point\nInversion",
#                 "No\nOne-point\nInversion",
#             ]
#         },
#
#         "Combination of selections (one-point and scramble)": {
#             "sheet_names": [
#                 "Config-3",
#                 "Config-12",
#                 "Config-21",
#             ],
#             "config_labels": [
#                 "Roulette\nOne-point\nScramble",
#                 "Tournament\nOne-point\nScramble",
#                 "No\nOne-point\nScramble",
#             ]
#         },
#
#         "Combination of selections (two-point and random)": {
#             "sheet_names": [
#                 "Config-4",
#                 "Config-13",
#                 "Config-22",
#             ],
#             "config_labels": [
#                 "Roulette\nTwo-point\nRandom",
#                 "Tournament\nTwo-point\nRandom",
#                 "No\nTwo-point\nRandom",
#             ]
#         },
#
#         "Combination of selections (two-point and inversion)": {
#             "sheet_names": [
#                 "Config-5",
#                 "Config-14",
#                 "Config-23",
#             ],
#             "config_labels": [
#                 "Roulette\nTwo-point\nInversion",
#                 "Tournament\nTwo-point\nInversion",
#                 "No\nTwo-point\nInversion",
#             ]
#         },
#
#         "Combination of selections (two-point and scramble)": {
#             "sheet_names": [
#                 "Config-6",
#                 "Config-15",
#                 "Config-24",
#             ],
#             "config_labels": [
#                 "Roulette\nTwo-point\nScramble",
#                 "Tournament\nTwo-point\nScramble",
#                 "No\nTwo-point\nScramble",
#             ]
#         },
#
#         "Combination of selections (uniform and random)": {
#             "sheet_names": [
#                 "Config-7",
#                 "Config-16",
#                 "Config-25",
#             ],
#             "config_labels": [
#                 "Roulette\nUniform\nRandom",
#                 "Tournament\nUniform\nRandom",
#                 "No\nUniform\nRandom",
#             ]
#         },
#
#         "Combination of selections (uniform and inversion)": {
#             "sheet_names": [
#                 "Config-8",
#                 "Config-17",
#                 "Config-26",
#             ],
#             "config_labels": [
#                 "Roulette\nUniform\nInversion",
#                 "Tournament\nUniform\nInversion",
#                 "No\nUniform\nInversion",
#             ]
#         },
#
#         "Combination of selections (uniform and scramble)": {
#             "sheet_names": [
#                 "Config-9",
#                 "Config-18",
#                 "Config-27",
#             ],
#             "config_labels": [
#                 "Roulette\nUniform\nScramble",
#                 "Tournament\nUniform\nScramble",
#                 "No\nUniform\nScramble",
#             ]
#         },
#     },
#
#     "crossover": {
#         "Combination of crossover (roulette and random)": {
#             "sheet_names": [
#                 "Config-1",
#                 "Config-4",
#                 "Config-7",
#             ],
#             "config_labels": [
#                 "One-point\nRoulette\nRandom",
#                 "Two-point\nRoulette\nRandom",
#                 "Uniform\nRoulette\nRandom",
#             ]
#         },
#
#         "Combination of crossover (roulette and inversion)": {
#             "sheet_names": [
#                 "Config-2",
#                 "Config-5",
#                 "Config-8",
#             ],
#             "config_labels": [
#                 "One-point\nRoulette\nInversion",
#                 "Two-point\nRoulette\nInversion",
#                 "Uniform\nRoulette\nInversion",
#             ]
#         },
#
#         "Combination of crossover (roulette and scramble)": {
#             "sheet_names": [
#                 "Config-3",
#                 "Config-6",
#                 "Config-9",
#             ],
#             "config_labels": [
#                 "One-point\nRoulette\nScramble",
#                 "Two-point\nRoulette\nScramble",
#                 "Uniform\nRoulette\nScramble",
#             ]
#         },
#
#         "Combination of crossover (tournament and random)": {
#             "sheet_names": [
#                 "Config-10",
#                 "Config-13",
#                 "Config-16",
#             ],
#             "config_labels": [
#                 "One-point\nTournament\nRandom",
#                 "Two-point\nTournament\nRandom",
#                 "Uniform\nTournament\nRandom",
#             ]
#         },
#
#         "Combination of crossover (tournament and inversion)": {
#             "sheet_names": [
#                 "Config-11",
#                 "Config-14",
#                 "Config-17",
#             ],
#             "config_labels": [
#                 "One-point\nTournament\nInversion",
#                 "Two-point\nTournament\nInversion",
#                 "Uniform\nTournament\nInversion",
#             ]
#         },
#
#         "Combination of crossover (tournament and scramble)": {
#             "sheet_names": [
#                 "Config-12",
#                 "Config-15",
#                 "Config-18",
#             ],
#             "config_labels": [
#                 "One-point\nTournament\nScramble",
#                 "Two-point\nTournament\nScramble",
#                 "Uniform\nTournament\nScramble",
#             ]
#         },
#
#         "Combination of crossover (No and random)": {
#             "sheet_names": [
#                 "Config-19",
#                 "Config-22",
#                 "Config-25",
#             ],
#             "config_labels": [
#                 "One-point\nNo\nRandom",
#                 "Two-point\nNo\nRandom",
#                 "Uniform\nNo\nRandom",
#             ]
#         },
#
#         "Combination of crossover (No and inversion)": {
#             "sheet_names": [
#                 "Config-20",
#                 "Config-23",
#                 "Config-26",
#             ],
#             "config_labels": [
#                 "One-point\nNo\nInversion",
#                 "Two-point\nNo\nInversion",
#                 "Uniform\nNo\nInversion",
#             ]
#         },
#
#         "Combination of crossover (No and scramble)": {
#             "sheet_names": [
#                 "Config-21",
#                 "Config-24",
#                 "Config-27",
#             ],
#             "config_labels": [
#                 "One-point\nNo\nScramble",
#                 "Two-point\nNo\nScramble",
#                 "Uniform\nNo\nScramble",
#             ]
#         },
#     },
#
#     "mutation": {
#         "Combination of mutation (roulette and one-point)": {
#             "sheet_names": [
#                 "Config-1",
#                 "Config-2",
#                 "Config-3",
#             ],
#             "config_labels": [
#                 "Random\nRoulette\nOne-point",
#                 "Inversion\nRoulette\nOne-point",
#                 "Scramble\nRoulette\nOne-point",
#             ]
#         },
#
#         "Combination of mutation (roulette and two-point)": {
#             "sheet_names": [
#                 "Config-4",
#                 "Config-5",
#                 "Config-6",
#             ],
#             "config_labels": [
#                 "Random\nRoulette\nTwo-point",
#                 "Inversion\nRoulette\nTwo-point",
#                 "Scramble\nRoulette\nTwo-point",
#             ]
#         },
#
#         "Combination of mutation (roulette and uniform)": {
#             "sheet_names": [
#                 "Config-7",
#                 "Config-8",
#                 "Config-9",
#             ],
#             "config_labels": [
#                 "Random\nRoulette\nUniform",
#                 "Inversion\nRoulette\nUniform",
#                 "Scramble\nRoulette\nUniform",
#             ]
#         },
#
#         "Combination of mutation (tournament and One-point)": {
#             "sheet_names": [
#                 "Config-10",
#                 "Config-11",
#                 "Config-12",
#             ],
#             "config_labels": [
#                 "Random\nTournament\nOne-point",
#                 "Inversion\nTournament\nOne-point",
#                 "Scramble\nTournament\nOne-point",
#             ]
#         },
#
#         "Combination of mutation (tournament and two-point)": {
#             "sheet_names": [
#                 "Config-13",
#                 "Config-14",
#                 "Config-15",
#             ],
#             "config_labels": [
#                 "Random\nTournament\nTwo-point",
#                 "Inversion\nTournament\nTwo-point",
#                 "Scramble\nTournament\nTwo-point",
#             ]
#         },
#
#         "Combination of mutation (tournament and uniform)": {
#             "sheet_names": [
#                 "Config-16",
#                 "Config-17",
#                 "Config-18",
#             ],
#             "config_labels": [
#                 "Random\nTournament\nUniform",
#                 "Inversion\nTournament\nUniform",
#                 "Scramble\nTournament\nUniform",
#             ]
#         },
#
#         "Combination of mutation (no and one-point)": {
#             "sheet_names": [
#                 "Config-19",
#                 "Config-20",
#                 "Config-21",
#             ],
#             "config_labels": [
#                 "Random\nNo\nOne-point",
#                 "Inversion\nNo\nOne-point",
#                 "Scramble\nNo\nOne-point",
#             ]
#         },
#
#         "Combination of mutation (no and two-point)": {
#             "sheet_names": [
#                 "Config-22",
#                 "Config-23",
#                 "Config-24",
#             ],
#             "config_labels": [
#                 "Random\nNo\nTwo-point",
#                 "Inversion\nNo\nTwo-point",
#                 "Scramble\nNo\nTwo-point",
#             ]
#         },
#
#         "Combination of mutation (no and uniform)": {
#             "sheet_names": [
#                 "Config-25",
#                 "Config-26",
#                 "Config-27",
#             ],
#             "config_labels": [
#                 "Random\nNo\nUniform",
#                 "Inversion\nNo\nUniform",
#                 "Scramble\nNo\nUniform",
#             ]
#         },
#
#     }
#
# }


sheet_names_map = {
    "selection": {
        "Combination of selections (one)": {
            "sheet_names": [
                "Config-1",
                "Config-10",
                "Config-19",
                "Config-2",
                "Config-11",
                "Config-20",
                "Config-3",
                "Config-12",
                "Config-21",
            ],
            "config_labels": [
                "Roulette\nOne-point\nRandom",
                "Tournament\nOne-point\nRandom",
                "No\nOne-point\nRandom",
                "Roulette\nOne-point\nInversion",
                "Tournament\nOne-point\nInversion",
                "No\nOne-point\nInversion",
                "Roulette\nOne-point\nScramble",
                "Tournament\nOne-point\nScramble",
                "No\nOne-point\nScramble",
            ]
        },

        "Combination of selections (two)": {
            "sheet_names": [
                "Config-4",
                "Config-13",
                "Config-22",
                "Config-5",
                "Config-14",
                "Config-23",
                "Config-6",
                "Config-15",
                "Config-24",
            ],
            "config_labels": [
                "Roulette\nTwo-point\nRandom",
                "Tournament\nTwo-point\nRandom",
                "No\nTwo-point\nRandom",
                "Roulette\nTwo-point\nInversion",
                "Tournament\nTwo-point\nInversion",
                "No\nTwo-point\nInversion",
                "Roulette\nTwo-point\nScramble",
                "Tournament\nTwo-point\nScramble",
                "No\nTwo-point\nScramble",
            ]
        },

        "Combination of selections (uniform)": {
            "sheet_names": [
                "Config-7",
                "Config-16",
                "Config-25",
                "Config-8",
                "Config-17",
                "Config-26",
                "Config-9",
                "Config-18",
                "Config-27",
            ],
            "config_labels": [
                "Roulette\nUniform\nRandom",
                "Tournament\nUniform\nRandom",
                "No\nUniform\nRandom",
                "Roulette\nUniform\nInversion",
                "Tournament\nUniform\nInversion",
                "No\nUniform\nInversion",
                "Roulette\nUniform\nScramble",
                "Tournament\nUniform\nScramble",
                "No\nUniform\nScramble",
            ]
        },
    },

    "crossover": {
        "Combination of crossover (roulette)": {
            "sheet_names": [
                "Config-1",
                "Config-4",
                "Config-7",
                "Config-2",
                "Config-5",
                "Config-8",
                "Config-3",
                "Config-6",
                "Config-9",
            ],
            "config_labels": [
                "One-point\nRoulette\nRandom",
                "Two-point\nRoulette\nRandom",
                "Uniform\nRoulette\nRandom",
                "One-point\nRoulette\nInversion",
                "Two-point\nRoulette\nInversion",
                "Uniform\nRoulette\nInversion",
                "One-point\nRoulette\nScramble",
                "Two-point\nRoulette\nScramble",
                "Uniform\nRoulette\nScramble",
            ]
        },

        "Combination of crossover (tournament)": {
            "sheet_names": [
                "Config-10",
                "Config-13",
                "Config-16",
                "Config-11",
                "Config-14",
                "Config-17",
                "Config-12",
                "Config-15",
                "Config-18",
            ],
            "config_labels": [
                "One-point\nTournament\nRandom",
                "Two-point\nTournament\nRandom",
                "Uniform\nTournament\nRandom",
                "One-point\nTournament\nInversion",
                "Two-point\nTournament\nInversion",
                "Uniform\nTournament\nInversion",
                "One-point\nTournament\nScramble",
                "Two-point\nTournament\nScramble",
                "Uniform\nTournament\nScramble",
            ]
        },

        "Combination of crossover (No)": {
            "sheet_names": [
                "Config-19",
                "Config-22",
                "Config-25",
                "Config-20",
                "Config-23",
                "Config-26",
                "Config-21",
                "Config-24",
                "Config-27",
            ],
            "config_labels": [
                "One-point\nNo\nRandom",
                "Two-point\nNo\nRandom",
                "Uniform\nNo\nRandom",
                "One-point\nNo\nInversion",
                "Two-point\nNo\nInversion",
                "Uniform\nNo\nInversion",
                "One-point\nNo\nScramble",
                "Two-point\nNo\nScramble",
                "Uniform\nNo\nScramble",
            ]
        },

    },

    "mutation": {
        "Combination of mutation (roulette)": {
            "sheet_names": [
                "Config-1",
                "Config-2",
                "Config-3",
                "Config-4",
                "Config-5",
                "Config-6",
                "Config-7",
                "Config-8",
                "Config-9",
            ],
            "config_labels": [
                "Random\nRoulette\nOne-point",
                "Inversion\nRoulette\nOne-point",
                "Scramble\nRoulette\nOne-point",
                "Random\nRoulette\nTwo-point",
                "Inversion\nRoulette\nTwo-point",
                "Scramble\nRoulette\nTwo-point",
                "Random\nRoulette\nUniform",
                "Inversion\nRoulette\nUniform",
                "Scramble\nRoulette\nUniform",
            ]
        },

        "Combination of mutation (tournament)": {
            "sheet_names": [
                "Config-10",
                "Config-11",
                "Config-12",
                "Config-13",
                "Config-14",
                "Config-15",
                "Config-16",
                "Config-17",
                "Config-18",
            ],
            "config_labels": [
                "Random\nTournament\nOne-point",
                "Inversion\nTournament\nOne-point",
                "Scramble\nTournament\nOne-point",
                "Random\nTournament\nTwo-point",
                "Inversion\nTournament\nTwo-point",
                "Scramble\nTournament\nTwo-point",
                "Random\nTournament\nUniform",
                "Inversion\nTournament\nUniform",
                "Scramble\nTournament\nUniform",
            ]
        },

        "Combination of mutation (no)": {
            "sheet_names": [
                "Config-19",
                "Config-20",
                "Config-21",
                "Config-22",
                "Config-23",
                "Config-24",
                "Config-25",
                "Config-26",
                "Config-27",
            ],
            "config_labels": [
                "Random\nNo\nOne-point",
                "Inversion\nNo\nOne-point",
                "Scramble\nNo\nOne-point",
                "Random\nNo\nTwo-point",
                "Inversion\nNo\nTwo-point",
                "Scramble\nNo\nTwo-point",
                "Random\nNo\nUniform",
                "Inversion\nNo\nUniform",
                "Scramble\nNo\nUniform",
            ]
        },

    },

    "all": {
        "Combination of all": {
            "sheet_names": [
                "Config-1",
                "Config-2",
                "Config-3",
                "Config-4",
                "Config-5",
                "Config-6",
                "Config-7",
                "Config-8",
                "Config-9",
                "Config-10",
                "Config-11",
                "Config-12",
                "Config-13",
                "Config-14",
                "Config-15",
                "Config-16",
                "Config-17",
                "Config-18",
                "Config-19",
                "Config-20",
                "Config-21",
                "Config-22",
                "Config-23",
                "Config-24",
                "Config-25",
                "Config-26",
                "Config-27",
            ],
            "config_labels": [
                "Random\nRoulette\nOne-point",
                "Inversion\nRoulette\nOne-point",
                "Scramble\nRoulette\nOne-point",
                "Random\nRoulette\nTwo-point",
                "Inversion\nRoulette\nTwo-point",
                "Scramble\nRoulette\nTwo-point",
                "Random\nRoulette\nUniform",
                "Inversion\nRoulette\nUniform",
                "Scramble\nRoulette\nUniform",
                "Random\nTournament\nOne-point",
                "Inversion\nTournament\nOne-point",
                "Scramble\nTournament\nOne-point",
                "Random\nTournament\nTwo-point",
                "Inversion\nTournament\nTwo-point",
                "Scramble\nTournament\nTwo-point",
                "Random\nTournament\nUniform",
                "Inversion\nTournament\nUniform",
                "Scramble\nTournament\nUniform",
                "Random\nNo\nOne-point",
                "Inversion\nNo\nOne-point",
                "Scramble\nNo\nOne-point",
                "Random\nNo\nTwo-point",
                "Inversion\nNo\nTwo-point",
                "Scramble\nNo\nTwo-point",
                "Random\nNo\nUniform",
                "Inversion\nNo\nUniform",
                "Scramble\nNo\nUniform",
            ]
        },
    },

    "baseline and best": {
        "Baseline and best": {
            "sheet_names": [
                "Config-4",
                "Config-16",
            ],
            "config_labels": [
                "Roulette\nTwo-point\nRandom",
                "Tournament\nUniform\nRandom",
            ]
        },
    }

}

try:
    os.mkdir(CubeConstants.graph_directory_name)
except:
    pass

df = pd.read_excel(file_name, sheet_name=None)

for k in sheet_names_map.keys():
    try:
        os.mkdir(CubeConstants.graph_directory_name + k + "/")
    except:
        pass
    sheet_dicts = sheet_names_map[k]
    rotation = 0
    if k == "all":
        rotation = 90
    for key in sheet_dicts.keys():
        graph_config = sheet_dicts[key]
        sheet_names = graph_config["sheet_names"]
        config_labels = graph_config["config_labels"]

        fitness_values = []
        for sheet in sheet_names:
            values = []
            data = df[sheet]
            for i in range(data.shape[0]):
                for j in range(1, len(data.columns) - 1):
                    values.append(data.loc[i][j])
            fitness_values.append(values)

        plt.figure(figsize=(20, 10))
        plt.boxplot(fitness_values, showmeans=True)
        plt.xticks([i + 1 for i in range(len(sheet_names))], config_labels, rotation=rotation)
        plt.xlabel("operator combination")
        plt.ylabel("Best fitness")
        plt.title(key)
        plt.savefig(CubeConstants.graph_directory_name + k + "/" + key + ".png")
        # plt.show()
