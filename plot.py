import numpy as np
import matplotlib.pyplot as plt

import matplotlib_func

# Parameters
x_unit_in = 1e0;
y_unit_in = 1e0;

# Plot unit (1-plot, 2 semilogx, 3-semilogy, 4-loglog)
plot_format_in = 1

### Import data

# From scope .trc file
# data = np.genfromtxt("./data.trc", delimiter=',', skip_header=5)

# Cadence data good
data = np.genfromtxt("./data.vcvs", delimiter=',', skip_header=6)


# Cadence data bad
# data = np.genfromtxt("./data.vcvs", delimiter=',', skip_header=6)
# data = matplotlib_func.format_cadence_bad(data)

# data1 = np.genfromtxt("./data1.vcvs", delimiter=',', skip_header=6)
# data1 = matplotlib_func.format_cadence_bad(data1)

# data = np.append(data, data1, axis=1)

# Create label array with names for both x and y columns
color_array_in = ["#ff0000","#ff0000","#00ff00","#00ff00","#0000ff","#0000ff","#ffff00","#ffff00","#8000ff","#8000ff","#ff00ff","#ff00ff","#00ffff","#00ffff","#ff8000","#ff8000"]
label_array = ["High pass diff output", "Chip diff output", "chip diff output", "chip diff output"]
line_style_in = ["-", "--", "-.", ":"]

# Defaults
legend_enable_in = 0
x_offset_in = 0
y_offset_in = 0
title_in =  'Title'
x_axis_title_in =  'X Axis Title'
y_axis_title_in =  'Y Axis Title'
x_min_in = 0  
x_max_in = 0
limits_enable_x_in = 0
y_min_in = 0
y_max_in = 0
limits_enable_y_in = 0
line_style_enable_in = 0
linewidth_in = 1

# If 1 need array if 0 need string
label_array_enable_in = 0
if label_array_enable_in:
	label_array_in = label_array
else:
	label_array_in = "label"

### Start Plotting

# Initialize plot axis 
fig, ax = matplotlib_func.init_plot()
# Sub plot notation - use ax1 and ax2 intead of ax in the plot_data function
# fig, (ax1, ax2) = plt.subplots(2, 1)

# Use plot data function here 
matplotlib_func.plot_data(fig, ax, data, color_array_in, label_array_in, label_array_enable_in, legend_enable_in, line_style_in, line_style_enable_in, x_unit_in, x_offset_in, y_unit_in, y_offset_in, plot_format_in, title_in, x_axis_title_in, y_axis_title_in, x_min_in, x_max_in, limits_enable_x_in,y_min_in, y_max_in, limits_enable_y_in, linewidth_in)

# Plot and save data function
matplotlib_func.save_plot()