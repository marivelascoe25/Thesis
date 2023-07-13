import matplotlib.pyplot as plt
from functions import *
from scipy.interpolate import make_interp_spline, BSpline
plt.rcParams.update({'font.size':22})

## Doping effect
#file_path1 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230406_pg3t09.03\\U3_m01_transfer1-02_trans_drain=-7.000e-01_Loop1=2.txt'
#file_path2 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230406_pg3t_doped5_09.03\\D7_m01_transfer1-02_trans_drain=-7.000e-01_Loop1=2.txt'
#file_path3 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230411_pg3t_doped10_09.03\\U5_m01_transfer1-02_trans_drain=-7.000e-01_Loop1=2.txt'

## Reduction step effect
#file_path1 = 'Data\\3. Transfer curves\\3. Data_on_bioprobe_older_PC\\230316_newpg3t\\U4_m01_transfer1-11_trans_drain=-1.000e-01_Loop1=2.txt'
#file_path2 = 'Data\\3. Transfer curves\\2. Bioprobe\\230602_pg3t_SolidSE_aftertrialsGB_aftergatededoping\\D5_m01_transfer1-3_trans_drain=-1.000e-01.txt'

## Before and after exposure
#file_path1 = 'Data\\3. Transfer curves\\1. IV\\230601_new_pg3t+dropSSE_aftergatededoping\\U3_m01_transfer1-1_trans_drain=-1.000e-01.txt'
#file_path2 = 'Data\\3. Transfer curves\\1. IV\\230601_new_pg3t+dropSSE_aftergatededoping_after60sexposure\\U3_m01_transfer1-1_trans_drain=-1.000e-01.txt'
#file_path1 = 'Data\\3. Transfer curves\\1. IV\\230601_new_pg3t+dropSSE_aftergatededoping\\U3_m01_transfer1-2_trans_drain=-5.000e-02.txt'
#file_path2 = 'Data\\3. Transfer curves\\1. IV\\230601_new_pg3t+dropSSE_aftergatededoping_after60sexposure\\U3_m01_transfer1-2_trans_drain=-5.000e-02.txt'

## Doping with Solid state device
#file_path1 = 'Data\\3. Transfer curves\\1. IV\\230614_pg3t_photopattternSSE\\D6_m01_transfer1-1.txt'
#file_path2 = 'Data\\3. Transfer curves\\1. IV\\230629_doped_pg3t_5mgmlF6TCNNQ_photopattternSSE\\D3_m01_transfer1-1.txt'

## After heating (hopefully deoxidazing)
file_path1 = 'Data\\3. Transfer curves\\1. IV\\230629_doped_pg3t_5mgmlF6TCNNQ_printedSSE\\U1_m01_transfer1-1.txt'
file_path2 = 'Data\\3. Transfer curves\\1. IV\\230711_doped_pg3t_5mgmlF6TCNNQ_printedSSE\\U1_secondtimevthshift_transfer1-1.txt'
file_path3 = 'Data\\3. Transfer curves\\1. IV\\230711_doped_pg3t_5mgmlF6TCNNQ_printedSSE\\U1_m02_afterheating120C_transfer1-1.txt'
file_path4 = 'Data\\3. Transfer curves\\1. IV\\230712_doped_pg3t_5mgmlF6TCNNQ_printedSSE\\U1_m01_onedayafterheating_transfer1-1.txt'

Leg1 = "First measurement 29.06"
Leg2 = "After exposure to air, 11/07" ## I printed SSE on top of the remaining 6 devices
Leg3 = "Immediately after heating 11/07"
Leg4 = "Next day of heating 12/07"
#Leg2 = "After exposure"

transfer = [file_path1, file_path2, file_path3, file_path4]
legends = [Leg1, Leg2, Leg3, Leg4] 
#title = "Doping effect @ Vds = -0.7V"
title = "Trying heat de reduce oxidized? doped-p(g3T2-T) device"
#vgs = [9, 7]
#ids = [6, 5]
vgs = [6, 6, 6, 6]
ids = [3, 3, 3, 3]

plots_comparison(title, legends, transfer, vgs, ids)

plt.show()