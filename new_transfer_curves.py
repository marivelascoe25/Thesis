import matplotlib.pyplot as plt
from functions import *
plt.rcParams.update({'font.size':20})


#dir_path = 'Data\\3. Transfer curves\\230515_ox_pg3t_SSE_ink + heat'
#dir_path = 'Data\\3. Transfer curves\\230515_ox_pg3t_SSE_photo + heat'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230519_pg3t_after_stability'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230519_pg3t+SSE_afterIV+bio'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230522_pg3t+SSE_IV_afterbio'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230531_pg3t+printedSSE_IV'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230601_pg3t+printedSSE_aftergatededoping'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230601_new_pg3t+dropSSE_aftergatededoping'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230601_new_pg3t+dropSSE_aftergatededoping_after60sexposure'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230602_new_pg3t+dropSSE_aftergatededoping_after60sexposure'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230602_new_pg3t+solidSE_aftergatededopingsolid'
#dir_path = 'Data\\3. Transfer curves\\2. Bioprobe\\230602_pg3t_SolidSE_aftertrialsGB_aftergatededoping'
#dir_path = 'Data\\3. Transfer curves\\2. Bioprobe\\230602_pg3t_SolidSE_aftertrialsGB_aftergatededopingx2'
#dir_path = 'Data\\3. Transfer curves\\2. Bioprobe\\230602_pg3t_SolidSE_aftertrialsGB_aftergatededoping'#'Data\\3. Transfer curves\\1. IV\\230602_new_pg3t+solidSE_aftergatededopingsolid'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230605_new_pg3t+solidSE_aftergatededopingsolid'
#dir_path = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t'
dir_path = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t_doped5'
#dir_path = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t_doped10'

## Store files
transfer, out = read_directory_transfer(dir_path)

## Get plot legends
L , Vds = plot_legends(transfer)

## Get plot titles
T = plot_titles_morevds(transfer)
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

## Get plots
# Default loop_case = 1 which is ploting only 2, default gate = False
# Use loop_case = 2 if you want to all loops except the first one
# Use loop_case other if you want to plot all
# trans default is False, if True, transconductance is plotted
#X, Y = plot_transfer_curves_old(T, transfer, L, Vds, column_ids, column_vgs, column_loop)#, number=3)#, loop_case=2)
X, Y, gm = plot_transfer_tranconductance_old(T, transfer, L, Vds, column_ids, column_vgs, column_loop)#, number=3)#, loop_case=2)

## Doping
c1 = 10 /40
c2 = 14/40
## Undoping
#c1 = 18/40
#c2 = 21/40

#calculate_vth (T, transfer, L, Vds, c1, c2, column_ids, column_vgs, column_loop)
plt.show()