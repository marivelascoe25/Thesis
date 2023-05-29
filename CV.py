import matplotlib.pyplot as plt
from functions import *
plt.rcParams.update({'font.size':22})

dir_path1 = 'Data\\5. CV\\23.05.24\\pg3t(-10)_AgAgCl_Exp2_HigherRange_10cycles.txt'

#plot_CV (dir_path, WE, Ref), WE: Working Electrode, Ref: Reference Electrode
plot_CV(dir_path1, "Ag/AgCl" , "Au/p(g3T2-T)")

plt.show()