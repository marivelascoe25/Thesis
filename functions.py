#import matplotlib.pyplot as plt
import numpy as np
import os

def extract_data(dir):
    X, Y = [], []
    for line in open(dir, 'r'):
        try:
            values = [float(s) for s in line.split()]
            X.append(values[0])
            Y.append(values[1])
        except:
            pass
    return X, Y


def absorbance(files):
    X1, R = extract_data(files[0])
    X2, T = extract_data(files[1])
    A = 100*np.ones(len(X2)) - T - R
    return X1, A


def read_directory(dir_path):
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