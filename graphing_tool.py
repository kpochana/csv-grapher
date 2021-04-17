import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import numpy as np

fig, ax = plt.subplots()
fig.subplots_adjust(right = 0.75)

twins = [ax]
plots = []

x_axes = []
y_axes = []
x_label = ""
y_labels = []
line_labels = []

'''
Function that gets labels for x and y axes, including overall x axis label
'''
def get_labels(input_str, manual=False):
    global x_label
    input_str = input_str.rstrip().split(",")
    if(not len(x_axes)):
        if(manual):
            x_label = input("Enter the label for the overall x-axis: ")
        else:
            x_label = input_str[0]
    if(manual):
        return input("Enter the label for this y-axis: ")
    return input_str[1]


# loop to iterate through each csv file given
while(True):
    # get file path and check user decision
    file_path = input("\nEnter the full filepath of your csv file, or <enter> to plot: ")
    if(file_path == ""):
        break
    
    x_vals = []
    y_vals = []
    y_label = ""

    # if the filepath isn't valid go to beginning of loop
    try:
        dataFile = open(file_path, 'r')
    except:
        print("Invalid file path\n")
        continue

    line_labels.append(input("Enter the label for this line: "))

    # get a valid decision on manual axis labels
    while(True):
        try:
            manual_labels = bool({"y" : 1, "Y" : 1, "n" : 0, "N" : 0}[input("Would you like to enter manual axis labels?" +
                                                                        " If not, program takes them from the first line in the csv files (y/n): ")])
            break
        except:
            print("invalid choice\n")
        

    # loop through csv file and grab data values
    index = 0
    for line in dataFile:
        if(index == 0):
            y_label = get_labels(line, manual_labels)
            index += 1
            continue
                
        point = line.split(",")
        x_vals.append(float(point[0]))
        y_vals.append(float(point[1]))
        index += 1

    # after looping through, add these to axis lists
    y_labels.append(y_label)
    x_axes.append(x_vals)
    y_axes.append(y_vals)
    if(len(x_axes) > 1):
        twins.append(ax.twinx())

tkw = dict(size=4, width=1.5)
cmap = plt.get_cmap('gnuplot')
colors = [cmap(i) for i in np.linspace(0, 0.5, len(x_axes))]
for i in range(len(x_axes)):
    if(i > 1):
       twins[i].spines["right"].set_position(("axes", 1.15 + 0.15 * (i-2)))

    pi, = twins[i].plot(x_axes[i], y_axes[i], color=colors[i], label=line_labels[i])
    plots.append(pi)

    twins[i].set_xlim(min(x_axes[i]), max(x_axes[i]))
    twins[i].set_ylim(min(y_axes[i]), max(y_axes[i]))
    twins[i].set_ylabel(y_labels[i])
    twins[i].yaxis.label.set_color(pi.get_color())
    twins[i].tick_params(axis='y', colors=pi.get_color(), **tkw)
    

ax.tick_params(axis='x', **tkw)
ax.set_xlabel(x_label)
ax.legend(handles=plots)
while(True):
        try:
            ax.xaxis.set_minor_locator(MultipleLocator(float(input("Enter the interval for minor ticks in the plot: "))))
            break
        except:
            print("Unable to parse input\n")

plt.title(input("Enter a title for the graph: "))
plt.show()
        
        
    


print("exited")

