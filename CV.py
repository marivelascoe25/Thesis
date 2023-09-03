import matplotlib.pyplot as plt
from functions import *
from peakdetect import peakdetect
plt.rcParams.update({'font.size':20})

#dir_path1 = 'Data\\5. CV\\23.05.24'
#dir_path2 = 'Data\\5. CV\\23.05.31'
#dir_path1 = 'Data\\5. CV\\23.06.02'
#dir_path2 = 'Data\\5. CV\\23.06.05'


#dir_path1 = 'Data\\5. CV\\23.06.14'
#dir_path5 = 'Data\\5. CV\\23.06.13'
#dir_path1 = 'Data\\5. CV\\23.06.15'
#dir_path = 'Data\\5. CV\\23.06.29_doped'
#dir_path = 'Data\\5. CV\\23.07.11_doped5mgml'
#dir_path = 'Data\\5. CV\\23.07.20_undoped'

#dir_path = 'Data\\5. CV\\23.06.16_bioprobe'
#dir_path = 'Data\\5. CV\\23.07.06_Jun13'

## Master Thesis
##EC dedoping
#dir_path = 'Data\\5. CV\\23.06.02' ##AgAgCl RECE
dir_path = 'Data\\5. CV\\23.05.31_bioprobe' ##AgAgCl WE

#dropcast ## change from D7 to D3
#file_path = 'Data\\5. CV\\23.06.05\\WE_Aupf3t_RECE_Aupf3t_10cycles_D1.txt'
#dir_path = 'Data\\5. CV\\23.06.05'
#dir_path = 'Data\\5. CV\\23.05.31'
#photo ## change from D5 to U3
#file_path = 'Data\\5. CV\\23.06.14\\WE_Aupg3t_RECE_Aupg3t_10cycles_D5.txt'
#file_path = 'Data\\5. CV\\23.06.15\\WE_Aupg3t_RECE_Aupg3t_10cycles_U3.txt'
#dir_path = 'Data\\5. CV\\23.06.14'
#dir_path = 'Data\\5. CV\\23.06.15'
#dir_path = 'Data\\5. CV\\23.06.16_bioprobe' #color = #996548
#ink
#file_path = 'Data\\5. CV\\23.07.20_undoped\\WE_AuAgNP_RECE_Aupg3t_10cycles_U5.txt'
#doped
#file_path = 'Data\\5. CV\\23.07.11_doped5mgml\\WE_Aupg3t_RECE_Aupg3t_10cycles_U7.txt'

#title1 = "Ag/AgCl as working electrode"

files, titles = read_directory_allfiles(dir_path)
#print(titles)
for i in range(len(files)):
    plot_CV(files[i], titles[i], "Ag/AgCl Gate", "Au/p(g3T2-T) channel")

#plot_CV (file_path, "", "Gate", "Channel")#, WE: Working Electrode, Ref: Reference Electrode

plt.show()