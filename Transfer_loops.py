import matplotlib.pyplot as plt
from functions import *
from scipy.interpolate import make_interp_spline, BSpline
plt.rcParams.update({'font.size':20})

## IV
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230613_pg3t_photopattternSSE'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230614_pg3t_photopattternSSE_before'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230614_pg3t_photopattternSSE'
#dir_path = 'Data\\3. Transfer curves\\1. IV\\230615_pg3t_photopattternSSE_from13again'
dir_path = 'Data\\3. Transfer curves\\1. IV\\230621_pg3t_f6tcnnq10_photopattternSSE'

##Bioprobe
#dir_path = 'Data\\3. Transfer curves\\2. Bioprobe\\230616_pg3t_photopattternSSE'

## Store files
transfer, out = read_directory_transfer(dir_path)

## Get plot titles
T = plot_titles(transfer)
#Column 6 and 8 (9 if loop is added) corresponds to Ids and Vgs in previous files
#IV
column_ids=3
column_vgs=6
#bioprobe
#column_ids=5
#column_vgs=7
##old data bioprobe with loops
#column_ids=6
#column_vgs=9
column_loop=column_vgs-1

## Get gradient plots, just one vds but multiple loops
for i in range(len(transfer)):
    plot_transfer_curves_one_vds(T[i], transfer[i], column_ids, column_vgs, column_loop)

## Doping
#c1 = 10 /40
#c2 = 14/40
## Undoping
#c1 = 18/40
#c2 = 21/40
#calculate_vth (T, transfer, L, Vds, c1, c2, column_ids, column_vgs, column_loop)
plt.show()