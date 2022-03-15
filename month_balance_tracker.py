"""Expects a csv file with your balance data for consecutive months,
and plots the monthly balance as a function of time (in months)"""

# imports
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# reading data and storing in pd.Dataframe
my_data = pd.read_csv("month_data2.csv", index_col=None)

# subsetting for data and labels
source_labels = list(my_data.iloc[:, 0])
sb_values = my_data.iloc[:, 1]

# simple data preprocessing: replacing NaNs by the average of neighbor values
# (enough here, exoecting only to see the monthly balance evolve over time)
for index, value in enumerate(sb_values):
    # numbers are kept
    try:
        sb_values.loc[index] = int(value)

    # other types are replaced by neighbors' average
    except:
        if(index > 0):
            sb_values.loc[index] = (sb_values[index-1]+sb_values[index+1])/2
        else:
            print("First value is broken")
            sb_values.loc[index] = 0


# preparing to plot
y_to_plot = np.array(sb_values)
x_to_plot = np.array(range(len(y_to_plot)))

# formatting x labels
skip_each = 6   # filtering labels to display
positions = []  # where to place "kept labels" at plot time
new_labels = []
max_to_loop = len(source_labels)
for index in range(max_to_loop):
    if (
        # the labels to keep
        (index % skip_each == 0 and index < max_to_loop - 2) or
        (index == max_to_loop-2)
    ):
        # making sure it's a string before keeping it
        if(isinstance(source_labels[index], str)):
            new_labels.append(source_labels[index])
        else:  # its content gets skipped
            new_labels.append('')
        positions.append(x_to_plot[index])

# building the plot
plt.scatter(x_to_plot, y_to_plot)
plt.plot(x_to_plot, y_to_plot)
plt.ylim(bottom=0)
plt.suptitle("Monthly Balance Tracker", fontsize=30)
plt.title(
    "(Mock Data: add your month balace to month_data.csv)")
plt.xlabel("Months")

# other plot customizations
plt.xticks(ticks=positions, labels=new_labels)
plt.ylabel("R$")
plt.grid(True)

# setting to display window at max size
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

plt.show()
