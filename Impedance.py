import matplotlib.pyplot as plt
from functions import *
plt.rcParams.update({'font.size':22})

#dir_path1 = 'Data\\6. Impedence\\23.05.24\\pg3t(-10)_AgAgCl.txt'
#dir_path1 = 'Data\\6. Impedence\\23.06.05\\D1_m01.txt'
#dir_path2 = 'Data\\6. Impedence\\23.06.05\\D3_m01.txt'
#dir_path3 = 'Data\\6. Impedence\\23.06.05\\D7_m01.txt'
#dir_path4 = 'Data\\6. Impedence\\23.06.05\\U4_m01.txt'

## Undoped
#dir_path = 'Data\\6. Impedence\\23.06.14'
#dir_path = 'Data\\6. Impedence\\23.06.13'
#dir_path = 'Data\\6. Impedence\\23.07.06_Jun13'

## Doped
dir_path = 'Data\\6. Impedence\\23.06.29_doped'

files, titles = read_directory_allfiles(dir_path)

for i in range(len(files)):
    impedance_spec(files[i], titles[i], C=True, Nyq=True)

plt.show()
