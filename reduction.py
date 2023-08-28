import matplotlib.pyplot as plt
from functions import *
plt.rcParams.update({'font.size':20})

#dir_path = 'Data\\4. Stability\\230519_pg3t+SSE_patterned_IV'
#dir_path = 'Data\\4. Stability\\1. IV\\230613_pg3t_photopattternSSE_dedoping'
#dir_path = 'Data\\4. Stability\\1. IV\\230614_pg3t_photopattternSSE_dedoping'
#dir_path = 'Data\\4. Stability\\1. IV\\230620_pg3t_f6tcnnq5_channel_conductivity'
#dir_path = 'Data\\4. Stability\\1. IV\\230620_pg3t_f6tcnnq5+SSE_channel_conductivity'
#dir_path = 'Data\\4. Stability\\1. IV\\230621_pg3t_f6tcnnq5_channel_conductivity'
#dir_path = 'Data\\4. Stability\\1. IV\\230621_pg3t_f6tcnnq_dropSSE_air'
#dir_path = 'Data\\4. Stability\\2. Bioprobe\\230630_pg3t_doped5mgml_channel'
#dir_path = 'Data\\4. Stability\\1. IV\\230629_pg3t_doped_5mgmlF6TCNNQ_printedSSE'
#dir_path = 'Data\\4. Stability\\230522_pg3t+SSE_bioprobe_only'230522_pg3t+SSE_bioprobe_only\D5_m01_Dedoping-1.txt
#dir_path = 'Data\\4. Stability\\230522_pg3t+SSE_IV_afterbio'

## EC de-doping for master thesis
dir_path = 'Data\\4. Stability\\1. IV\\230621_pg3t_f6tcnnq_dropSSE_air'
#dir_path = 'Data\\4. Stability\\230523_new_pg3t+SSE'

## Comparison for master thesis
file_path1 = 'Data\\4. Stability\\230519_pg3t+SSE_patterned_IV\\U2_m01_Dedoping-1.txt'
file_path2 = 'Data\\4. Stability\\1. IV\\230620_pg3t_f6tcnnq5+SSE_channel_conductivity\\U3_m01_Dedoping3-1.txt'
#file_path1 = 'Data\\4. Stability\\230522_pg3t+SSE_bioprobe_only\\D5_m01_Dedoping-1.txt'
#file_path2 = 'Data\\4. Stability\\1. IV\\230621_pg3t_f6tcnnq_dropSSE_air\\D2_m01_Dedoping3-1.txt'


#deox = read_directory_deox(dir_path)
deox = [file_path1, file_path2]
## Get plot titles
#T = plot_titles_deox(deox)

L = ["Undoped", "5 mg/mL"]

#print(T)
# Asigning columns
#columns = [0, 7, 5] #bioprobe
#columns = [0, 5, 7] #bioprobe_old_weird
columns = [0, 3, 6] #IV
range1 = [0,10]
range2 = [10, 50]
ranges = [range1, range2]
colour = [r'#003147', r'#089099']
## Get all plots
#for i in range(len(deox)):
#    stability(deox[i], T[i], columns, ranges, gate=False)#, log=False)
stability_comparison(deox, L, columns, colour)#, log=False)

plt.show()