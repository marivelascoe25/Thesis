import numpy as np
import os

"""
def extract_csv_column_data(file_path, column_index):
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        column_data = []
        for row in reader:
            if len(row) > column_index:
                cell_value = row[column_index].replace(',', '.')  # Replacing commas with periods for decimals
                try:
                    column_data.append(float(cell_value))
                except:
                    pass
                    
    return column_data
"""

os.chdir('./Data/6. Impedence/23.06.14')
dir_path = os.path.dirname(os.path.realpath(__file__))
file_names = []

for file in os.listdir('{}/Data/6. Impedence/23.06.14'.format(dir_path)):
    if file.endswith(".txt"):
        file_names.append(file)

for n in file_names:
    frequ, ReZ, minusImZ, Impe, minusPhase = np.loadtxt(n,
                             unpack = True,
                             delimiter = '\t',
                             skiprows=1,
                             usecols=[1,2,3,4,5])

################ data processing #######################

    ImZ = minusImZ * -1
    OUT = np.column_stack((frequ, ReZ, ImZ, Impe, minusPhase))

#################### data output #########################

    np.savetxt('Fitting/Fitconfig_' + n + '.txt', OUT, header='\n\n\n\n\n\nFrequency/Hz\tReZ/Ohm\tImZ/Ohm\tImpedance/Ohm\t-Phase/degree\ttime/s', comments='', delimiter='\t')
