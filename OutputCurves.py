import matplotlib.pyplot as plt
from functions import *
from scipy.interpolate import make_interp_spline, BSpline

#dir_path = 'Data\\3. Transfer curves\\230213_pg3tDMFx4_undoped'
#dir_path = 'Data\\3. Transfer curves\\230223_dopedpg3t_liquidSSE'
#dir_path = 'Data\\3. Transfer curves\\230222_pg3tWL'
dir_path = 'Data\\3. Transfer curves\\221115_firstDevice_pedotAgGatePrinted\\Rawdata'

## Store files
transfer, out = read_directory_bioprobe(dir_path)

## Get plot legends
L = []
for i in range(len(out)):
    start = out[i].index('out_gate')
    try:
        end = out[i].index('e-01')
    except:
        end = out[i].index('e+00')
    label = str(float(out[i][start+9:end+4]))
    L.append(r'$V_{GS}$ = '+label+'V')

## Get plot title
T = []
for i in range(len(out)):
    start = out[i].index('output')
    #T.append(out[i][start-14:start-5]) ## Just used when for pg3tWL
    T.append(out[i][start-10:start-8])
#T=list(dict.fromkeys(T))
T=list(dict.fromkeys(T))

for k in range(len(T)):
    plt.figure()
    plt.xlabel("Drain Voltage (V)")
    plt.ylabel("Drain Current (A)")

    for i in range(len(out)):
        start = out[i].index('output')
        if out[i][start-10:start-8] == T[k]:
        #if out[i][start-14:start-5] == T[k]: ## Just used when for pg3tWL
            plt.title(T[k])
            #plt.yscale('log')
            ## Print plots
            #Column 6 and 8 corresponds to Ids and Vgs
            ids=9
            vgs=8 ## 9 if loop is added
            X, Y = extract_data(out[i],vgs,ids)
            plt.plot(X, Y, label = L[i])
    plt.legend()
    plt.grid()

plt.show()