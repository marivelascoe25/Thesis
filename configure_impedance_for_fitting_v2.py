import numpy as np
import os

os.chdir('./Data1')
dir_path = os.path.dirname(os.path.realpath(__file__))
file_names = []

for file in os.listdir('{}/Data1'.format(dir_path)):
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
