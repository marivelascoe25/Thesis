import matplotlib.pyplot as plt
from functions import *

dir_path1 = 'Data\\2. UVVis\\23.02.23_new'
dir_path2 = 'Data\\2. UVVis\\23.02.24'
#dir_path3 = 'Data\\2. UVVis\\Degradation\\pg3t_doped5mg'
#dir_path4 = 'Data\\2. UVVis\\Degradation\\pg3t_doped10mg'
title1 = "Feb23"
title2 = "Feb24"
#title3 = "Doped pg3t with 5mg/mL"
#title4 = "Doped pg3t with 10mg/mL"

x_axis = "Wavelength (nm)"
y_axis = "Absorbance (%)"

#plot_absorbance(dir_path1,title1,x_axis,y_axis)
plot_multiple_abs([dir_path1,dir_path2],[title1,title2],x_axis,y_axis)
#plot_absorbance(dir_path3,title3,x_axis,y_axis)
plt.show()