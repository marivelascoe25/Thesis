import matplotlib.pyplot as plt
from functions import *
from peakdetect import peakdetect
import scipy.constants as sc
plt.rcParams.update({'font.size':22})

#dir_path1 = 'Data\\5. CV\\23.05.24'
#dir_path2 = 'Data\\5. CV\\23.05.31'
#dir_path1 = 'Data\\5. CV\\23.06.02'
#dir_path2 = 'Data\\5. CV\\23.06.05'


#dir_path1 = 'Data\\5. CV\\23.06.14'
#dir_path5 = 'Data\\5. CV\\23.06.13'
#dir_path1 = 'Data\\5. CV\\23.06.15'
dir_path = 'Data\\5. CV\\23.06.29_doped'

#dir_path = 'Data\\5. CV\\23.06.16_bioprobe'
#dir_path = 'Data\\5. CV\\23.07.06_Jun13'


#title1 = "Ag/AgCl as working electrode"

files, titles = read_directory_allfiles(dir_path)
print(titles)

for i in range(len(files)):
    #plot_CV (dir_path, WE, Ref), WE: Working Electrode, Ref: Reference Electrode
    plot_CV(files[i], titles[i], "Au/p(g3T2-T)", "Au/p(g3T2-T)")



plt.show()