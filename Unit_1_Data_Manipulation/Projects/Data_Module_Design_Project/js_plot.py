import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def double_bar_graph(bar1_label, bar1_values, bar2_label, bar2_values, categories, title, barWidth):
    
    # Determine a list of centers for the first set of bars such that the bars are spaced apart by three barWidths:
    first_bar_centers = [1]
    for i in range(len(bar1_values)-1):
        value_to_append = first_bar_centers[i] + 3 * barWidth
        first_bar_centers.append(value_to_append)

    # Determine a list of centers for the second set of bars such each bar in the second set of bars is positioned 1 barWidth to the right 
    # of its corresponding bar in the first set of bars.
    second_bar_centers = []
    for value in first_bar_centers:
        second_bar_centers.append(value + barWidth)
    
    # Plot the bars:
    plt.bar(first_bar_centers, bar1_values, width = barWidth)
    plt.bar(second_bar_centers, bar2_values, width = barWidth)
    
    # Display the value of the categories along the x-axis:
    # Set the position of each tick to the point between the pair of bars:
    x_tick_positions = []
    for value in first_bar_centers:
        x_tick_positions.append(value + .5 * barWidth)
    # Assign category labels to the xticks rotated 45 degrees, right aligned, and anchored to the xtick:
    plt.xticks(x_tick_positions, categories, rotation = 45, ha = 'right', rotation_mode = 'anchor')

    # Display a title:
    plt.title(title)

    # Display a legend:
    plt.legend([bar1_label,bar2_label])
    
    # Display the plot:
    plt.show()


def compare_to_mean_graphs(dataframe, index_column, records, columns):
    # Set index to selected column:
    dataframe = dataframe.set_index(index_column)
    
    # Generate a list of mean values for each column selected:
    mean_values = []
    for column in columns:
        mean_values.append(dataframe[column].mean())

    # Generate a dataframe containing only the selected records and columns:
    dataframe = dataframe.loc[records,columns]
    
    # Iterate through each record and create a double bar graph that compares that record's column value to the average column value across all records:
    for record in records:
        # Generate a list of column values for each record:
        values = []
        for column in columns:
            values.append(dataframe.loc[record][column])
        # Generate a double bar graph for each record:
        double_bar_graph(record,values,'Mean',mean_values, columns, record, 1)
