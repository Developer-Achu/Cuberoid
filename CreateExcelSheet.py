import os

import pandas as pd

import CubeConstants

files = sorted(os.listdir(CubeConstants.directory_name))
writer = pd.ExcelWriter(CubeConstants.directory_name + CubeConstants.excel_file_name, engine='xlsxwriter')

for file in files:
    with open(CubeConstants.directory_name + file, 'r') as f:
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
