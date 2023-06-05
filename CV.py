import matplotlib.pyplot as plt
from functions import *
plt.rcParams.update({'font.size':22})

#dir_path1 = 'Data\\5. CV\\23.05.24\\pg3t(-10)_AgAgCl_Exp2_HigherRange_10cycles.txt'
#dir_path2 = 'Data\\5. CV\\23.05.31\\WE_AgAgCl_RECE_Au_10cycles_Refine.txt'
#dir_path3 = 'Data\\5. CV\\23.05.31\\WE_AgAgCl_RECE_Au_10cycles_Refine_Till1.5V.txt'
dir_path1 = 'Data\\5. CV\\23.06.02\\WE_Aupf3t_RECE_AgAgCl_10cycles.txt'
dir_path2 = 'Data\\5. CV\\23.06.05\\WE_Aupf3t_RECE_Aupf3t_10cycles_D1.txt'
dir_path3 = 'Data\\5. CV\\23.06.05\\WE_Aupf3t_RECE_Aupf3t_10cycles_D3.txt'
dir_path4 = 'Data\\5. CV\\23.06.05\\WE_Aupf3t_RECE_Aupf3t_10cycles_D7.txt'
dir_path5 = 'Data\\5. CV\\23.06.05\\WE_Aupf3t_RECE_Aupf3t_10cycles_U4.txt'

title1 = "D5"
title2 = "D1"
title3 = "D3"
title4 = "D7"
title5 = "U4"

#plot_CV (dir_path, WE, Ref), WE: Working Electrode, Ref: Reference Electrode
plot_CV(dir_path1, title1, "Au/p(g3T2-T)", "Ag/AgCl")
plot_CV(dir_path2, title2, "Au/p(g3T2-T)", "Au/p(g3T2-T)")
plot_CV(dir_path3, title3, "Au/p(g3T2-T)", "Au/p(g3T2-T)")
plot_CV(dir_path4, title4, "Au/p(g3T2-T)", "Au/p(g3T2-T)")
plot_CV(dir_path5, title5, "Au/p(g3T2-T)", "Au/p(g3T2-T)")

plt.show()