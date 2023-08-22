import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
import numpy as np
plt.rcParams.update({'font.size':20})

#SET1 = np.array([6.3,0.1046,0.0707,0.0494])
#SET2 = np.array([44.1, 0.7322, 0.4949, 0.3458])

SET1 = np.array([104.6,70.7,49.4])
SET2 = np.array([0.7322, 0.4949, 0.3458])

#undoped = np.array([0.150688,0.09901,0.09901])
#doped5 = np.array([0.058582,-0.0111064,-0.0111064])
#doped10 = np.array([0.100006667,-0.034073333,-0.0043])
Y = [SET1,SET2]
x =np.array([0,1,2])
#x =np.array([0,1,2,3])

#xx = ['Undoped','5 mg/mL', '10 mg/mL','20 mg/mL']
xx = ['5 mg/mL', '10 mg/mL','20 mg/mL']
L = ['Sheet resistance','Resistivity']

fig, ax = plt.subplots(figsize = (9,6.5))
ax.set_xlabel("Dopant concentration",fontsize=22,fontweight='bold')
#ax.set_ylabel(r"$R_{S}$  (M$\Omega$/sq)",fontsize=22,fontweight='bold')
ax.set_ylabel(r"$R_{S}$  (k$\Omega$/sq)",fontsize=22,fontweight='bold')
ax.tick_params(axis='y')
#ax.set_ylim([-0.1, 6.1])
#plt.gca().yaxis.grid()
ax.get_ygridlines()
ax.set_xticks(x,xx)
ax.plot(x,Y[0],'o--', linewidth=2, markersize=10, label = L[0])
secax = ax.twinx()
secax.plot(x,Y[1],'o--', linewidth=2, markersize=10, label = L[1])
secax.set_ylabel(r"$\rho$ ($\Omega$cm)", fontsize=22,fontweight='bold')
secax.tick_params(axis='y')
#secax.set_ylim([-1, 61])

#ax.grid(True)
#for i in range(2):
    #plt.xticks(x,xx)
    #plt.plot(x,Y[i],'o--', linewidth=1, markersize=14, label = L[i])
    #X2, Y2 = extract_data(transfer[i],vgs,igs)
    #plt.plot(X2, np.absolute(Y2),"--",linewidth=1, label = L[i])
    #plt.quiver(X, np.absolute(Y), label = L[i])

#plt.legend(loc='upper right')
plt.grid()
plt.tight_layout()
plt.show()


