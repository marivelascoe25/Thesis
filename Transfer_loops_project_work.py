import matplotlib.pyplot as plt
from functions import *
plt.rcParams.update({'font.size':22})

## IV
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230613_pg3t_photopattternSSE'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230614_pg3t_photopattternSSE_before'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230614_pg3t_photopattternSSE'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230615_pg3t_photopattternSSE_from13again'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230621_pg3t_f6tcnnq10_photopattternSSE'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230629_doped_pg3t_5mgmlF6TCNNQ_photopattternSSE'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230706_pg3t_photopattternSSE_remainings13.05'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230711_doped_pg3t_15mgmlF6TCNNQ_printedSSE'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230711_doped_pg3t_5mgmlF6TCNNQ_printedSSE'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230712_doped_pg3t_15mgmlF6TCNNQ_AgNP_printedSSE'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230720_undoped_pg3t_inkSSE'

##Bioprobe
#dir_path = 'Data\\3. Transfer curves\\2. Bioprobe\\230616_pg3t_photopattternSSE'
dir_path = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t'
## Store files
transfer, out = read_directory_transfer(dir_path)

## Get plot titles
T = plot_titles(transfer)
#Column 6 and 8 (9 if loop is added) corresponds to Ids and Vgs in previous files
#IV
#column_ids=3
#column_vgs=6
#bioprobe
#column_ids=5
#column_vgs=7
##old data bioprobe with loops
column_ids=6
column_vgs=9
column_loop=column_vgs-1


## Forward
#d1 = 25.8/40
#d2 = 26.5/40
   
## Backward
d1 = 34/40
d2 = 34.5/40

for i in range(len(transfer)):
    ## Get gradient plots, just one vds but multiple loops
    plot_transfer_curves_one_vds(T[i], transfer[i], column_ids, column_vgs, column_loop)
    ## Calculate Vth for multiple loops
    #calculate_vth_one_vds(T[i], transfer[i], d1, d2, column_ids, column_vgs, column_loop)

plt.show()