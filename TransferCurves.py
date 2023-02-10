import matplotlib.pyplot as plt
from functions import *
from scipy.interpolate import make_interp_spline, BSpline


dir_path = 'Data\\221115_firstDevice_pedotAgGatePrinted\\U2'

## Store files
transfer, out = read_directory_bioprobe(dir_path)

## Get plot legends
L = []
for i in range(len(transfer)):
    start = transfer[i].index('drain')
    L.append('Vds'+transfer[i][start+5:start+16])

## Print plots

AX = []
AY = []

#Column 6 and 8 corresponds to Ids and Vgs
ids=6
vgs=8

plt.figure()
plt.title("PEDOT:PSS/Ag")
plt.xlabel("Gate voltage (V)")
plt.ylabel("Drain Current (A)")
plt.yscale('log')
plt.grid()
#plt.xlim([330, 850])

for i in range (len(transfer)):
    #print(i)
    X, Y = extract_data(transfer[i],vgs,ids)
    AX.append(X)
    AY.append(Y)
    plt.plot(AX[i], np.absolute(AY[i]), label = L[i])
plt.legend()
plt.show()