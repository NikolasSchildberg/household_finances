"""Expects a cat_data.csv file with data corresponding to an year budget,
with expenses described by category. Creates an image with many plots,
each one corresponding to the temporal evolution of a given category,
so one can see how expenses of this category evolved over the year"""

# imports: data libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# reading data and storing in pd.Dataframe
my_data = pd.read_csv("cat_data.csv", index_col=None)

# pre-processing: cleaning final rows (in this case, two extra rows with stats came at the end of data)
rows_to_exclude = 2

# building the plots
for column_index in range(1, len(my_data.columns)):
    plt.subplot(3, 4, column_index)

    # extracting relevant data and labels from dataFrame

    # getting x axis labels (month names) from dF
    source_labels = list(my_data.iloc[:-rows_to_exclude, 0])

    # getting "y" data from dF: the amount spent in each category
    amounts_to_plot = my_data.iloc[:-rows_to_exclude, column_index]

    # preparing data to plot
    y_to_plot = np.array(amounts_to_plot)
    x_to_plot = np.array(range(len(y_to_plot)))

    # formatting x labels: skipping some of them for plot to look cleaner,
    # and storing ticks' positions for later use in plt.xticks()
    display_every = 3   # filtering labels to display
    positions = []      # where to place "kept labels" at plot time
    new_labels = []
    labels_length = len(source_labels)
    for label_index in range(labels_length):

        # choosing the wanted labels, picking one in every 'show_every',
        #  up to last label
        if (
            (
                # displays one label for every "display_every" of them
                label_index % display_every == 0 and
                label_index < labels_length - 2
            ) or
                # displays last one, too
                (label_index == labels_length-1)):

            # if is one of wanted labels: is added to new labels list:

            # making sure it's a string before keeping it
            if(isinstance(source_labels[label_index], str)):
                new_labels.append(source_labels[label_index])
            else:  # its content gets skipped
                new_labels.append('')
            positions.append(x_to_plot[label_index])

    # building the plot
    plt.scatter(x_to_plot, y_to_plot)
    plt.plot(x_to_plot, y_to_plot)
    plt.title(str(amounts_to_plot.name))
    # plt.xlabel("Months")

    # setting x labels
    plt.xticks(ticks=positions, labels=new_labels)
    plt.ylabel("R$ spent")
    plt.grid(True)
    plt.ylim([0, 1.1*max(y_to_plot)])

# setting to display window at max size
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

# fixing spacing and displaying
plt.subplots_adjust(
    top=0.85,
    bottom=0.058,
    left=0.052,
    right=0.989,
    hspace=0.37,
    wspace=0.307)

# main title and getting it shown
plt.suptitle("Monthly expenses by category", fontsize=50)
plt.show()
