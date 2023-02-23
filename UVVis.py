import matplotlib.pyplot as plt
from functions import *

dir_path1 = 'Data\\2. UVVis\\Degradation\\Pg3t_undoped'
dir_path2 = 'Data\\2. UVVis\\Degradation\\pg3t_doped2mg'
dir_path3 = 'Data\\2. UVVis\\Degradation\\pg3t_doped5mg'
dir_path4 = 'Data\\2. UVVis\\Degradation\\pg3t_doped10mg'
title1 = "Undoped pg3t"
title2 = "Doped pg3t with 2mg/mL"
title3 = "Doped pg3t with 5mg/mL"
title4 = "Doped pg3t with 10mg/mL"

x_axis = "Wavelength (nm)"
y_axis = "Absorbance (%)"

#plot_absorbance(dir_path1,title1,x_axis,y_axis)
plot_multiple_abs([dir_path1,dir_path2,dir_path3,dir_path4],[title1,title2,title3,title4],x_axis,y_axis)
#plot_absorbance(dir_path3,title3,x_axis,y_axis)
plt.show()