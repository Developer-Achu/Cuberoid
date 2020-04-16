import sys

import pandas as pd
import xlrd
import matplotlib.pyplot as plt
import CubeConstants

if len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    print("Invalid argument count")
    exit(0)

xls = xlrd.open_workbook(file_name, on_demand=True)
sheet_names = xls.sheet_names()

df = pd.read_excel(file_name, sheet_name=None)
averages = []
for sheet in sheet_names:
    data = df[sheet]
    averages.append(data.iloc[:, -1])

plt.boxplot(averages, showmeans=True)
plt.xticks([i + 1 for i in range(len(sheet_names))], sheet_names, rotation=45)
# plt.savefig(CubeConstants.image_name)
plt.show()
