import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size':20})

##Chosen for threshold voltage shift:
## solid OECTs
#means = np.array([-0.297, -0.167, -0.072, -0.094, 0.13, -0.054, 0.36, 0.25])
#std_devs = np.array([0.126, 0.083, 0.059, 0.039, 0,  0, 0.05, 0.13]) ##DopedPrinted Loop3
#labels = ["Undoped\nDrop-SSE\nForward", "Undoped\nDrop-SSE\nBackward", "Undoped\nPhot-SSE\nForward", "Undoped\nPhot-SSE\nBackward", "Undoped\nPrint-SSE", "Doped\nPrint-SSE", "Ox-Undoped\nPhot-SSE\nForward","Ox-Undoped\nPhot-SSE\nBackward"]
#color = ['#045275', '#045275', '#045275', '#045275', '#045275', '#089099','#089099','#089099']

## doping channel
#vds=-0.1V
means = np.array([0.128, 0.071, 0.062]) #Loop3
std_devs = np.array([0.007, 0.006, 0.015]) #Loop3

#vds=-0.3V
means_group2 = np.array([0.107, 0.064, 0.090])  # Second group of data
std_devs_group2 = np.array([0.005, 0.004 , 0.052])  # Second group of data

#vds=-0.5V
means_group3 = np.array([0.121, 0.069, 0.102])  # Second group of data
std_devs_group3 = np.array([0.012, 0.005 , 0.039])  # Second group of data

#vds=-0.7V
means_group4 = np.array([0.142, 0.075, 0.077])  # Second group of data
std_devs_group4 = np.array([0.041, 0.003 , 0.018])  # Second group of data

labels = ['Undoped','5 mg/mL', '10 mg/mL']
c = ['#045275', '#089099', '#7CCBA2', '#FCDE9C']

# X-axis values (assuming you want to space the error bars along the x-axis)
x = np.arange(len(means))
# Set the offset for the second group
x_offset = 0.15

# Set the figure size (width x height in inches)
plt.figure(figsize=(9, 6.5))

# Create a dot plot with error bars
plt.errorbar(x-x_offset, means, yerr=std_devs, fmt='o', markersize=10, capsize=5, linewidth=3, color=c[0], label=r'$V_{DS} = -0.1 V$')
plt.errorbar(x, means_group2, yerr=std_devs_group2, fmt='o', markersize=10, capsize=5, label=r'$V_{DS} = -0.3 V$', linewidth=3, color=c[1])
plt.errorbar(x+x_offset, means_group3, yerr=std_devs_group3, fmt='o', markersize=10, capsize=5, label=r'$V_{DS} = -0.5 V$', linewidth=3, color=c[2])
plt.errorbar(x+2*x_offset, means_group4, yerr=std_devs_group4, fmt='o', markersize=10, capsize=5, label=r'$V_{DS} = -0.7 V$', linewidth=3, color=c[3])

# Set the x-axis labels
plt.xticks(x, labels)

# Add labels and title
plt.xlabel('Dopant concentration', fontweight='bold')
plt.ylabel(r'V$_{Th}$ [V]', fontweight='bold')
#plt.title('Threshold Voltage Shift', fontweight='bold')

plt.ylim(0.025,0.20)
yticks = [0.05, 0.10, 0.15, 0.20]
plt.yticks(yticks)
# Show the plot
plt.tight_layout()
plt.legend()
plt.gca().yaxis.grid()
#plt.grid(True)
plt.show()

