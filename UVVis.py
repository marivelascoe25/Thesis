import matplotlib.pyplot as plt
from functions import *

dir_path1 = 'Data\\2. UVVis\\23.02.10'
dir_path2 = 'Data\\2. UVVis\\23.02.16'
dir_path3 = 'Data\\2. UVVis\\23.01.16'
title1 = "Doping pg3t_23.02.10"
title2 = "Doping pg3t_23.02.16"
title3 = "Doping pg3t_23.01.16"
x_axis = "Wavelength (nm)"
y_axis = "Absorbance (%)"

#plot_absorbance(dir_path1,title1,x_axis,y_axis)
#plot_absorbance(dir_path2,title2,x_axis,y_axis)
plot_multiple_abs([dir_path1,dir_path2,dir_path3],[title1,title2,title3],x_axis,y_axis)
plt.show()