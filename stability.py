import matplotlib.pyplot as plt
from functions import *

dir_path1 = 'Data\\4. Stability\\230517_pg3t_patterned_IV\\U2_m02_ID2-1.txt'
dir_path2 = 'Data\\4. Stability\\230517_pg3t_patterned_bioprobe\\U2_m01_stability1-1.txt'

title1 = "Patterned p(g3T2-T) in GB"#_23.03.20"
title2 = "Patterned p(g3T2-T) in air"

## Store files
#transfer1, stab1 = read_directory_bioprobe(dir_path1)
#transfer2, stab2 = read_directory_bioprobe(dir_path2)

stability(dir_path1, title1)
stability(dir_path2, title2)

plt.show()