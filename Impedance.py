import matplotlib.pyplot as plt
from functions import *
plt.rcParams.update({'font.size':20})

#dir_path1 = 'Data\\6. Impedence\\23.05.24\\pg3t(-10)_AgAgCl.txt'
#dir_path1 = 'Data\\6. Impedence\\23.06.05\\D1_m01.txt'
#dir_path2 = 'Data\\6. Impedence\\23.06.05\\D3_m01.txt'
#dir_path = 'Data\\6. Impedence\\23.06.05\\D7_m01.txt'
#dir_path4 = 'Data\\6. Impedence\\23.06.05\\U4_m01.txt'

## Undoped
#dir_path = 'Data\\6. Impedence\\23.06.14'
#dir_path = 'Data\\6. Impedence\\23.06.13'
#dir_path = 'Data\\6. Impedence\\23.07.06_Jun13'

## Doped
#dir_path = 'Data\\6. Impedence\\23.06.29_doped'
#dir_path = 'Data\\6. Impedence\\23.07.11_doped5mgml'
#dir_path = 'Data\\6. Impedence\\23.07.20_undoped'

##Master thesis
#Dropcast SSE
#file_path = 'Data\\6. Impedence\\23.06.05\\D7_m01.txt'
#dir_path = 'Data\\6. Impedence\\23.06.05' ## Devices same conditions
#dir_path = 'Data\\6. Impedence\\23.05.24' ##AgCl
#Photo SSE
#dir_path = 'Data\\6. Impedence\\23.06.14'
#dir_path = 'Data\\6. Impedence\\23.06.13'
#file_path = 'Data\\6. Impedence\\23.06.14\\D5_m01.txt'
#Printed SSE
#dir_path = 'Data\\6. Impedence\\23.07.20_undoped'
#doped and printed SSE
dir_path = 'Data\\6. Impedence\\23.07.11_doped5mgml'

files, titles = read_directory_allfiles(dir_path)

for i in range(len(files)):
    impedance_spec(files[i], titles[i], C=True)#, Nyq=True)

#impedance_spec(file_path, "", C=True)#, Nyq=True)

plt.show()
