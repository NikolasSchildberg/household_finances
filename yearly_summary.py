"""Takes a csv file with data organized as months names as lines
and expenses category as columns (entries are monthly expenses within
 a given category). Plots a bar chart to ease comparison among categories.
 Yearly amounts used here, but monthly amount can be use by changing lines
 (since entries in the line indexed as "-2" is the sum of entries above it)"""

# imports
import matplotlib.pyplot as plt
import pandas as pd

# getting data from csv file
data = pd.read_csv('cat_data.csv', index_col=None)

# preparing data to plot: column -2 corresponds to sum over the year
amounts = data.iloc[-2, 1:-1].sort_values()
labels = list(amounts.keys())
positions = range(1, len(labels)+1)

# plotting and customizing
plt.title("Yearly expenses by category", fontsize='15')
plt.barh(labels, amounts)
plt.grid()
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()
