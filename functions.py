#import matplotlib.pyplot as plt
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