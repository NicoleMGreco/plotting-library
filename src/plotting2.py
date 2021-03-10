#!/bin/python

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def read_data(filename):
    # Create an array (a multi-dimensional table) out of our data file, full of text
    all_data = np.genfromtxt(filename, delimiter=',',skip_header=1)
    print(all_data)

    # Select the data range we are interested in, convert it into a new array, full of numbers
    grainsize_data = np.array(all_data[1:,:], dtype=float)
    print(grainsize_data)
    return grainsize_data
grainsize_data = read_data("../gs_data.csv")

# Compute a new column by multiplying column number 1 to Kelvin
grainsize_calculated = (grainsize_data[:,0,None] - 5) * 2

# Append this new column to the existing temperature_data array
processed_grainsize_data = np.append(grainsize_data, grainsize_calculated,1)
print (processed_grainsize_data)

# Create a figure of the processed data
grainsize_figure = plt.figure()
grainsize_plot = plt.plot (processed_grainsize_data[:,2],processed_grainsize_data[:,1])
plt.xlabel("Diameter(microns)")
plt.ylabel("Concentration")
plt.title("Grain Size Data")
grainsize_figure.savefig('results/grainsize-fig.png')


#all_data = pd.read_csv("gs_data.csv", index_col='Date', header=4)
#all_data.info()
#all_data.to_json("results/data_output.json")

#json_data = pd.read_json("results/data_output.json")
#json_data.info()

#print(json_data.loc['195012':'197512','Value'])