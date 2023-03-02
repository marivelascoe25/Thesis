import matplotlib.pyplot as plt
from functions import *
from scipy.signal import find_peaks_cwt
from peakdetect import peakdetect
import scipy.constants as sc
#from scipy.signal import argrelextrema

dir_path1 = 'Data\\2. UVVis\\23.02.10'
dir_path2 = 'Data\\2. UVVis\\23.02.16'
dir_path3 = 'Data\\2. UVVis\\23.02.23_old'

title1 = "Doping pg3t_23.02.10"
title2 = "Doping pg3t_23.02.16"
title3 = "Doping pg3t_23.02.23"

x_axis = "Wavelength (nm)"
y_axis = "Absorbance (%)"

#plot_absorbance(dir_path1,title1,x_axis,y_axis)
#plot_multiple_abs([dir_path1,dir_path2],[title1,title2],x_axis,y_axis)
#plot_multiple_abs([dir_path1,dir_path2,dir_path3],[title1,title2,title3],x_axis,y_axis)
X, Y, L = plot_absorbance(dir_path3,title3,x_axis,y_axis)


peak_array = []

for i in range(len(X)):
    #peaks = find_peaks_cwt(Y[i], np.arange(1, 550))
    peaks = peakdetect(Y[i], lookahead=50)
    #np.diff(peaks)
    peak_array.append(peaks)

for k in range(len(peak_array)):
    print(L[k])
    for j in range(len(peak_array[k][0])):
        #print(peak_array[k][0][j][0])
        wl = X[k][peak_array[k][0][j][0]]
        E = sc.Planck * sc.c / (sc.eV * wl*(10**-9))
        #print(E)
        print(str(wl) + "nm corresponding to " + str(round(E,2)) + "eV")
        


plt.show()