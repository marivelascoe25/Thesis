import matplotlib.pyplot as plt
from functions import *
from scipy.interpolate import make_interp_spline, BSpline
plt.rcParams.update({'font.size':22})


#dir_path1 = 'Data\\3. Transfer curves\\230316_newpg3t_doped5'
dir_path3 = 'Data\\3. Transfer curves\\230414_ox_pg3t_SSE_ink'
dir_path2 = 'Data\\3. Transfer curves\\230412_pg3t_SSE_solid'
#dir_path1 = 'Data\\3. Transfer curves\\230413_ox_pg3t_SSE_photo'
dir_path1 = 'Data\\3. Transfer curves\\230519_pg3t_after_stability'
#dir_path2 = 'Data\\3. Transfer curves\\230411_pg3t_doped10_09.03'
#dir_path2 = 'Data\\3. Transfer curves\\230411_pg3t_doped5_16.03'
#dir_path1 = 'Data\\3. Transfer curves\\230316_newpg3t_doped5'


## Store files
transfer1, out1 = read_directory_bioprobe(dir_path1)
#transfer2, out2 = read_directory_bioprobe(dir_path2)
#transfer3, out3 = read_directory_bioprobe(dir_path3)

## Get plot legends
L1 , Vds1 = plot_legends(transfer1)
#L2 , Vds2 = plot_legends(transfer2)
#L3 , Vds3 = plot_legends(transfer3)

## Get plot titles
T1 = plot_titles(transfer1)
#T2 = plot_titles(transfer2)
#T3 = plot_titles(transfer3)


## Get plots
#plot_transfer_linear(T1, transfer1, L1, Vds1)
#X, Y = plot_second_transfer(T1, transfer1, L1, Vds1)

#print(len(X[0]))
#print(len(X))
#print(dir_path1)
#calculate_vth_on_loop2(T1, transfer1, L1, Vds1)

#Since hysteresis appears, if no hysteresis, use wichever
#doping = True #For my measurements: From positive to negative 
doping = False #For my measurements: From negative to positive

calculate_vth_all_loops(T1, transfer1, L1, Vds1, doping)

#X_mean = calculate_mean(X)
#Y_mean = calculate_mean(Y)

#loop = 3
#transfer_mean = new_for_mean_values(transfer1,loop)
#L_mean = new_for_mean_values(L1,loop)
#Vds1_mean = new_for_mean_values(Vds1,loop)

#plot_mean_transfer(X_mean, Y_mean, T1, transfer_mean, L_mean, Vds1_mean)

#plot_transfer_comparison(T1, T2, transfer1, transfer2, L1, L2, Vds1, Vds2)

#dir_path = 'Data\\3. Transfer curves\\Thesis\\doping_effect_new_new10\\Vds3'
#plot_doping_comparison(dir_path)

plt.show()