import matplotlib.pyplot as plt
from functions import *


dir_path = 'Data\Test'

# list to store files
R, T =read_directory(dir_path)

# Print plots

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
    plt.plot(AX[i], AY[i])
    plt.legend(R[i])
plt.show()
