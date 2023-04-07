import matplotlib.pyplot as plt
import numpy as np
import os

def extract_data(dir,x,y):
    X, Y = [], []
    for line in open(dir, 'r'):
        sline = line.split('\t')    
        try:
            X.append(float(sline[x]))
            Y.append(float(sline[y]))
        except:
            pass
    return X,Y

def absorbance(files, N=False):
    X1, R = extract_data(files[0],0,1)
    X2, T = extract_data(files[1],0,1)
    A = 100*np.ones(len(X2)) - T - R
    if N:
        maxA = np.max(A)
        A = A/maxA

    return X1, A

def read_directory_UV(dir_path):
    R = []
    T = []
    # Iterate directory
    for path in os.listdir(dir_path):
    # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            if path[0] == 'T':
                T.append(dir_path + '\\' + path)
            else:
                R.append(dir_path + '\\' + path)
    return R, T

def read_directory_bioprobe(dir_path):
    transfer = []
    out = []
    # Iterate directory
    for path in os.listdir(dir_path):
    # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            if 'transfer' in path:
                transfer.append(dir_path + '\\' + path)
            else:
                out.append(dir_path + '\\' + path)
    return transfer, out

def plot_absorbance(dir_path,title,x_axis,y_axis,N=False):
    ## Store files
    R, T = read_directory_UV(dir_path)
    L = []

    ## Get plot legends
    for i in range(len(R)):
        start = R[i].index('R_')
        try:
            end = R[i].index('_Storage')
        except:
            end = start+14
        L.append(R[i][start+2:end])

    ## Print plots

    AX = []
    AY = []
    max_aux = []
    max = []

    plt.figure()
    plt.title(title,fontsize=28,fontweight='bold')
    plt.xlabel(x_axis,fontsize=25,fontweight='bold')
    plt.ylabel(y_axis,fontsize=25,fontweight='bold')
    #plt.xlim([300, 2000])
    plt.xlim([300, 1600])

    for i in range (len(T)):
        files = [R[i], T[i]]
        X, Y = absorbance(files,N)
        AX.append(X)
        AY.append(Y)
        plt.plot(AX[i], AY[i], label = L[i])
    #print (AX[2])
    #print (len(AX[2]))
    plt.legend()
    plt.grid()
    return AX, AY, L


def plot_multiple_abs(dir_paths,titles,x_axis,y_axis):
    n = len(dir_paths)
    fig, axs = plt.subplots(n, sharex=True,sharey=True)
    fig.text(0.5, 0.04, x_axis, ha='center')
    fig.text(0.04, 0.5, y_axis, va='center', rotation='vertical')

    for k in range(n):
        ## Store files
        R, T = read_directory_UV(dir_paths[k])
        L = []

        ## Get plot legends
        for i in range(len(R)):
            start = R[i].index('R_')
            try:
                end = R[i].index('_Storage')
            except:
                end = start+14
            L.append(R[i][start+2:end])

        ## Print plots

        AX = []
        AY = []

        axs[k].set_title(titles[k])
        #plt.xlim([300, 1400])
        #axs[k].set_xlim([300, 1400])

        for i in range (len(T)):
            files = [R[i], T[i]]
            X, Y = absorbance(files)
            axs[k].plot(X, Y, label = L[i])
        axs[k].legend()
        axs[k].grid()

def plot_transfer_curves(dir_path):
    ## Store files
    transfer, out = read_directory_bioprobe(dir_path)
    
    ## Get plot legends
    L = []
    for i in range(len(transfer)):
        start = transfer[i].index('drain')
        end = transfer[i].index('e-01')
        label = str(float(transfer[i][start+6:end+4]))
        L.append(r'$V_{DS}$ = '+label+'V')


    ## Get plot title
    T = []
    for i in range(len(transfer)):
        start = transfer[i].index('transfer')
        #T.append(transfer[i][start-14:start-5]) ## Just used when for pg3tWL
        T.append(transfer[i][start-7:start-5])
    #T=list(dict.fromkeys(T))
    T=list(dict.fromkeys(T))


    for k in range(len(T)):
        plt.figure()
        plt.xlabel("Gate Voltage (V)")
        plt.ylabel("Drain Current (A)")

        for i in range(len(transfer)):
            start = transfer[i].index('transfer')
            if transfer[i][start-7:start-5] == T[k]:
            #if transfer[i][start-14:start-5] == T[k]: ## Just used when for pg3tWL
                plt.title(T[k])
                plt.yscale('log')
                ## Print plots
                #Column 6 and 8 corresponds to Ids and Vgs
                ids=6
                vgs=9 ## 9 if loop is added
                X, Y = extract_data(transfer[i],vgs,ids)
                plt.plot(X, np.absolute(Y), label = L[i])
                #plt.quiver(X, np.absolute(Y), label = L[i])
        plt.legend()
        plt.grid()

def plot_transfer_curves2(dir_path):
    ## Store files
    transfer, out = read_directory_bioprobe(dir_path)

    ## Get plot legends
    L = []
    Vds = []
    for i in range(len(transfer)):
        start = transfer[i].index('drain')
        end = transfer[i].index('e-01')
        vds = float(transfer[i][start+6:end+4])
        label = str(vds)
        Vds.append(vds)
        L.append(r'$V_{DS}$ = '+label+'V')

    ## Get plot title
    T = []
    for i in range(len(transfer)):
        start = transfer[i].index('transfer')
        #T.append(transfer[i][start-14:start-5]) ## Just used when for pg3tWL
        T.append(transfer[i][start-7:start-5])
    #T=list(dict.fromkeys(T))
    T=list(dict.fromkeys(T))


    for k in range(len(T)):
        plt.figure()
        plt.xlabel("Gate Voltage (V)",fontsize=26,fontweight='bold')
        plt.ylabel("Drain Current (A)",fontsize=26,fontweight='bold')

        for i in range(len(transfer)):
            start = transfer[i].index('transfer')
            if transfer[i][start-7:start-5] == T[k]:
            #if transfer[i][start-14:start-5] == T[k]: ## Just used when for pg3tWL
                plt.title(T[k])
                plt.yscale('log')
                ## Print plots
                #Column 6 and 8 corresponds to Ids and Vgs
                ids=6
                vgs=9 ## 9 if loop is added
                X, Y = extract_data(transfer[i],vgs,ids)
                #if label
                if Vds[i] == -0.7:                   
                    plt.plot(X, np.absolute(Y), 'o-', color=u'#1f77b4')
                elif Vds[i] == -0.5:
                    plt.plot(X, np.absolute(Y), 'o-', color=u'#ff7f0e')
                elif Vds[i] == -0.3:
                    plt.plot(X, np.absolute(Y), 'o-', color=u'#2ca02c')
                else: # Vds[i] == -0.1:
                    plt.plot(X, np.absolute(Y), 'o-', color=u'#d62728')
                #plt.quiver(X, np.absolute(Y), label = L[i])
        #plt.legend()
        plt.grid()

def plot_transfer_linear(dir_path):
    ## Store files
    transfer, out = read_directory_bioprobe(dir_path)

    ## Get plot legends
    L = []
    Vds = []
    for i in range(len(transfer)):
        start = transfer[i].index('drain')
        end = transfer[i].index('e-01')
        vds = float(transfer[i][start+6:end+4])
        label = str(vds)
        Vds.append(vds)
        L.append(r'$V_{DS}$ = '+label+'V')

    ## Get plot title
    T = []
    for i in range(len(transfer)):
        start = transfer[i].index('transfer')
        #T.append(transfer[i][start-14:start-5]) ## Just used when for pg3tWL
        T.append(transfer[i][start-7:start-5])
    #T=list(dict.fromkeys(T))
    T=list(dict.fromkeys(T))


    for k in range(len(T)):
        plt.figure()
        plt.xlabel("Gate Voltage (V)",fontsize=26,fontweight='bold')
        plt.ylabel("Drain Current (mA)",fontsize=26,fontweight='bold')

        for i in range(len(transfer)):
            start = transfer[i].index('transfer')
            if transfer[i][start-7:start-5] == T[k]:
            #if transfer[i][start-14:start-5] == T[k]: ## Just used when for pg3tWL
                plt.title(T[k])
                #plt.yscale('log')
                ## Print plots
                #Column 6 and 8 corresponds to Ids and Vgs
                ids=6
                vgs=9 ## 9 if loop is added
                X, Y0 = extract_data(transfer[i],vgs,ids)
                Y = [x * 1000 for x in Y0]
                if Vds[i] == -0.7:                   
                    plt.plot(X, Y, 'o-', color=u'#1f77b4')
                elif Vds[i] == -0.5:
                    plt.plot(X, Y, 'o-', color=u'#ff7f0e')
                elif Vds[i] == -0.3:
                    plt.plot(X, Y, 'o-', color=u'#2ca02c')
                else: # Vds[i] == -0.1:
                    plt.plot(X, Y, 'o-', color=u'#d62728')
                #plt.quiver(X, np.absolute(Y), label = L[i])
        #plt.legend()
        plt.grid()


def plot_transfer_comparison(dir_path):
    ## Store files
    transfer, out = read_directory_bioprobe(dir_path)

    ## Get plot legends
    L = []
    for i in range(len(transfer)):
        start = transfer[i].index('drain')
        end = transfer[i].index('e-01')
        label = transfer[i][start+6:end] ##just for doping_effect folder
        L.append(label) ##just for doping_effect folder


    ## Get plot title
    T = []
    for i in range(len(transfer)):
        start = transfer[i].index('transfer')
        T.append(transfer[i][start-13:start-5]) ## Just used when for doping effect
    #T=list(dict.fromkeys(T))
    T=list(dict.fromkeys(T))


    for k in range(len(T)):
        plt.figure()
        plt.xlabel("Gate Voltage (V)")
        plt.ylabel("Drain Current (A)")

        for i in range(len(transfer)):
            start = transfer[i].index('transfer')
            if transfer[i][start-13:start-5] == T[k]: ## Just used when for doping_effect             
                plt.title(T[k])
                plt.yscale('log')
                ## Print plots
                #Column 6 and 8 corresponds to Ids and Vgs
                ids=6
                igs=10
                vgs=9 ## 9 if loop is added
                X1, Y1 = extract_data(transfer[i],vgs,ids)
                plt.plot(X1, np.absolute(Y1), label = L[i])
                #X2, Y2 = extract_data(transfer[i],vgs,igs)
                #plt.plot(X2, np.absolute(Y2),"--",linewidth=1, label = L[i])
                #plt.quiver(X, np.absolute(Y), label = L[i])
        plt.legend()
        plt.grid()

