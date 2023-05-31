import matplotlib.pyplot as plt
from functions import *
plt.rcParams.update({'font.size':22})

dir_path1 = 'Data\\5. CV\\23.05.24\\pg3t(-10)_AgAgCl_Exp2_HigherRange_10cycles.txt'
dir_path2 = 'Data\\5. CV\\23.05.31\\WE_AgAgCl_RECE_Au_10cycles_Refine.txt'
dir_path3 = 'Data\\5. CV\\23.05.31\\WE_AgAgCl_RECE_Au_10cycles_Refine_Till1.5V.txt'

#plot_CV (dir_path, WE, Ref), WE: Working Electrode, Ref: Reference Electrode
plot_CV(dir_path1, "Ag/AgCl" , "Au/p(g3T2-T)")
plot_CV(dir_path2, "Ag/AgCl" , "Au")
plot_CV(dir_path3, "Ag/AgCl" , "Au")

plt.show()