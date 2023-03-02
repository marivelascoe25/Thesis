import matplotlib.pyplot as plt
from functions import *
from scipy.signal import find_peaks_cwt
from peakdetect import peakdetect
import scipy.constants as sc
#from scipy.signal import argrelextrema

dir_path1 = 'Data\\2. UVVis\\23.02.10'
dir_path2 = 'Data\\2. UVVis\\23.02.16'
dir_path3 = 'Data\\2. UVVis\\23.02.23_new'

title1 = "Doping pg3t_23.02.10"
title2 = "Doping pg3t_23.02.16"
title3 = "Doping pg3t_23.02.23"

x_axis = "Wavelength (nm)"
y_axis = "Absorbance (%)"

#plot_absorbance(dir_path1,title1,x_axis,y_axis)
#plot_multiple_abs([dir_path1,dir_path2],[title1,title2],x_axis,y_axis)
#plot_multiple_abs([dir_path1,dir_path2,dir_path3],[title1,title2,title3],x_axis,y_axis)

X, Y, L = plot_absorbance(dir_path3,title3,x_axis,y_axis) ## Add N=True for a normalized absorbance plot

peak_array = []

for i in range(len(X)):
    peaks = peakdetect(Y[i], lookahead=50)
    peak_array.append(peaks)
## Peak array is composed by 4 dimensions?  
## First one defines the number of files to plot
## Second: 0 for peaks, 1 for valleys
## Third: Number of peaks or valleys
## Forth: It would be the actual element

for k in range(len(peak_array)): ## Number of plots
    print(L[k])
    for j in range(len(peak_array[k][0])): ## Number of peaks (if second number were 1: number of valleys)
        #print(peak_array[k][0][j][0])
        wl = X[k][peak_array[k][0][j][0]]  
        E = sc.Planck * sc.c / (sc.eV * wl*(10**-9))
        print(str(wl) + " <> " + str(round(E,2)) + "eV")
        
plt.show()