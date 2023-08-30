import matplotlib.pyplot as plt
from functions import *
import numpy as np
from numpy import diff
plt.rcParams.update({'font.size':20})

## Master Thesis
#Undoped #U4 transfer
#dir1 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t\\U4_m01_transfer1-11_trans_drain=-1.000e-01_Loop1=2.txt'
#dir1 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t\\D3_m01_transfer1-08_trans_drain=-3.000e-01_Loop1=2.txt'
#dir2 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t\\D3_m01_transfer1-05_trans_drain=-5.000e-01_Loop1=2.txt'
#dir2 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t\\U4_m01_transfer1-02_trans_drain=-7.000e-01_Loop1=2.txt'

#Doped 5mg/mL #U2 transfer
#dir1 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t_doped5\\U2_m01_transfer1-12_trans_drain=-1.000e-01_Loop1=3.txt'
#dir1 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t_doped5\\U2_m01_transfer1-09_trans_drain=-3.000e-01_Loop1=3.txt'
#dir2 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t_doped5\\U2_m01_transfer1-06_trans_drain=-5.000e-01_Loop1=3.txt'
#dir2 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t_doped5\\U2_m01_transfer1-03_trans_drain=-7.000e-01_Loop1=3.txt'

#Doped 10mg/mL #U4 transfer
dir1 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t_doped10\\U4_m01_transfer1-12_trans_drain=-1.000e-01_Loop1=3.txt'
#dir1 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t_doped10\\U4_m01_transfer1-09_trans_drain=-3.000e-01_Loop1=3.txt'
#dir2 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t_doped10\\U4_m01_transfer1-03_trans_drain=-7.000e-01_Loop1=3.txt'
dir2 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t_doped10\\U4_m01_transfer1-06_trans_drain=-5.000e-01_Loop1=3.txt'


dir = [dir1, dir2]
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
#column_igs=column_vgs+1
#column_loop=column_vgs-1

## One file per loop
start = dir[0].index('Loop1') 
loop_nr = int(dir[0][start+6:start+7])
L, Vds = plot_legends(dir)
c = [u'#FCDE9C', u'#045275']
ylim = [-0.25, 1.25]

gm_values = plot_linear_ids_transconductance(dir, column_ids, column_vgs, loop_nr, L, c, ylim)
#plot_linear_ids_transconductance(dir1, n_ids, n_vgs, loop_nr)
#plot_linear_ids_transconductance(dir2, n_ids, n_vgs, loop_nr)
#gm_values = plot_linear_ids_transconductance_one_vds(dir, column_ids, column_vgs, loop_nr, c, ylim)

for i in range (len(dir)):
    try:
        print (L[i])
    except:
        pass
    print (max(gm_values[i]))
plt.show()


##all loops in one file
loop_nr = 2


