import matplotlib.pyplot as plt
from functions import *
plt.rcParams.update({'font.size':20})


#dir_path = 'Data\\4. Stability\\1. IV\\230613_pg3t_photopattternSSE_dedoping'
#dir_path = 'Data\\4. Stability\\1. IV\\230614_pg3t_photopattternSSE_dedoping'
#dir_path = 'Data\\4. Stability\\1. IV\\230620_pg3t_f6tcnnq5_channel_conductivity'
#dir_path = 'Data\\4. Stability\\1. IV\\230620_pg3t_f6tcnnq5+SSE_channel_conductivity'
#dir_path = 'Data\\4. Stability\\1. IV\\230621_pg3t_f6tcnnq5_channel_conductivity'
dir_path = 'Data\\4. Stability\\1. IV\\230621_pg3t_f6tcnnq_dropSSE_air'

deox = read_directory_deox(dir_path)

## Get plot titles
T = plot_titles_deox(deox)

# Asigning columns
#columns = [0, 7, 5] #bioprobe
columns = [0, 3, 6] #IV
range1 = [100,120]
range2 = [400, 440]
ranges = [range1, range2]

## Get all plots
for i in range(len(deox)):
    stability(deox[i], T[i], columns, ranges, gate=False)#, log=False)

plt.show()