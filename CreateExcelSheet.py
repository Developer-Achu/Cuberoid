import os
import sys

import pandas as pd
from openpyxl import load_workbook

import CubeConstants

if len(sys.argv) == 2:
    dir_name = sys.argv[1]
else:
    print("Invalid argument count")
    exit(0)

files = sorted(os.listdir(dir_name))
writer = pd.ExcelWriter(dir_name + "/" + CubeConstants.excel_file_name, engine='xlsxwriter')
sheet_names = []
for file in files:
    sheet_names.append(file)
    with open(dir_name + "/" + file, 'r') as f:
        data_dict = {}
        lines = f.read().split("\n")
        for line in lines:
            if len(line) == 0:
                break
            current_array = line.split()
            key = current_array[0]
            value = current_array[1:]
            data_dict.update({key: value})

        df = pd.DataFrame(data_dict)
        df.to_excel(writer, sheet_name=str(file), index=False)
    f.close()
writer.save()

averages_to_write = []
df = pd.read_excel(dir_name + "/" + CubeConstants.excel_file_name, sheet_name=None)
for sheet in sheet_names:
    data = df[sheet]
    averages = ['average']
    for i in range(data.shape[0]):
        sum_of_retries = 0
        for j in range(1, len(data.columns)):
            sum_of_retries += int(data.loc[i][j])
        averages.append(sum_of_retries / (len(data.columns) - 1))

    averages_to_write.append(averages)


writer = pd.ExcelWriter(dir_name + "/" + CubeConstants.excel_file_name, engine='openpyxl')
for index, averages in enumerate(averages_to_write):
    data_dict = {}
    key = averages[0]
    value = averages[1:]
    data_dict.update({key: value})

    writer.book = load_workbook(dir_name + "/" + CubeConstants.excel_file_name)
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    reader = pd.read_excel(dir_name + "/" + CubeConstants.excel_file_name)

    df = pd.DataFrame(data_dict)
    df.to_excel(writer, sheet_name=sheet_names[index], startcol=6, index=False)
    writer.close()
writer.save()
