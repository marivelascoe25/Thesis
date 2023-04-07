import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
import numpy as np
plt.rcParams.update({'font.size':24})

SET1 = np.array([0.150688,0.058582,0.100006667])
SET2 = np.array([0.09901,-0.0111064,-0.034073333])
SET3 = np.array([0.09901,-0.0111064,-0.0043])

#undoped = np.array([0.150688,0.09901,0.09901])
#doped5 = np.array([0.058582,-0.0111064,-0.0111064])
#doped10 = np.array([0.100006667,-0.034073333,-0.0043])
Y = [SET1,SET2,SET3]
x =np.array([0,1,2])
xx = ['Undoped', '5 mg/mL', '10 mg/mL']
L = ['SET 1','SET 2','SET 3']
plt.figure()
plt.xlabel("Dopant concentration",fontsize=26,fontweight='bold')
plt.ylabel("Threshold Voltage (V)",fontsize=26,fontweight='bold')
plt.ylim([-0.05,0.20])
plt.gca().yaxis.grid()

for i in range(3):
    plt.xticks(x,xx)
    plt.plot(x,Y[i],'o--', linewidth=1, markersize=14, label = L[i])
    #X2, Y2 = extract_data(transfer[i],vgs,igs)
    #plt.plot(X2, np.absolute(Y2),"--",linewidth=1, label = L[i])
    #plt.quiver(X, np.absolute(Y), label = L[i])
plt.legend(loc='upper right')
#plt.grid()
plt.show()


