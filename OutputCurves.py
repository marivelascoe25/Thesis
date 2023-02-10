import matplotlib.pyplot as plt
from functions import *
from scipy.interpolate import make_interp_spline, BSpline


dir_path = 'Data\\221115_firstDevice_pedotAgGatePrinted\\U2'

## Store files
transfer, out = read_directory_bioprobe(dir_path)

## Get plot legends
L = []
for i in range(len(out)):
    start = out[i].index('out_gate')
    L.append('Vgs'+out[i][start+8:start+19])

## Print plots

AX = []
AY = []

#Column 9 and 8 corresponds to Ids and Vds
ids=9
vds=8

plt.figure()
plt.title("PEDOT:PSS/Ag")
plt.xlabel("Drain voltage (V)")
plt.ylabel("Drain Current (A)")
plt.grid()
#plt.xlim([330, 850])

for i in range (len(out)):
    #print(i)
    X, Y = extract_data(out[i],vds,ids)
    #Y = abs(Y)
    AX.append(X)
    AY.append(Y)
    plt.plot(AX[i], AY[i], label = L[i])
plt.legend()
plt.show()