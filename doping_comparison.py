import matplotlib.pyplot as plt
from functions import *
from scipy.interpolate import make_interp_spline, BSpline
plt.rcParams.update({'font.size':22})


file_path1 = 'Data\\3. Transfer curves\\230406_pg3t09.03\\U3_m01_transfer1-02_trans_drain=-7.000e-01_Loop1=2.txt'
file_path2 = 'Data\\3. Transfer curves\\230406_pg3t_doped5_09.03\\D7_m01_transfer1-02_trans_drain=-7.000e-01_Loop1=2.txt'
file_path3 = 'Data\\3. Transfer curves\\230411_pg3t_doped10_09.03\\U5_m01_transfer1-02_trans_drain=-7.000e-01_Loop1=2.txt'

Leg1 = "Undoped"
Leg2 = "Doped 5 mg/mL"
Leg3 = "Doped 10 mg/mL"


transfer = [file_path1, file_path2, file_path3]
Legends = [Leg1, Leg2, Leg3] 
Title = "Doping effect @ Vds = -0.7V"

plot_doping_comparison(Title, Legends, transfer)

plt.show()