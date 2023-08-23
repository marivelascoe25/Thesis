import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
import numpy as np
plt.rcParams.update({'font.size':20})

#SET1 = np.array([0.150688,0.058582,0.100006667])
#SET2 = np.array([0.09901,-0.0111064,-0.034073333])
#SET3 = np.array([0.09901,-0.0111064,-0.0043])

##Only best on loops:
SET1 = np.array([0.142,0.065,0.050])
SET3 = np.array([0.113,0.060,0.050])
SET5 = np.array([0.118,0.064,0.051])
SET7 = np.array([0.124,0.070,0.0])

#undoped = np.array([0.150688,0.09901,0.09901])
#doped5 = np.array([0.058582,-0.0111064,-0.0111064])
#doped10 = np.array([0.100006667,-0.034073333,-0.0043])
#Y = [SET1,SET2,SET3]
#x =np.array([0,1,2])
#xx = ['Undoped', '5 mg/mL', '10 mg/mL']
#L = ['SET 1','SET 2','SET 3']

Y = [SET1,SET3,SET5,SET7]
x =np.array([0,1,2])
xx = ['Undoped', '5 mg/mL', '10 mg/mL']
L = [r'$V_{DS}$ = - 0.1 V',r'$V_{DS}$ = - 0.3 V',r'$V_{DS}$ = - 0.5 V',r'$V_{DS}$ = - 0.7 V']

plt.figure(figsize=(9,6.5))
plt.xlabel("Dopant concentration",fontsize=20,fontweight='bold')
plt.ylabel(r"$V_{Th}$ (V)",fontsize=20,fontweight='bold')
plt.ylim([0.03,0.15])
plt.gca().yaxis.grid()
colors = [u'#045275', u'#089099', u'#7CCBA2', u'#FCDE9C']

for i in range(len(Y)):
    plt.xticks(x,xx)
    try:
        plt.plot(x,Y[i],'o--', linewidth=2, markersize=14, label = L[i], color=colors[i])
    except:
        pass
    #X2, Y2 = extract_data(transfer[i],vgs,igs)
    #plt.plot(X2, np.absolute(Y2),"--",linewidth=1, label = L[i])
    #plt.quiver(X, np.absolute(Y), label = L[i])
plt.legend(loc='upper right', fontsize=20)
#plt.grid()
plt.tight_layout()
plt.show()


