import matplotlib.pyplot as plt
from functions import *
from scipy.interpolate import make_interp_spline, BSpline
plt.rcParams.update({'font.size':22})


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
dir_path = 'Data\\3. Transfer curves\\1. IV\\230605_new_pg3t+solidSE_aftergatededopingsolid'

## Store files
transfer, out = read_directory_bioprobe(dir_path)

## Get plot legends
L , Vds = plot_legends(transfer)

## Get plot titles
T = plot_titles(transfer)

#Column 6 and 8 (9 if loop is added) corresponds to Ids and Vgs in previous files
#IV
column_ids=3
column_vgs=6
#bioprobe
#column_ids=5
#column_vgs=7
column_loop=column_vgs-1

## Get plots
# Default loop_case = 1 which is ploting only 2, default gate = False
# Use loop_case = 2 if you want to all loops except the first one
# Use loop_case other if you want to plot all
X, Y = plot_transfer_curves(T, transfer, L, Vds, column_ids, column_vgs, column_loop)#, loop_case=2) 

plt.show()