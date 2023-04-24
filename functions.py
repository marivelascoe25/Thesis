import matplotlib.pyplot as plt
import numpy as np
import os
import math
#from sklearn.linear_model import LinearRegression
from scipy.stats import linregress

Vds1 = -0.7
Vds2 = -0.5
Vds3 = -0.3
Vds4 = -0.1
loops = 3
n_vds = 4

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

def plot_legends(transfer):
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
    return L, Vds

def plot_titles(transfer):
    ## Get plot title
    T = []
    for i in range(len(transfer)):
        start = transfer[i].index('transfer')
        #T.append(transfer[i][start-14:start-5]) ## Just used when for pg3tWL
        T.append(transfer[i][start-7:start-5])
    #T=list(dict.fromkeys(T))
    T=list(dict.fromkeys(T))
    return T

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

def plot_transfer_curves(T, transfer, L, Vds):
    L = len(T)
    M = len(transfer)
    N = len(transfer[0])
    X_structure = [[0.0 for i in range (M-1)] for k in range(L-1)]
    Y_structure = [[0.0 for i in range (M-1)] for k in range(L-1)]

    ## plotX[][][], 1st corresponding title (U), 2nd corresponding Vds, 3nd actual number X or Y
    for k in range(L-2):
        plt.figure()
        plt.xlabel("Gate Voltage (V)",fontsize=26,fontweight='bold')
        plt.ylabel("Drain Current (A)",fontsize=26,fontweight='bold')
        for i in range(M-1):
            start = transfer[i].index('transfer')
            if transfer[i][start-7:start-5] == T[k]: ## Join all data from one device
            #if transfer[i][start-14:start-5] == T[k]: ## Just used when for pg3tWL
                plt.title(T[k])
                plt.yscale('log')
                ## Print plots
                #Column 6 and 8 corresponds to Ids and Vgs
                ids=6
                vgs=9 ## 9 if loop is added
                X, Y = extract_data(transfer[i],vgs,ids)
                Y = np.absolute(Y)
                X_structure[k][i] = X_structure[k][i] + np.array(X)
                Y_structure[k][i] = Y_structure[k][i] + np.array(Y)    
                #if label
                if Vds[i] == Vds1:                                   
                    plt.plot(X, Y, 'o-', color=u'#1f77b4')#, label=L[i]) 
                elif Vds[i] == Vds2:
                    plt.plot(X, Y, 'o-', color=u'#ff7f0e')#, label=L[i])
                elif Vds[i] == Vds3:
                    plt.plot(X, Y, 'o-', color=u'#2ca02c')#, label=L[i])
                elif Vds[i] == Vds4:
                    plt.plot(X, Y, 'o-', color=u'#d62728')#, label=L[i])
                    
        #plt.legend()
        
        plt.grid()
    return X_structure, Y_structure

def plot_transfer_linear(T, transfer, L, Vds):

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
                if Vds[i] == Vds1:                   
                    plt.plot(X, Y, 'o-', color=u'#1f77b4', label=L[i])
                elif Vds[i] == Vds2:
                    plt.plot(X, Y, 'o-', color=u'#ff7f0e')
                elif Vds[i] == Vds3:
                    plt.plot(X, Y, 'o-', color=u'#2ca02c')
                else: # Vds[i] == -0.1:
                    plt.plot(X, Y, 'o-', color=u'#d62728')
                #plt.quiver(X, np.absolute(Y), label = L[i])
        #plt.legend()
        plt.grid()

def plot_transfer_comparison(T1, T2, transfer1, tranfer2, Vds1, Vds2):
    
    for k in range(len(T1)):
        plt.figure()
        plt.xlabel("Gate Voltage (V)",fontsize=26,fontweight='bold')
        plt.ylabel("Drain Current (A)",fontsize=26,fontweight='bold')

        for i in range(len(transfer1)):
            start = transfer1[i].index('transfer')
            if transfer1[i][start-7:start-5] == T1[k]: ## including all al files of same title (i.e. U1) in a plot
            #if transfer[i][start-14:start-5] == T[k]: ## Just used when for pg3tWL
                plt.title(T1[k])
                plt.yscale('log')
                ## Print plots
                #Column 6 and 8 corresponds to Ids and Vgs
                ids=6
                vgs=9 ## 9 if loop is added
                X, Y = extract_data(transfer1[i],vgs,ids)
                #if label
                if Vds1[i] == Vds1:                   
                    plt.plot(X, np.absolute(Y), 'o-', color=u'#1f77b4')
                elif Vds1[i] == Vds2:
                    plt.plot(X, np.absolute(Y), 'o-', color=u'#ff7f0e')
                elif Vds1[i] == Vds3:
                    plt.plot(X, np.absolute(Y), 'o-', color=u'#2ca02c')
                else: # Vds[i] == -0.1:
                    plt.plot(X, np.absolute(Y), 'o-', color=u'#d62728')
                #plt.quiver(X, np.absolute(Y), label = L[i])
        #plt.legend()
        plt.grid()

def new_for_mean_values(original_list, loop):
    new_list = []

    for i in range(2, len(original_list), loop):
        new_list.append(original_list[i])

    return new_list

def calculate_mean (X):

    # Assuming your data is stored as a 2D numpy array called 'current_data', with shape (num_samples, num_devices * num_files_per_device)
    num_devices = len(X)
    num_after_average = int(len(X[0])/3)
    
    # Calculate the average of the first 3 files for each device
    X_aux = []
    X_avg = []
    X_avg_final = []
    
    for i in range(num_devices-1):
        for k in range(num_after_average-1):
            print("Printing...")
            print(X[i][3*k])
            print("Printing...")
            print(X[i][3*k+1])
            print("Printing...")
            print(X[i][3*k+2])
            
            X_list = zip(X[i][3*k],X[i][3*k+1],X[i][3*k+2])
            #print(X_list)
            X_aux = [sum(x) for x in X_list]
            X_avg.append(X_aux)
        #print(X_avg)
        #print(len(X_avg))
        X_avg_final.append(X_avg)
    #print(X_avg_final)
    #print(len(X_avg_final))    
    #print("Averages")
    #print(device_averages)

def calculate_vth(T, transfer, L, Vds):
    
    for k in range(len(T)):
        plt.figure()
        plt.xlabel("Gate Voltage (V)",fontsize=26,fontweight='bold')
        plt.ylabel(r"$\sqrt{I_{DS}} (A^{1/2})$",fontsize=26,fontweight='bold')
        print(T[k])
        for i in range(len(transfer)):
            
            start = transfer[i].index('transfer')
            if transfer[i][start-7:start-5] == T[k]:
            #if transfer[i][start-14:start-5] == T[k]: ## Just used when for pg3tWL
                plt.title(T[k])
                ## Print plots
                #Column 6 and 8 corresponds to Ids and Vgs
                ids=6
                vgs=9 ## 9 if loop is added
                X, Y0 = extract_data(transfer[i],vgs,ids)
                start_X = int(13*len(X)/40)#X.index(0.7*Vds[i])
                end_X = int(16*len(X)/40)#X.index(0)
                Y = np.array([math.sqrt(abs(x)) for x in Y0])
                X = np.array(X)
                """X_fit = np.array(X).reshape((-1,1))
                Y_fit = np.array(Y)
                model = LinearRegression().fit(X_fit,Y_fit)
                r_sq = model.score(X_fit,Y_fit)
                print(f"coefficient of determination: {r_sq}")                
                print(f"intercept: {model.intercept_}")
                print(f"coefficients: {model.coef_}")
                Y_fitted = model.predict(X_fit)
                """
                
                # Fit a quadratic function to the data
                #coeffs = np.polyfit(X, Y, 2)

                # Find the maximum value of sqrt_id in the linear region
                #max_sqrt_id = np.max(Y[X > 0.5])

                # Find the indices of the data points in the linear region
                #linear_indices = np.where(Y >= max_sqrt_id)[0]
                

                slope, intercept, rvalue, pvalue, stderr = linregress(X[start_X:end_X], Y[start_X:end_X])
                vth = - intercept / slope
                
                Y_fitted = intercept + slope*X[start_X:end_X]
                
                if Vds[i] == Vds1:                   
                    plt.plot(X, Y, 'o-', color=u'#1f77b4')#, label=L[i])
                    plt.plot(X[start_X:end_X],Y_fitted,color=u'#00a5e3', label="Linear Fit")    
                    print(vth)
                elif Vds[i] == Vds2:
                    plt.plot(X, Y, 'o-', color=u'#ff7f0e')
                    plt.plot(X[start_X:end_X],Y_fitted, color=u'#8dd7bf', label="Linear Fit") 
                    print(vth)
                elif Vds[i] == Vds3:
                    plt.plot(X, Y, 'o-', color=u'#2ca02c')
                    plt.plot(X[start_X:end_X],Y_fitted, color=u'#ff96c5', label="Linear Fit") 
                    print(vth)
                elif Vds[i] == -0.1:
                    plt.plot(X, Y, 'o-', color=u'#d62728')
                    plt.plot(X[start_X:end_X],Y_fitted, color=u'#ffbf65', label="Linear Fit") 
                    print(vth)
                #plt.quiver(X, np.absolute(Y), label = L[i])
        plt.legend()
        plt.grid()

def plot_mean_transfer(X,Y,T,transfer,L,Vds):
    num_devices = len(X)
    num_sweeps = len(transfer)
    
    ## X[][], 1st corresponding title (U), 2nd corresponding # files with average from loops
    for k in range(num_devices-1):
        plt.figure()
        plt.xlabel("Gate Voltage (V)",fontsize=26,fontweight='bold')
        plt.ylabel("Drain Current (A)",fontsize=26,fontweight='bold')
        Y[k] = [abs(ele) for ele in Y[k]]  

        for i in range(num_sweeps-1): 
            start = transfer[i].index('transfer')
            if transfer[i][start-7:start-5] == T[k]: ## Join all data from one device
                plt.title(T[k])
                plt.yscale('log')
                ## Print plots 
                print(Y[k][i])
                plt.plot(X[k][i], Y[k][i], 'o-')#, color=u'#1f77b4')#, label=L[3*i]) 

                """
                #if label
                if Vds[i] == Vds1:                                   
                    plt.plot(X[k][i], Y[k][i], 'o-', color=u'#1f77b4')#, label=L[3*i]) 
                elif Vds[3*i] == Vds2:
                    plt.plot(X[k][i], Y[k][i], 'o-', color=u'#ff7f0e')#, label=L[3*i])
                elif Vds[3*i] == Vds3:
                    plt.plot(X[k][i], Y[k][i], 'o-', color=u'#2ca02c')#, label=L[3*i])
                elif Vds[3*i] == Vds4:
                    plt.plot(X[k][i], Y[k][i], 'o-', color=u'#d62728')#, label=L[3*i])
                """    
        #plt.legend() 
        plt.grid()