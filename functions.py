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

def absorbance(files):
    X1, R = extract_data(files[0],0,1)
    X2, T = extract_data(files[1],0,1)
    A = 100*np.ones(len(X2)) - T - R
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

def plot_absorbance(dir_path,title,x_axis,y_axis):
    ## Store files
    R, T = read_directory_UV(dir_path)
    L = []

    ## Get plot legends
    for i in range(len(R)):
        start = R[i].index('R')
        L.append(R[i][start:start+14])

    ## Print plots

    AX = []
    AY = []

    plt.figure()
    plt.title(title)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.xlim([300, 1400])

    for i in range (len(T)):
        files = [R[i], T[i]]
        X, Y = absorbance(files)
        AX.append(X)
        AY.append(Y)
        plt.plot(AX[i], AY[i], label = L[i])
    plt.legend()


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
            start = R[i].index('R')
            L.append(R[i][start:start+14])

        ## Print plots

        AX = []
        AY = []

        axs[k].set_title(titles[k])
        #plt.xlim([300, 1400])
        axs[k].set_xlim([300, 1400])

        for i in range (len(T)):
            files = [R[i], T[i]]
            X, Y = absorbance(files)
            axs[k].plot(X, Y, label = L[i])
        axs[k].legend()