import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.ticker as ticker
import numpy as np
import os
import math
#from sklearn.linear_model import LinearRegression
from scipy.stats import linregress
import csv

#Vds1 = -0.7
#Vds2 = -0.5
#Vds3 = -0.3
#Vds4 = -0.1
Vds1 = -0.1
Vds2 = -0.05
Vds3 = -0.01


def extract_csv_column_data(file_path, column_index):
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        column_data = []
        for row in reader:
            if len(row) > column_index:
                cell_value = row[column_index].replace(',', '.')  # Replacing commas with periods for decimals
                try:
                    column_data.append(float(cell_value))
                except:
                    pass
                    
    return column_data

def extract_data(dir,x,y,z):
    X, Y, Z = [], [], []
    for line in open(dir, 'r'):
        sline = line.split('\t')    
        try:
            X.append(float(sline[x]))
            Y.append(float(sline[y]))
            Z.append(float(sline[z]))
        except:
            pass
    return X,Y,Z

def extract_data_loop2(dir,x,y,n_loop):
    X, Y = [], []
    loop_case = 2
    for line in open(dir, 'r'):
        sline = line.split('\t')
        try:  
            if int(sline[n_loop]) == loop_case:  
                try:
                    X.append(float(sline[x]))
                    Y.append(float(sline[y]))
                except:
                    pass
        except:
            pass
    return X,Y

def extract_data_loops(dir,x,y,n_loop):
    X, Y = [], []
    loop_case = 1
    for line in open(dir, 'r'):
        sline = line.split('\t')
        try:  
            if int(sline[n_loop]) != loop_case:  
                try:
                    X.append(float(sline[x]))
                    Y.append(float(sline[y]))
                except:
                    pass
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

def read_directory_transfer(dir_path):
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

def read_directory_deox(dir_path):
    deox = []
    # Iterate directory
    for path in os.listdir(dir_path):
    # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            if 'Dedoping' in path:
                deox.append(dir_path + '\\' + path)
    return deox

def colorFader(c1,c2,mix=0): #fade (linear interpolate) from color c1 (at mix=0) to c2 (mix=1)
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))

    return mpl.colors.to_hex((1-mix)*c1 + mix*c2)

def plot_CV (dir_path, title, WE, Ref):

    V_All = extract_csv_column_data(dir_path, 0)
    I_All = extract_csv_column_data(dir_path, 2)
    Scan_number = extract_csv_column_data(dir_path, 4)

    total_scan = int(Scan_number[-1])
    matrix_length = int(len(V_All)/total_scan)
    #print(matrix_length)

    Potential = [[0.0 for i in range (matrix_length-1)] for k in range(total_scan-1)]
    Current = [[0.0 for i in range (matrix_length-1)] for k in range(total_scan-1)]

    for j in range (len(Scan_number)):
        if Scan_number[j] != 1:
            index = int(Scan_number[j])
            Potential[index-2].append(V_All[j])
            Current[index-2].append(I_All[j])

    c1 = 'red'
    c2 = 'blue'

    plt.figure(figsize=(12, 7.5))
    plt.title(title)
    plt.xlabel("Potential (V vs " + Ref + ")",fontsize=20,fontweight='bold')
    plt.ylabel("Current @ " + WE + " (A)",fontsize=20,fontweight='bold')
    for i in range (total_scan-1):
        plt.plot(Potential[i], Current[i], '-', color = colorFader(c1,c2,i/(total_scan-1)))
        if i == 0 or i == 8:
            plt.plot(Potential[i], Current[i], '-', color = colorFader(c1,c2,i/(total_scan-1)), label = "Scan" + str(i+2))
    plt.legend()
    plt.grid()

def impedance_spec(dir_path, title):

    Freq = extract_csv_column_data(dir_path, 1)
    Z = extract_csv_column_data(dir_path, 4)
    Phase = extract_csv_column_data(dir_path, 5)
    Z_img = extract_csv_column_data(dir_path, 3) ##complex impedance
    
    #Volumetric capacitance calculation
    C_aux = 2*math.pi*np.array(Freq)*np.array(Z_img)
    C = 1/C_aux

    #Plots:
    #Impedance and phase
    fig, ax1 = plt.subplots()#figsize=(10, 7.5))
    ax1.set_title(title)
    ax2 = ax1.twinx()

    ax1.plot(Freq, Z, 'bo-')
    ax2.plot(Freq, Phase, 'go-')
    ax1.set_yscale('log')
    ax2.set_xscale('log')

    ax1.set_xlabel("Frequency (Hz)",fontsize=24,fontweight='bold')
    ax1.set_ylabel("|Z| (\u03A9)",fontsize=24,fontweight='bold')
    ax1.yaxis.label.set_color('blue')
    ax1.tick_params(axis='y', colors='b')
   
    ax2.set_ylabel("-Phase (°)",fontsize=24,fontweight='bold')
    ax2.yaxis.label.set_color('green')
    ax2.tick_params(axis='y', colors='g')

    # Match the grids of main and secondary plots
    #ax2.set_xticks(ax1.get_xticks())
    #ax2.set_yticks(ax1.get_yticks())

    # Match the x-axis gridlines
    #ax2.set_xticks(ax1.get_xticks())

    # Match the y-axis gridlines approximately
    #ax2_yticks = ax2.get_yticks()
    #ax1_yticks = ax1.get_yticks()
    #ax2_yticks_new = [ax2_yticks[i] for i in range(len(ax2_yticks)) if i < len(ax1_yticks)]
    #ax2.set_yticks(ax2_yticks_new)

    # Set the secondary plot's y-axis tick labels to match the main plot's scale
    #ax2.set_yscale('linear')  # Change to 'log' if the secondary plot should be in logarithmic scale
    #ax2.yaxis.set_major_locator(ticker.FixedLocator(ax1.get_yticks()))
    #ax2.yaxis.set_major_formatter(ticker.FixedFormatter(ax1.get_yticklabels()))
    #ax2.yaxis.set_major_formatter(ticker.FixedFormatter([label.get_text() for label in ax1.get_yticklabels()]))
    
    #fig.suptitle("Temperature down, price up", fontsize=20)
    #fig.autofmt_xdate()
    ax1.grid(color='b', linestyle='--')
    ax2.grid(color='g', linestyle='--')

    #Capacitance
    plt.figure(figsize=(10, 7.5))
    plt.title(title)
    plt.ylabel("Capacitance (C)",fontsize=26,fontweight='bold')
    plt.xlabel("Frequency (Hz)",fontsize=26,fontweight='bold')
    plt.xscale('log')                                     
    plt.plot(Freq, C, 'o-')#, color=u'#1f77b4')
    #plt.legend()
    plt.grid()

def plot_legends(transfer):
    ## Get plot legends
    L = []
    Vds = []
    for i in range(len(transfer)):
        start = transfer[i].index('drain')
        end = transfer[i].index('e-0')
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
        T.append(transfer[i][start-7:start-1])
    #T=list(dict.fromkeys(T))
    T=list(dict.fromkeys(T))
    return T

def plot_titles_deox(deox):
    ## Get plot title
    T = []
    for i in range(len(deox)):
        start = deox[i].index('Dedoping')
        #T.append(transfer[i][start-14:start-5]) ## Just used when for pg3tWL
        T.append(deox[i][start-7:start-1])
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

    plt.figure(figsize=(10, 7.5))
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

def calculate_transconductance(vgs, ids):
    # Calculate the derivative of ids with respect to vgs
    dvgs = np.gradient(vgs)
    dids = np.gradient(ids)
    
    # Calculate transconductance (gm)
    gm = dids / dvgs
    gmax = np.max(gm)*1000
    
    return gm, gmax

def plot_transfer_curves(T, transfer, L, Vds, n_ids, n_vgs, n_loop, trans = False, loop_case = 1):
    num_devices = len(T)
    num_files = len(transfer) # for each vds x loops
   
    X_structure = [[0.0 for i in range (num_files)] for k in range(num_devices)]
    Y_structure = [[0.0 for i in range (num_files)] for k in range(num_devices)]
    gm = [[0.0 for i in range (num_files)] for k in range(num_devices)]
    gmax = [[0.0 for i in range (num_files)] for k in range(num_devices)]

    for k in range(num_devices):
        plt.figure(figsize=(11, 7.5))
        plt.xlabel("Gate Voltage (V)",fontsize=26,fontweight='bold')
        plt.ylabel("Drain Current (A)",fontsize=26,fontweight='bold')
        plt.title(T[k])
        plt.yscale('log')
                
        for i in range(num_files):
            start = transfer[i].index('transfer')
            if transfer[i][start-7:start-5] == T[k]: ## Join all data from one device (U# or D#)
                
                ## Print plots
                if loop_case == 1:
                    X, Y = extract_data_loop2(transfer[i],n_vgs,n_ids,n_loop)
                elif loop_case == 2:
                    X, Y = extract_data_loops(transfer[i],n_vgs,n_ids,n_loop)
                else: 
                    X, Y = extract_data(transfer[i],n_vgs,n_ids)
                gm[k][i], gmax[k][i] = calculate_transconductance(X,Y)
                Y = np.absolute(Y)
                X_structure[k][i] = X_structure[k][i] + np.array(X)
                Y_structure[k][i] = Y_structure[k][i] + np.array(Y)
                #print ("Device" + str(k) + L[i])
                #print (X_structure[k][i])

                #if label
                if Vds[i] == Vds1:                                   
                    plt.plot(X, Y, 'o-', color=u'#1f77b4', label=L[i])
                    #plt.plot(X, gm[k][i], 'o-', color=u'#1f77b4', label=L[i])
                    #plt.text(-1, 0.e-10, gmax[k][i])

                elif Vds[i] == Vds2:
                    plt.plot(X, Y, 'o-', color=u'#ff7f0e', label=L[i])
                    #plt.plot(X, gm[k][i], 'o-', color=u'#1f77b4', label=L[i])
                elif Vds[i] == Vds3:
                    plt.plot(X, Y, 'o-', color=u'#2ca02c', label=L[i])
                    #plt.plot(X, gm[k][i], 'o-', color=u'#1f77b4', label=L[i])
                #elif Vds[i] == Vds4:
                #    plt.plot(X, Y, 'o-', color=u'#d62728', label=L[i])
                else:
                    plt.plot(X, Y, 'o-', label=L[i])
                    
        plt.legend()
        plt.grid()

    ## plotX[][][], 1st corresponding title (U), 2nd corresponding Vds, 3nd actual number X or Y
    if trans:
        for k in range(num_devices):
            fig, ax1 = plt.subplots(figsize=(10, 7.5))
            ax1.set_title(title)
            ax2 = ax1.twinx()

            ax1.plot(Freq, Z, 'bo-')
            ax2.plot(Freq, Phase, 'go-')
            ax1.set_yscale('log')
            ax2.set_xscale('log')

            ax1.set_xlabel("Frequency (Hz)",fontsize=26,fontweight='bold')
            ax1.set_ylabel("|Z| (\u03A9)",fontsize=26,fontweight='bold')
            ax1.yaxis.label.set_color('blue')
            ax1.tick_params(axis='y', colors='b')
        
            ax2.set_ylabel("-Phase (°)",fontsize=26,fontweight='bold')
            ax2.yaxis.label.set_color('green')
            ax2.tick_params(axis='y', colors='g')


        
    return X_structure, Y_structure, gm, gmax

def plot_transfer_linear(T, transfer, L, Vds, n_ids, n_vgs):

    for k in range(len(T)):
        plt.figure(figsize=(10, 7.5))
        plt.xlabel("Gate Voltage (V)",fontsize=26,fontweight='bold')
        plt.ylabel("Drain Current (mA)",fontsize=26,fontweight='bold')

        for i in range(len(transfer)):
            start = transfer[i].index('transfer')
            if transfer[i][start-7:start-5] == T[k]:
            #if transfer[i][start-14:start-5] == T[k]: ## Just used when for pg3tWL
                plt.title(T[k])
                #plt.yscale('log')
                ## Print plots
                X, Y0 = extract_data(transfer[i], n_ids, n_vgs)
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

def plots_comparison(title, legends, transfer,vgs,ids):
    
    num_files = len(transfer) # for each doping file
   
    #for k in range(num_devices):
    plt.figure(figsize=(10, 7.5))
    plt.xlabel("Gate Voltage (V)",fontsize=26,fontweight='bold')
    plt.ylabel("Drain Current (A)",fontsize=26,fontweight='bold')
    plt.title(title,fontweight='bold')
    plt.yscale('log')
    for i in range(num_files):
        ## Print plots
        #Column 6 and 8 corresponds to Ids and Vgs
        #ids=5
        #vgs=7 ## 9 if loop is added
        X, Y, Z = extract_data(transfer[i],vgs[i],ids[i],0)
        Y = np.absolute(Y)
        #X_structure[k][i] = X_structure[k][i] + np.array(X)
        #Y_structure[k][i] = Y_structure[k][i] + np.array(Y)    
        #if label
        #if Vds[i] == Vds1:                                   
        plt.plot(X, Y, 'o-', label=legends[i]) 
        #elif Vds[i] == Vds2:
        #    plt.plot(X, Y, 'o-', color=u'#ff7f0e')#, label=L[i])
        #elif Vds[i] == Vds3:
        #    plt.plot(X, Y, 'o-', color=u'#2ca02c')#, label=L[i])
        #elif Vds[i] == Vds4:
        #    plt.plot(X, Y, 'o-', color=u'#d62728')#, label=L[i])
    plt.legend()
    plt.grid()

    #return X_structure, Y_structure

def mean_values(original_list, loop):
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

def calculate_vth_all_loops(T, transfer, L, Vds, doping):
    
    for k in range(len(T)):
        plt.figure(figsize=(10, 7.5))
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
                print (transfer[i])
                if doping:
                    start_X = int(9*len(X)/40)#X.index(0.7*Vds[i])
                    end_X = int(12*len(X)/40)#X.index(0)
                else:
                    start_X = int(29*len(X)/40)#X.index(0.7*Vds[i])
                    end_X = int(31*len(X)/40)#X.index(0)

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
                
                try:
                    slope, intercept, rvalue, pvalue, stderr = linregress(X[start_X:end_X], Y[start_X:end_X])
                    vth = - intercept / slope
                    
                    Y_fitted = intercept + slope*X[start_X:end_X]
                    
                    if Vds[i] == Vds1:                   
                        plt.plot(X, Y, 'o-', color=u'#1f77b4')#, label=L[i])
                        plt.plot(X[start_X:end_X],Y_fitted,color=u'#00a5e3')#, label="Linear Fit")    
                        print("At " + L[i] + " Vth is " + str(vth))
                    elif Vds[i] == Vds2:
                        plt.plot(X, Y, 'o-', color=u'#ff7f0e')
                        plt.plot(X[start_X:end_X],Y_fitted, color=u'#8dd7bf')#, label="Linear Fit") 
                        print("At " + L[i] + " Vth is " + str(vth))
                    elif Vds[i] == Vds3:
                        plt.plot(X, Y, 'o-', color=u'#2ca02c')
                        plt.plot(X[start_X:end_X],Y_fitted, color=u'#ff96c5')#, label="Linear Fit") 
                        print("At " + L[i] + " Vth is " + str(vth))
                    elif Vds[i] == -0.1:
                        plt.plot(X, Y, 'o-', color=u'#d62728')
                        plt.plot(X[start_X:end_X],Y_fitted, color=u'#ffbf65')#, label="Linear Fit") 
                        print("At " + L[i] + " Vth is " + str(vth))
                    #plt.quiver(X, np.absolute(Y), label = L[i])
                except:
                    pass
        #plt.legend()
        plt.grid()

def plot_second_transfer(T,transfer,L,Vds):
    num_devices = len(T)
    vds_sweep = len(transfer)
    loop = 2
    #N = len(transfer[0])

    X_structure = [[0.0 for i in range (vds_sweep)] for k in range(num_devices)]
    Y_structure = [[0.0 for i in range (vds_sweep)] for k in range(num_devices)]

    ## plotX[][][], 1st corresponding title (U), 2nd corresponding Vds, 3nd actual number X or Y
    for k in range(num_devices):
        plt.figure(figsize=(10, 7.5))
        plt.xlabel("Gate Voltage (V)",fontsize=26,fontweight='bold')
        plt.ylabel("Drain Current (A)",fontsize=26,fontweight='bold')
        for i in range(vds_sweep):
            start = transfer[i].index('transfer')
            nloop = transfer[i].index('Loop1')
            
            if transfer[i][start-7:start-5] == T[k] and int(transfer[i][nloop+6]) == loop: ## Join all data from one device and second loop
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
                    plt.plot(X, Y, 'o-', color=u'#1f77b4', label=L[i]) 
                elif Vds[i] == Vds2:
                    plt.plot(X, Y, 'o-', color=u'#ff7f0e', label=L[i])
                elif Vds[i] == Vds3:
                    plt.plot(X, Y, 'o-', color=u'#2ca02c', label=L[i])
                elif Vds[i] == Vds4:
                    plt.plot(X, Y, 'o-', color=u'#d62728', label=L[i])
                    
        plt.legend()
        plt.grid()
    return X_structure, Y_structure

def calculate_vth_on_loop2(T, transfer, L, Vds):
    num_devices = len(T)
    num_files = len(transfer)
    loop = 2
    #N = len(transfer[0])

    X_structure = [[0.0 for i in range (num_files)] for k in range(num_devices)]
    Y_structure = [[0.0 for i in range (num_files)] for k in range(num_devices)]

    ## plotX[][][], 1st corresponding title (U), 2nd corresponding Vds, 3nd actual number X or Y
    for k in range(num_devices):
        plt.figure(figsize=(10, 7.5))
        plt.xlabel("Gate Voltage (V)",fontsize=26,fontweight='bold')
        plt.ylabel(r"$\sqrt{I_{DS}} (A^{1/2})$",fontsize=26,fontweight='bold')

        for i in range(num_files):
            start = transfer[i].index('transfer')
            nloop = transfer[i].index('Loop1')
            
            if transfer[i][start-7:start-5] == T[k] and int(transfer[i][nloop+6]) == loop: ## Join all data from one device and second loop
                plt.title(T[k])
                print(T[k])
                plt.yscale('log')
                ## Print plots
                #Column 6 and 8 corresponds to Ids and Vgs
                ids=6
                vgs=9 ## 9 if loop is added
                X, Y0 = extract_data(transfer[i],vgs,ids)
                start_X = int(3.5*len(X)/24)#X.index(0.7*Vds[i])
                end_X = int(6*len(X)/24)#X.index(0)
                Y = np.array([math.sqrt(abs(x)) for x in Y0])
                X = np.array(X)    
                
                slope, intercept, rvalue, pvalue, stderr = linregress(X[start_X:end_X], Y[start_X:end_X])
                vth = - intercept / slope
                
                Y_fitted = intercept + slope*X[start_X:end_X]
                
                if Vds[i] == Vds1:                   
                    plt.plot(X, Y, 'o-', color=u'#1f77b4', label=L[i])
                    plt.plot(X[start_X:end_X],Y_fitted,color=u'#00a5e3', label="Linear Fit")    
                    print("At " + L[i] + " Vth is " + str(vth))
                elif Vds[i] == Vds2:
                    plt.plot(X, Y, 'o-', color=u'#ff7f0e', label=L[i])
                    plt.plot(X[start_X:end_X],Y_fitted, color=u'#8dd7bf', label="Linear Fit") 
                    print("At " + L[i] + " Vth is " + str(vth))
                elif Vds[i] == Vds3:
                    plt.plot(X, Y, 'o-', color=u'#2ca02c', label=L[i])
                    plt.plot(X[start_X:end_X],Y_fitted, color=u'#ff96c5', label="Linear Fit") 
                    print("At " + L[i] + " Vth is " + str(vth))
                elif Vds[i] == -0.1:
                    plt.plot(X, Y, 'o-', color=u'#d62728', label=L[i])
                    plt.plot(X[start_X:end_X],Y_fitted, color=u'#ffbf65', label="Linear Fit") 
                    print("At " + L[i] + " Vth is " + str(vth))
                #plt.quiver(X, np.absolute(Y), label = L[i])
        plt.legend()
        plt.grid()

def calculate_average_in_index_range(arr, start_index, end_index):
    selected_elements = arr[start_index : end_index + 1]
    if len(selected_elements) > 0:
        average = sum(selected_elements) / len(selected_elements)
        return average
    else:
        return None  # Return None if no elements fall within the specified index range

def get_index_of_closest_value(arr, target_value):
    closest_index = min(range(len(arr)), key=lambda i: abs(arr[i] - target_value))
    return closest_index

def get_average (X, Y, range):
    
    start_range = get_index_of_closest_value(X, range[0])
    end_range = get_index_of_closest_value(X, range[1])
    Y_avg = calculate_average_in_index_range(Y, start_range, end_range)

    return Y_avg

def stability(stability, title, columns, ranges, gate=True, log=True):

    ## Extract data
    z_column = columns[2]#5
    y_column = columns[1]#7
    x_column = columns[0]#0 ## 9 if loop is added
    X, Y, Z = extract_data(stability,x_column,y_column,z_column)
    #print (stability)
    if log:
        #plt.yscale('log')
        Y = np.absolute(Y)
        Z = np.absolute(Z)
    
    Y_avg1 = get_average (X,Y,ranges[0])
    Y_avg2 = get_average (X,Y,ranges[1])
    print (Y_avg1)
    print (Y_avg2)

    ## Plots
    plt.figure(figsize=(13, 7))
    plt.title(title)#title.set_text('First Plot')
    
    plt.plot(X, Y, 'b-', label = r"$I_{\mathrm{DS}}$")
    if gate:
        plt.plot(X, Z, 'g-', label = r"$I_{\mathrm{GS}}$")
    if log:
        plt.yscale('log')
        #plt.ylim((10**-7,10**-6))
    
    plt.xlabel("Time (s)",fontsize=26,fontweight='bold')
    plt.ylabel("Current (A)",fontsize=26,fontweight='bold')
                
    plt.legend()
    plt.grid()

def calculate_vth(T, transfer, L, Vds, c1, c2, n_ids, n_vgs, n_loop, loop_case = 1):
    for k in range(len(T)):
        plt.figure(figsize=(10, 7.5))
        plt.xlabel("Gate Voltage (V)",fontsize=24,fontweight='bold')
        plt.ylabel(r"$\sqrt{I_{DS}} (A^{1/2})$",fontsize=24,fontweight='bold')
        plt.title(T[k])
        print(T[k])
        for i in range(len(transfer)):
            
            start = transfer[i].index('transfer')
            if transfer[i][start-7:start-5] == T[k]:
            #if transfer[i][start-14:start-5] == T[k]: ## Just used when for pg3tWL
                
                ## Print plots
                if loop_case == 1:
                    X, Y0 = extract_data_loop2(transfer[i],n_vgs,n_ids,n_loop)
                elif loop_case == 2:
                    X, Y0 = extract_data_loops(transfer[i],n_vgs,n_ids,n_loop)
                else: 
                    X, Y0 = extract_data(transfer[i],n_vgs,n_ids)
                
                #Y = np.absolute(Y)
                #X_structure[k][i] = X_structure[k][i] + np.array(X)
                #Y_structure[k][i] = Y_structure[k][i] + np.array(Y)

                #if doping:
                start_X = int(c1*len(X))#X.index(0.7*Vds[i])
                end_X = int(c2*len(X))#X.index(0)
                #else:
                #    start_X = int(29*len(X)/40)#X.index(0.7*Vds[i])
                #    end_X = int(31*len(X)/40)#X.index(0)

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
                
                try:
                    slope, intercept, rvalue, pvalue, stderr = linregress(X[start_X:end_X], Y[start_X:end_X])
                    vth = - intercept / slope
                    
                    Y_fitted = intercept + slope*X[start_X:end_X]
                    
                    if Vds[i] == Vds1:                   
                        plt.plot(X, Y, 'o-', color=u'#1f77b4', label=L[i])
                        plt.plot(X[start_X:end_X],Y_fitted,color=u'#00a5e3')#, label="Linear Fit")    
                        print("At " + L[i] + " Vth is " + str(vth))
                    elif Vds[i] == Vds2:
                        plt.plot(X, Y, 'o-', color=u'#ff7f0e', label=L[i])
                        plt.plot(X[start_X:end_X],Y_fitted, color=u'#8dd7bf')#, label="Linear Fit") 
                        print("At " + L[i] + " Vth is " + str(vth))
                    elif Vds[i] == Vds3:
                        plt.plot(X, Y, 'o-', color=u'#2ca02c', label=L[i])
                        plt.plot(X[start_X:end_X],Y_fitted, color=u'#ff96c5')#, label="Linear Fit") 
                        print("At " + L[i] + " Vth is " + str(vth))
                    #elif Vds[i] == Vds4:
                    #    plt.plot(X, Y, 'o-', color=u'#d62728')
                    #    plt.plot(X[start_X:end_X],Y_fitted, color=u'#ffbf65')#, label="Linear Fit") 
                    #    print("At " + L[i] + " Vth is " + str(vth))
                    #plt.quiver(X, np.absolute(Y), label = L[i])
                except:
                    pass
        plt.legend()
        plt.grid()

def plot_transfer_curves_one_vds(Title, transfer, n_ids, n_vgs, n_loop, trans = False):#3, loop_case = 1):
    
    X, Y, L = extract_data(transfer,n_vgs, n_ids, n_loop)
    Y = np.absolute(Y)

    total_loops = int(L[-1])
    matrix_length = int(len(L)/total_loops)
    
    V_GS = [[0.0 for i in range (matrix_length-1)] for k in range(total_loops)]
    I_DS = [[0.0 for i in range (matrix_length-1)] for k in range(total_loops)]

    
    for j in range (len(L)):
        index = int(L[j])
        V_GS[index-1].append(X[j])
        I_DS[index-1].append(Y[j])
    
    c1 = 'red'
    c2 = 'blue'

    plt.figure(figsize=(11, 7.5))
    plt.xlabel("Gate Voltage (V)",fontsize=26,fontweight='bold')
    plt.ylabel("Drain Current (A)",fontsize=26,fontweight='bold')
    plt.title(Title)
    plt.yscale('log')
            
    for i in range(total_loops):
        plt.plot(V_GS[i], I_DS[i], '-', color = colorFader(c1,c2,i/(total_loops-1)))
        if i == 0 or i == total_loops-1:
            plt.plot(V_GS[i], I_DS[i], '-', color = colorFader(c1,c2,i/(total_loops-1)), label = "Loop" + str(i+1))
    plt.legend()
    plt.grid()

    return X,Y

def calculate_vth_one_vds(Title, transfer, d1, d2, n_ids, n_vgs, n_loop):
    
    X, Y, L = extract_data(transfer,n_vgs, n_ids, n_loop)
    #Y = np.absolute(Y)

    total_loops = int(L[-1])
    matrix_length = int(len(L)/total_loops)
    
    V_GS = [[0.0 for i in range (matrix_length-1)] for k in range(total_loops)]
    sqrtI_DS = [[0.0 for i in range (matrix_length-1)] for k in range(total_loops)]
    Y_fitted = [[0.0 for i in range (matrix_length-1)] for k in range(total_loops)]
    
    for j in range (len(L)):
        index = int(L[j])
        V_GS[index-1].append(X[j])
        sqrtIDSaux = np.array(math.sqrt(abs(Y[j])))
        sqrtI_DS[index-1].append(sqrtIDSaux)

        #start_X = int(c1*len(X))#X.index(0.7*Vds[i])
        #end_X = int(c2*len(X))#X.index(0)

    plt.figure(figsize=(11, 7.5))
    plt.xlabel("Gate Voltage (V)",fontsize=24,fontweight='bold')
    plt.ylabel(r"$\sqrt{I_{DS}} (A^{1/2})$",fontsize=24,fontweight='bold')
    plt.title(Title)
    print (Title)
    
    c1 = 'red'
    c2 = 'blue'

    for i in range(total_loops):
        start_X = int(d1*len(V_GS[i]))#X.index(0.7*Vds[i])
        end_X = int(d2*len(V_GS[i]))#X.index(0)
        #print(len(V_GS[i]))
        #print(V_GS[i][start_X:end_X])
        if i == 0 or i == total_loops-1:
            plt.plot(V_GS[i], sqrtI_DS[i], '-', color = colorFader(c1,c2,i/(total_loops-1)), label = "Loop" + str(i+1))
        else:
            plt.plot(V_GS[i], sqrtI_DS[i], '-', color = colorFader(c1,c2,i/(total_loops-1)))
        
        try:
            slope, intercept, rvalue, pvalue, stderr = linregress(V_GS[i][start_X:end_X], sqrtI_DS[i][start_X:end_X])
            vth = - intercept / slope
            #print (type(V_GS[i][start_X:end_X]))

            Y_fitted[i] = intercept + [x * slope for x in V_GS[i][start_X:end_X]]

            plt.plot(V_GS[i][start_X:end_X],Y_fitted[i], '--',color = colorFader(c1,c2,i/(total_loops-1)))#, label="Linear Fit")    
            print("For loop " + str(i+1) + " Vth is " + str(vth))     
        except:
            pass
        
    plt.legend()
    plt.grid()

    #for i in range(total_loops):
    #    plt.plot(V_GS[i], sqrtI_DS[i], '-', color = colorFader(c1,c2,i/(total_loops-1)))
    #    if i == 0 or i == total_loops-1:
    #        plt.plot(V_GS[i], sqrtI_DS[i], '-', color = colorFader(c1,c2,i/(total_loops-1)), label = "Loop" + str(i+1))
    #plt.legend()
    #plt.grid()