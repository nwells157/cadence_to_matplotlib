import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot_data(fig, ax, data, color_array, label_array, label_array_enable_in, legend_enable, line_style, line_style_enable, x_unit, x_offset, y_unit, y_offset, plot_format, title, x_axis_title, y_axis_title, x_min, x_max, limits_enable_x,y_min, y_max, limits_enable_y, linewidth_assign, subplots_en):

    # Loop through columns in data
    for i in range(0, len(data[0])-1, 2): # Iterate by 2 since 2 columns is 1 plot

        # Extract x and y data
        x = data[:, i]*x_unit
        y = data[:, i+1]*y_unit

        if line_style_enable:
            line_style_assign = line_style[i]
        else:
            line_style_assign = '-'

        if label_array_enable_in:
            label_assign = label_array[i]
        else:
            label_assign = label_array


        match plot_format:
            case 1:
                ax.plot(x+x_offset, y+y_offset, color=color_array[i], label=label_assign, linestyle=line_style_assign, linewidth=linewidth_assign)
            case 2:
                ax.semilogx(x+x_offset, y+y_offset, color=color_array[i], label=label_assign, linestyle=line_style_assign, linewidth=linewidth_assign)
            case 3:
                ax.semilogy(x+x_offset, y+y_offset, color=color_array[i], label=label_assign, linestyle=line_style_assign, linewidth=linewidth_assign)
            case 4:
                ax.loglog(x+x_offset, y+y_offset, color=color_array[i], label=label_assign, linestyle=line_style_assign, linewidth=linewidth_assign)
    
    # Add title and labels
    
    # If subplots are on don't plot the title and x axis for each
    if subplots_en:
        # Change font sizes
        ax.set_ylabel(y_axis_title, fontsize=8, fontweight='bold')
    else:
        ax.set_title(title, fontsize=13, fontweight= 'bold')
        ax.set_xlabel(x_axis_title, fontsize=13, fontweight= 'bold')
        ax.set_ylabel(y_axis_title, fontsize=13, fontweight='bold')
        


	# Axis editor data
    if limits_enable_x:
        ax.set_xlim(x_min, x_max)
        
    if limits_enable_y:
        ax.set_ylim(y_min, y_max)

    # Enable the grid
    ax.grid(True)
    ax.minorticks_on()
    
    # Customize the appearance of the minor grid
    ax.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')

    # Add a legend
    if legend_enable:
        legend = ax.legend(loc="upper left")
        legend.get_frame().set_edgecolor('black') # Set the border color
        legend.get_frame().set_linewidth(2) # Set the border thickness

    # Make the border thicker
    for spine in ax.spines.values():
        spine.set_linewidth(2) # Set the border thickness

    # Make the tick labels normal or bold
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)


def init_plot():
    # Use Different Font
    # plt.rcParams['font.family'] = 'Times New Roman'

    # Create axis
    fig_temp, ax_temp = plt.subplots()
    return fig_temp, ax_temp

def save_plot():
    # Auto save png with high dpi
    plt.savefig("plot_data",dpi=1000)
    plt.savefig("plot_data.svg",  format='svg')

    # Automatically adjust the spacing to prevent overlap
    plt.tight_layout(rect=[0, 0.05, 1, 1])

    # Display the plot
    plt.show()



def format_cadence_bad(data):
    data = data.reshape(int(len(data)/2),2)
    
    return data
