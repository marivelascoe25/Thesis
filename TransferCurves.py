import matplotlib.pyplot as plt
from functions import *
from scipy.interpolate import make_interp_spline, BSpline


dir_path = 'Data\\2. UVVis\\23.02.23_new'

## Store files
transfer, out = read_directory_bioprobe(dir_path)

## Get plot title
T = []
for i in range(len(transfer)):
    start = transfer[i].index('transfer')
    T.append(transfer[i][start-7:start-1])

print(T)

## Get plot legends
L = []
for i in range(len(transfer)):
    start = transfer[i].index('drain')
    L.append('Vds'+transfer[i][start+5:start+16])

## Print plots

AX = [[]]
AY = [[]]
plt = []
#Column 6 and 8 corresponds to Ids and Vgs
ids=6
vgs=8
k=-1

for i in range (len(T)):
    X, Y = extract_data(transfer[i],vgs,ids)
    if i==0 or T[i] != T[i-1]:
        k=k+1
        plt.figure()
        plt.title(T[i])
        plt.xlabel("Gate voltage (V)")
        plt.ylabel("Drain Current (A)")
        plt.yscale('log')
        plt.grid()
    AX[k].append(X)
    AY[k].append(Y)
    plt.plot(AX[i], np.absolute(AY[i]), label = L[i])
    plt.legend()
    plt.show()

"""
for i in range (len(transfer)):
    #print(i)
    X, Y = extract_data(transfer[i],vgs,ids)
    AX.append(X)
    AY.append(Y)
    plt.plot(AX[i], np.absolute(AY[i]), label = L[i])
plt.legend()
plt.show()
"""