import matplotlib.pyplot as plt
from functions import *
plt.rcParams.update({'font.size':20})

dir_path1 = 'Data\\4. Stability\\230517_pg3t_patterned_IV\\U2_m02_ID2-1.txt'
dir_path2 = 'Data\\4. Stability\\230517_pg3t_patterned_bioprobe\\U2_m01_stability1-1.txt'
dir_path3 = 'Data\\4. Stability\\230519_pg3t+SSE_patterned_IV\\U2_m01_ID2-1.txt'
dir_path4 = 'Data\\4. Stability\\230519_pg3t+SSE_patterned_bioprobe\\U2_m02_stability1-1.txt'

title1 = "Patterned p(g3T2-T) in GB"#_23.03.20"
title2 = "Patterned p(g3T2-T) in air"
title3 = "Patterned p(g3T2-T) + SSE in GB"
title4 = "Patterned p(g3T2-T) + SSE in air"

## Store files
#transfer1, stab1 = read_directory_bioprobe(dir_path1)
#transfer2, stab2 = read_directory_bioprobe(dir_path2)

stability(dir_path1, title1, log=True)
stability(dir_path2, title2, log=True)
stability(dir_path3, title3, log=True)
stability(dir_path4, title4, log=True)

plt.show()