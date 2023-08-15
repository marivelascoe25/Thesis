import matplotlib.pyplot as plt
from functions import *
from peakdetect import peakdetect
import scipy.constants as sc
#from scipy.signal import argrelextrema
plt.rcParams.update({'font.size':22})

dir_path2 = 'Data\\2. UVVis\\0. Old data\\23.03.20'
dir_path1 = 'Data\\2. UVVis\\0. Old data\\23.04.05'
dir_path3 = 'Data\\2. UVVis\\0. Old data\\23.02.23_old'

title2 = "Doping p(g3T2-T)"#_23.03.20"
title1 = "After 2 weeks in air"
title3 = "Doping p(g3T2-T)"

## Add N=True for a normalized absorbance plot
N = False
x_axis = "Wavelength (nm)"
if N:
    y_axis = "Normalized Absorbance (a.u.)"
else:
    y_axis = "Absorbance (%)"

#plot_absorbance(dir_path1,title1,x_axis,y_axis)
#plot_multiple_abs([dir_path1,dir_path2],[title1,title2],x_axis,y_axis)
#plot_multiple_abs([dir_path1,dir_path2,dir_path3],[title1,title2,title3],x_axis,y_axis)

X, Y, L = plot_absorbance(dir_path1,title1,x_axis,y_axis, N)

"""
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
        print(str(wl) + "nm <> " + str(round(E,2)) + "eV")
"""
#plt.savefig("Doping.pdf", format="pdf", bbox_inches="tight")
#plt.legend()
plt.show()