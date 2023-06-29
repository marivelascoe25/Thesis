import matplotlib.pyplot as plt
from functions import *
from scipy.interpolate import make_interp_spline, BSpline
plt.rcParams.update({'font.size':22})


#file_path1 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230406_pg3t09.03\\U3_m01_transfer1-02_trans_drain=-7.000e-01_Loop1=2.txt'
#file_path2 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230406_pg3t_doped5_09.03\\D7_m01_transfer1-02_trans_drain=-7.000e-01_Loop1=2.txt'
#file_path3 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230411_pg3t_doped10_09.03\\U5_m01_transfer1-02_trans_drain=-7.000e-01_Loop1=2.txt'

#file_path1 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t\\U4_m01_transfer1-11_trans_drain=-1.000e-01_Loop1=2.txt'
#file_path2 = 'Data\\3. Transfer curves\\2. Bioprobe\\230602_pg3t_SolidSE_aftertrialsGB_aftergatededoping\\D5_m01_transfer1-3_trans_drain=-1.000e-01.txt'

#file_path1 = 'Data\\3. Transfer curves\\1. IV\\230601_new_pg3t+dropSSE_aftergatededoping\\U3_m01_transfer1-1_trans_drain=-1.000e-01.txt'
#file_path2 = 'Data\\3. Transfer curves\\1. IV\\230601_new_pg3t+dropSSE_aftergatededoping_after60sexposure\\U3_m01_transfer1-1_trans_drain=-1.000e-01.txt'

file_path1 = 'Data\\3. Transfer curves\\1. IV\\230601_new_pg3t+dropSSE_aftergatededoping\\U3_m01_transfer1-2_trans_drain=-5.000e-02.txt'
file_path2 = 'Data\\3. Transfer curves\\1. IV\\230601_new_pg3t+dropSSE_aftergatededoping_after60sexposure\\U3_m01_transfer1-2_trans_drain=-5.000e-02.txt'

#Leg1 = "Undoped"
#Leg2 = "Doped 5 mg/mL"
#Leg3 = "Doped 10 mg/mL"
Leg1 = "Before exposure"
Leg2 = "After exposure"

transfer = [file_path1, file_path2]#, file_path3]
legends = [Leg1, Leg2]#, Leg3] 
#title = "Doping effect @ Vds = -0.7V"
title = "@ Vds = -0.05V"
#vgs = [9, 7]
#ids = [6, 5]
vgs = [6, 6]
ids = [3, 3]

plots_comparison(title, legends, transfer, vgs, ids)

plt.show()