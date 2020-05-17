import os
import sys

import matplotlib.pyplot as plt
import pandas as pd

import CubeConstants

if len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    print("Invalid argument count")
    exit(0)

# sheet_names_map = {
#     "selection": {
#         "Combination of selections (one)": {
#             "sheet_names": [
#                 "Config-1",
#                 "Config-10",
#                 "Config-19",
#                 "Config-2",
#                 "Config-11",
#                 "Config-20",
#                 "Config-3",
#                 "Config-12",
#                 "Config-21",
#             ],
#             "config_labels": [
#                 "Roulette\nOne-point\nRandom",
#                 "Tournament\nOne-point\nRandom",
#                 "No\nOne-point\nRandom",
#                 "Roulette\nOne-point\nInversion",
#                 "Tournament\nOne-point\nInversion",
#                 "No\nOne-point\nInversion",
#                 "Roulette\nOne-point\nScramble",
#                 "Tournament\nOne-point\nScramble",
#                 "No\nOne-point\nScramble",
#             ]
#         },
# 
#         "Combination of selections (two)": {
#             "sheet_names": [
#                 "Config-4",
#                 "Config-13",
#                 "Config-22",
#                 "Config-5",
#                 "Config-14",
#                 "Config-23",
#                 "Config-6",
#                 "Config-15",
#                 "Config-24",
#             ],
#             "config_labels": [
#                 "Roulette\nTwo-point\nRandom",
#                 "Tournament\nTwo-point\nRandom",
#                 "No\nTwo-point\nRandom",
#                 "Roulette\nTwo-point\nInversion",
#                 "Tournament\nTwo-point\nInversion",
#                 "No\nTwo-point\nInversion",
#                 "Roulette\nTwo-point\nScramble",
#                 "Tournament\nTwo-point\nScramble",
#                 "No\nTwo-point\nScramble",
#             ]
#         },
# 
#         "Combination of selections (uniform)": {
#             "sheet_names": [
#                 "Config-7",
#                 "Config-16",
#                 "Config-25",
#                 "Config-8",
#                 "Config-17",
#                 "Config-26",
#                 "Config-9",
#                 "Config-18",
#                 "Config-27",
#             ],
#             "config_labels": [
#                 "Roulette\nUniform\nRandom",
#                 "Tournament\nUniform\nRandom",
#                 "No\nUniform\nRandom",
#                 "Roulette\nUniform\nInversion",
#                 "Tournament\nUniform\nInversion",
#                 "No\nUniform\nInversion",
#                 "Roulette\nUniform\nScramble",
#                 "Tournament\nUniform\nScramble",
#                 "No\nUniform\nScramble",
#             ]
#         },
#     },
# 
#     "crossover": {
#         "Combination of crossover (roulette)": {
#             "sheet_names": [
#                 "Config-1",
#                 "Config-4",
#                 "Config-7",
#                 "Config-2",
#                 "Config-5",
#                 "Config-8",
#                 "Config-3",
#                 "Config-6",
#                 "Config-9",
#             ],
#             "config_labels": [
#                 "One-point\nRoulette\nRandom",
#                 "Two-point\nRoulette\nRandom",
#                 "Uniform\nRoulette\nRandom",
#                 "One-point\nRoulette\nInversion",
#                 "Two-point\nRoulette\nInversion",
#                 "Uniform\nRoulette\nInversion",
#                 "One-point\nRoulette\nScramble",
#                 "Two-point\nRoulette\nScramble",
#                 "Uniform\nRoulette\nScramble",
#             ]
#         },
# 
#         "Combination of crossover (tournament)": {
#             "sheet_names": [
#                 "Config-10",
#                 "Config-13",
#                 "Config-16",
#                 "Config-11",
#                 "Config-14",
#                 "Config-17",
#                 "Config-12",
#                 "Config-15",
#                 "Config-18",
#             ],
#             "config_labels": [
#                 "One-point\nTournament\nRandom",
#                 "Two-point\nTournament\nRandom",
#                 "Uniform\nTournament\nRandom",
#                 "One-point\nTournament\nInversion",
#                 "Two-point\nTournament\nInversion",
#                 "Uniform\nTournament\nInversion",
#                 "One-point\nTournament\nScramble",
#                 "Two-point\nTournament\nScramble",
#                 "Uniform\nTournament\nScramble",
#             ]
#         },
# 
#         "Combination of crossover (No)": {
#             "sheet_names": [
#                 "Config-19",
#                 "Config-22",
#                 "Config-25",
#                 "Config-20",
#                 "Config-23",
#                 "Config-26",
#                 "Config-21",
#                 "Config-24",
#                 "Config-27",
#             ],
#             "config_labels": [
#                 "One-point\nNo\nRandom",
#                 "Two-point\nNo\nRandom",
#                 "Uniform\nNo\nRandom",
#                 "One-point\nNo\nInversion",
#                 "Two-point\nNo\nInversion",
#                 "Uniform\nNo\nInversion",
#                 "One-point\nNo\nScramble",
#                 "Two-point\nNo\nScramble",
#                 "Uniform\nNo\nScramble",
#             ]
#         },
# 
#     },
# 
#     "mutation": {
#         "Combination of mutation (roulette)": {
#             "sheet_names": [
#                 "Config-1",
#                 "Config-2",
#                 "Config-3",
#                 "Config-4",
#                 "Config-5",
#                 "Config-6",
#                 "Config-7",
#                 "Config-8",
#                 "Config-9",
#             ],
#             "config_labels": [
#                 "Random\nRoulette\nOne-point",
#                 "Inversion\nRoulette\nOne-point",
#                 "Scramble\nRoulette\nOne-point",
#                 "Random\nRoulette\nTwo-point",
#                 "Inversion\nRoulette\nTwo-point",
#                 "Scramble\nRoulette\nTwo-point",
#                 "Random\nRoulette\nUniform",
#                 "Inversion\nRoulette\nUniform",
#                 "Scramble\nRoulette\nUniform",
#             ]
#         },
# 
#         "Combination of mutation (tournament)": {
#             "sheet_names": [
#                 "Config-10",
#                 "Config-11",
#                 "Config-12",
#                 "Config-13",
#                 "Config-14",
#                 "Config-15",
#                 "Config-16",
#                 "Config-17",
#                 "Config-18",
#             ],
#             "config_labels": [
#                 "Random\nTournament\nOne-point",
#                 "Inversion\nTournament\nOne-point",
#                 "Scramble\nTournament\nOne-point",
#                 "Random\nTournament\nTwo-point",
#                 "Inversion\nTournament\nTwo-point",
#                 "Scramble\nTournament\nTwo-point",
#                 "Random\nTournament\nUniform",
#                 "Inversion\nTournament\nUniform",
#                 "Scramble\nTournament\nUniform",
#             ]
#         },
# 
#         "Combination of mutation (no)": {
#             "sheet_names": [
#                 "Config-19",
#                 "Config-20",
#                 "Config-21",
#                 "Config-22",
#                 "Config-23",
#                 "Config-24",
#                 "Config-25",
#                 "Config-26",
#                 "Config-27",
#             ],
#             "config_labels": [
#                 "Random\nNo\nOne-point",
#                 "Inversion\nNo\nOne-point",
#                 "Scramble\nNo\nOne-point",
#                 "Random\nNo\nTwo-point",
#                 "Inversion\nNo\nTwo-point",
#                 "Scramble\nNo\nTwo-point",
#                 "Random\nNo\nUniform",
#                 "Inversion\nNo\nUniform",
#                 "Scramble\nNo\nUniform",
#             ]
#         },
# 
#     },
# 
#     "all": {
#         "Combination of all": {
#             "sheet_names": [
#                 "Config-1",
#                 "Config-2",
#                 "Config-3",
#                 "Config-4",
#                 "Config-5",
#                 "Config-6",
#                 "Config-7",
#                 "Config-8",
#                 "Config-9",
#                 "Config-10",
#                 "Config-11",
#                 "Config-12",
#                 "Config-13",
#                 "Config-14",
#                 "Config-15",
#                 "Config-16",
#                 "Config-17",
#                 "Config-18",
#                 "Config-19",
#                 "Config-20",
#                 "Config-21",
#                 "Config-22",
#                 "Config-23",
#                 "Config-24",
#                 "Config-25",
#                 "Config-26",
#                 "Config-27",
#             ],
#             "config_labels": [
#                 "Random\nRoulette\nOne-point",
#                 "Inversion\nRoulette\nOne-point",
#                 "Scramble\nRoulette\nOne-point",
#                 "Random\nRoulette\nTwo-point",
#                 "Inversion\nRoulette\nTwo-point",
#                 "Scramble\nRoulette\nTwo-point",
#                 "Random\nRoulette\nUniform",
#                 "Inversion\nRoulette\nUniform",
#                 "Scramble\nRoulette\nUniform",
#                 "Random\nTournament\nOne-point",
#                 "Inversion\nTournament\nOne-point",
#                 "Scramble\nTournament\nOne-point",
#                 "Random\nTournament\nTwo-point",
#                 "Inversion\nTournament\nTwo-point",
#                 "Scramble\nTournament\nTwo-point",
#                 "Random\nTournament\nUniform",
#                 "Inversion\nTournament\nUniform",
#                 "Scramble\nTournament\nUniform",
#                 "Random\nNo\nOne-point",
#                 "Inversion\nNo\nOne-point",
#                 "Scramble\nNo\nOne-point",
#                 "Random\nNo\nTwo-point",
#                 "Inversion\nNo\nTwo-point",
#                 "Scramble\nNo\nTwo-point",
#                 "Random\nNo\nUniform",
#                 "Inversion\nNo\nUniform",
#                 "Scramble\nNo\nUniform",
#             ]
#         },
#     },
# 
#     "baseline and best": {
#         "Baseline and best": {
#             "sheet_names": [
#                 "Config-4",
#                 "Config-16",
#             ],
#             "config_labels": [
#                 "Roulette\nTwo-point\nRandom",
#                 "Tournament\nUniform\nRandom",
#             ]
#         },
#     }
# 
# }

sheet_names_map = {
    "baseline": {
        "Baseline parameters": {
            "sheet_names": [
                "Config-100-0.05-2000-1.0-4",
            ],
            "config_labels": [
                "Baseline\npop-size = 100\nmutation-rate=0.05\ngenerations=2000\nelitism=1%",
            ]
        },
    },

    "population-size": {
        "Population size 100": {
            "sheet_names": [
                "Config-100-0.05-2000-1.0-4",
                "Config-100-0.05-2000-2.0-4",
                "Config-100-0.05-2000-3.0-4",
                "Config-100-0.1-2000-1.0-4",
                "Config-100-0.1-2000-2.0-4",
                "Config-100-0.1-2000-3.0-4",
                "Config-100-0.15-2000-1.0-4",
                "Config-100-0.15-2000-2.0-4",
                "Config-100-0.15-2000-3.0-4",
            ],
            "config_labels": [
                "mutation-rate: 0.05\nElitism: 1%",
                "mutation-rate: 0.05\nElitism: 2%",
                "mutation-rate: 0.05\nElitism: 3%",
                "mutation-rate: 0.1\nElitism: 1%",
                "mutation-rate: 0.1\nElitism: 2%",
                "mutation-rate: 0.1\nElitism: 3%",
                "mutation-rate: 0.15\nElitism: 1%",
                "mutation-rate: 0.15\nElitism: 2%",
                "mutation-rate: 0.15\nElitism: 3%",
            ]
        },

        "Population size 200": {
            "sheet_names": [
                "Config-200-0.05-2000-1.0-4",
                "Config-200-0.05-2000-2.0-4",
                "Config-200-0.05-2000-3.0-4",
                "Config-200-0.1-2000-1.0-4",
                "Config-200-0.1-2000-2.0-4",
                "Config-200-0.1-2000-3.0-4",
                "Config-200-0.15-2000-1.0-4",
                "Config-200-0.15-2000-2.0-4",
                "Config-200-0.15-2000-3.0-4",
            ],
            "config_labels": [
                "mutation-rate: 0.05\nElitism: 1%",
                "mutation-rate: 0.05\nElitism: 2%",
                "mutation-rate: 0.05\nElitism: 3%",
                "mutation-rate: 0.1\nElitism: 1%",
                "mutation-rate: 0.1\nElitism: 2%",
                "mutation-rate: 0.1\nElitism: 3%",
                "mutation-rate: 0.15\nElitism: 1%",
                "mutation-rate: 0.15\nElitism: 2%",
                "mutation-rate: 0.15\nElitism: 3%",
            ]
        },

        "Population size 300": {
            "sheet_names": [
                "Config-300-0.05-2000-1.0-4",
                "Config-300-0.05-2000-2.0-4",
                "Config-300-0.05-2000-3.0-4",
                "Config-300-0.1-2000-1.0-4",
                "Config-300-0.1-2000-2.0-4",
                "Config-300-0.1-2000-3.0-4",
                "Config-300-0.15-2000-1.0-4",
                "Config-300-0.15-2000-2.0-4",
                "Config-300-0.15-2000-3.0-4",
            ],
            "config_labels": [
                "mutation-rate: 0.05\nElitism: 1%",
                "mutation-rate: 0.05\nElitism: 2%",
                "mutation-rate: 0.05\nElitism: 3%",
                "mutation-rate: 0.1\nElitism: 1%",
                "mutation-rate: 0.1\nElitism: 2%",
                "mutation-rate: 0.1\nElitism: 3%",
                "mutation-rate: 0.15\nElitism: 1%",
                "mutation-rate: 0.15\nElitism: 2%",
                "mutation-rate: 0.15\nElitism: 3%",
            ]
        },
    },

    "mutation-rate": {
        "Mutation rate 0_05": {
            "sheet_names": [
                "Config-100-0.05-2000-1.0-4",
                "Config-100-0.05-2000-2.0-4",
                "Config-100-0.05-2000-3.0-4",
                "Config-200-0.05-2000-1.0-4",
                "Config-200-0.05-2000-2.0-4",
                "Config-200-0.05-2000-3.0-4",
                "Config-300-0.05-2000-1.0-4",
                "Config-300-0.05-2000-2.0-4",
                "Config-300-0.05-2000-3.0-4",
            ],
            "config_labels": [
                "population-size: 100\nElitism: 1%",
                "population-size: 100\nElitism: 2%",
                "population-size: 100\nElitism: 3%",
                "population-size: 200\nElitism: 1%",
                "population-size: 200\nElitism: 2%",
                "population-size: 200\nElitism: 3%",
                "population-size: 300\nElitism: 1%",
                "population-size: 300\nElitism: 2%",
                "population-size: 300\nElitism: 3%",
            ]
        },

        "Mutation rate 0_1": {
            "sheet_names": [
                "Config-100-0.1-2000-1.0-4",
                "Config-100-0.1-2000-2.0-4",
                "Config-100-0.1-2000-3.0-4",
                "Config-200-0.1-2000-1.0-4",
                "Config-200-0.1-2000-2.0-4",
                "Config-200-0.1-2000-3.0-4",
                "Config-300-0.1-2000-1.0-4",
                "Config-300-0.1-2000-2.0-4",
                "Config-300-0.1-2000-3.0-4",
            ],
            "config_labels": [
                "population-size: 100\nElitism: 1%",
                "population-size: 100\nElitism: 2%",
                "population-size: 100\nElitism: 3%",
                "population-size: 200\nElitism: 1%",
                "population-size: 200\nElitism: 2%",
                "population-size: 200\nElitism: 3%",
                "population-size: 300\nElitism: 1%",
                "population-size: 300\nElitism: 2%",
                "population-size: 300\nElitism: 3%",
            ]
        },

        "Mutation rate 0_15": {
            "sheet_names": [
                "Config-100-0.15-2000-1.0-4",
                "Config-100-0.15-2000-2.0-4",
                "Config-100-0.15-2000-3.0-4",
                "Config-200-0.15-2000-1.0-4",
                "Config-200-0.15-2000-2.0-4",
                "Config-200-0.15-2000-3.0-4",
                "Config-300-0.15-2000-1.0-4",
                "Config-300-0.15-2000-2.0-4",
                "Config-300-0.15-2000-3.0-4",
            ],
            "config_labels": [
                "population-size: 100\nElitism: 1%",
                "population-size: 100\nElitism: 2%",
                "population-size: 100\nElitism: 3%",
                "population-size: 200\nElitism: 1%",
                "population-size: 200\nElitism: 2%",
                "population-size: 200\nElitism: 3%",
                "population-size: 300\nElitism: 1%",
                "population-size: 300\nElitism: 2%",
                "population-size: 300\nElitism: 3%",
            ]
        },
    },

    "elitism": {
        "Elitism 1": {
            "sheet_names": [
                "Config-100-0.05-2000-1.0-4",
                "Config-100-0.1-2000-1.0-4",
                "Config-100-0.15-2000-1.0-4",
                "Config-200-0.05-2000-1.0-4",
                "Config-200-0.1-2000-1.0-4",
                "Config-200-0.15-2000-1.0-4",
                "Config-300-0.05-2000-1.0-4",
                "Config-300-0.1-2000-1.0-4",
                "Config-300-0.15-2000-1.0-4",
            ],
            "config_labels": [
                "population-size: 100\nMutation-rate: 0.05",
                "population-size: 100\nMutation-rate: 0.1",
                "population-size: 100\nMutation-rate: 0.15",
                "population-size: 200\nMutation-rate: 0.05",
                "population-size: 200\nMutation-rate: 0.1",
                "population-size: 200\nMutation-rate: 0.15",
                "population-size: 300\nMutation-rate: 0.05",
                "population-size: 300\nMutation-rate: 0.1",
                "population-size: 300\nMutation-rate: 0.15",
            ]
        },

        "Elitism 2": {
            "sheet_names": [
                "Config-100-0.05-2000-2.0-4",
                "Config-100-0.1-2000-2.0-4",
                "Config-100-0.15-2000-2.0-4",
                "Config-200-0.05-2000-2.0-4",
                "Config-200-0.1-2000-2.0-4",
                "Config-200-0.15-2000-2.0-4",
                "Config-300-0.05-2000-2.0-4",
                "Config-300-0.1-2000-2.0-4",
                "Config-300-0.15-2000-2.0-4",
            ],
            "config_labels": [
                "population-size: 100\nMutation-rate: 0.05",
                "population-size: 100\nMutation-rate: 0.1",
                "population-size: 100\nMutation-rate: 0.15",
                "population-size: 200\nMutation-rate: 0.05",
                "population-size: 200\nMutation-rate: 0.1",
                "population-size: 200\nMutation-rate: 0.15",
                "population-size: 300\nMutation-rate: 0.05",
                "population-size: 300\nMutation-rate: 0.1",
                "population-size: 300\nMutation-rate: 0.15",
            ]
        },

        "Elitism 3": {
            "sheet_names": [
                "Config-100-0.05-2000-3.0-4",
                "Config-100-0.1-2000-3.0-4",
                "Config-100-0.15-2000-3.0-4",
                "Config-200-0.05-2000-3.0-4",
                "Config-200-0.1-2000-3.0-4",
                "Config-200-0.15-2000-3.0-4",
                "Config-300-0.05-2000-3.0-4",
                "Config-300-0.1-2000-3.0-4",
                "Config-300-0.15-2000-3.0-4",
            ],
            "config_labels": [
                "population-size: 100\nMutation-rate: 0.05",
                "population-size: 100\nMutation-rate: 0.1",
                "population-size: 100\nMutation-rate: 0.15",
                "population-size: 200\nMutation-rate: 0.05",
                "population-size: 200\nMutation-rate: 0.1",
                "population-size: 200\nMutation-rate: 0.15",
                "population-size: 300\nMutation-rate: 0.05",
                "population-size: 300\nMutation-rate: 0.1",
                "population-size: 300\nMutation-rate: 0.15",
            ]
        },
    },

    "all": {
        "Combination of all": {
            "sheet_names": [
                "Config-100-0.05-2000-1.0-4",
                "Config-100-0.05-2000-2.0-4",
                "Config-100-0.05-2000-3.0-4",
                "Config-100-0.1-2000-1.0-4",
                "Config-100-0.1-2000-2.0-4",
                "Config-100-0.1-2000-3.0-4",
                "Config-100-0.15-2000-1.0-4",
                "Config-100-0.15-2000-2.0-4",
                "Config-100-0.15-2000-3.0-4",
                "Config-200-0.05-2000-1.0-4",
                "Config-200-0.05-2000-2.0-4",
                "Config-200-0.05-2000-3.0-4",
                "Config-200-0.1-2000-1.0-4",
                "Config-200-0.1-2000-2.0-4",
                "Config-200-0.1-2000-3.0-4",
                "Config-200-0.15-2000-1.0-4",
                "Config-200-0.15-2000-2.0-4",
                "Config-200-0.15-2000-3.0-4",
                "Config-300-0.05-2000-1.0-4",
                "Config-300-0.05-2000-2.0-4",
                "Config-300-0.05-2000-3.0-4",
                "Config-300-0.1-2000-1.0-4",
                "Config-300-0.1-2000-2.0-4",
                "Config-300-0.1-2000-3.0-4",
                "Config-300-0.15-2000-1.0-4",
                "Config-300-0.15-2000-2.0-4",
                "Config-300-0.15-2000-3.0-4",
            ],
            "config_labels": [
                "population-size: 100\nmutation-rate: 0.05\nElitism: 1%",
                "population-size: 100\nmutation-rate: 0.05\nElitism: 2%",
                "population-size: 100\nmutation-rate: 0.05\nElitism: 3%",
                "population-size: 100\nmutation-rate: 0.1\nElitism: 1%",
                "population-size: 100\nmutation-rate: 0.1\nElitism: 2%",
                "population-size: 100\nmutation-rate: 0.1\nElitism: 3%",
                "population-size: 100\nmutation-rate: 0.15\nElitism: 1%",
                "population-size: 100\nmutation-rate: 0.15\nElitism: 2%",
                "population-size: 100\nmutation-rate: 0.15\nElitism: 3%",
                "population-size: 200\nmutation-rate: 0.05\nElitism: 1%",
                "population-size: 200\nmutation-rate: 0.05\nElitism: 2%",
                "population-size: 200\nmutation-rate: 0.05\nElitism: 3%",
                "population-size: 200\nmutation-rate: 0.1\nElitism: 1%",
                "population-size: 200\nmutation-rate: 0.1\nElitism: 2%",
                "population-size: 200\nmutation-rate: 0.1\nElitism: 3%",
                "population-size: 200\nmutation-rate: 0.15\nElitism: 1%",
                "population-size: 200\nmutation-rate: 0.15\nElitism: 2%",
                "population-size: 200\nmutation-rate: 0.15\nElitism: 3%",
                "population-size: 300\nmutation-rate: 0.05\nElitism: 1%",
                "population-size: 300\nmutation-rate: 0.05\nElitism: 2%",
                "population-size: 300\nmutation-rate: 0.05\nElitism: 3%",
                "population-size: 300\nmutation-rate: 0.1\nElitism: 1%",
                "population-size: 300\nmutation-rate: 0.1\nElitism: 2%",
                "population-size: 300\nmutation-rate: 0.1\nElitism: 3%",
                "population-size: 300\nmutation-rate: 0.15\nElitism: 1%",
                "population-size: 300\nmutation-rate: 0.15\nElitism: 2%",
                "population-size: 300\nmutation-rate: 0.15\nElitism: 3%",
            ]
        },
    },

    "baseline and best": {
        "Baseline and best": {
            "sheet_names": [
                "Config-100-0.05-2000-1.0-4",
                "Config-300-0.15-2000-3.0-4",
            ],
            "config_labels": [
                "Baseline",
                "Best\npopulation-size=300\nmutation-rate=0.15\nElitism=3%)",
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
    sheet_dicts = sheet_names_map[  k]
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

        plt.figure(figsize=(20, 15))
        plt.boxplot(fitness_values, showmeans=True)
        plt.xticks([i + 1 for i in range(len(sheet_names))], config_labels, rotation=rotation)
        # plt.xlabel("operator combination")
        plt.xlabel("parameter combination")
        plt.ylabel("Best fitness")
        plt.title(key)
        plt.savefig(CubeConstants.graph_directory_name + k + "/" + key + ".png")
        # plt.show()
