import matplotlib.pyplot as plt
from functions import *
from scipy.interpolate import make_interp_spline, BSpline


dir_path = 'Data\Test'

## Store files
R, T =read_directory_UV(dir_path)
L = []

## Get plot legends
for i in range(len(R)):
    start = R[i].index('R')
    L.append(R[i][start:start+15])

print(L)
## Print plots

AX = []
AY = []

plt.figure()
plt.title("Doping pg3t")
plt.xlabel("Wavelength (nm)")
plt.ylabel("Absorbance (%)")
plt.xlim([330, 850])

for i in range (len(T)):
    #print(i)
    files = [R[i], T[i]]
    X, Y = absorbance(files)
    AX.append(X)
    AY.append(Y)
    #spl = make_interp_spline(AX[i], AY[i], k=15)
    #AY_smooth = spl(AX[i])
    #plt.plot(AX[i], AY_smooth, label = L[i])
    plt.plot(AX[i], AY[i], label = L[i])
plt.legend()
plt.show()