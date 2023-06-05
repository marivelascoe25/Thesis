import matplotlib.pyplot as plt
from functions import *
plt.rcParams.update({'font.size':22})

#dir_path1 = 'Data\\6. Impedence\\23.05.24\\pg3t(-10)_AgAgCl.txt'
dir_path1 = 'Data\\6. Impedence\\23.06.05\\D1_m01.txt'
dir_path2 = 'Data\\6. Impedence\\23.06.05\\D3_m01.txt'
dir_path3 = 'Data\\6. Impedence\\23.06.05\\D7_m01.txt'
dir_path4 = 'Data\\6. Impedence\\23.06.05\\U4_m01.txt'

title1 = "D1"
title2 = "D3"
title3 = "D7"
title4 = "U4"

impedance_spec(dir_path1, title1)
impedance_spec(dir_path2, title2)
impedance_spec(dir_path3, title3)
impedance_spec(dir_path4, title4)

plt.show()
