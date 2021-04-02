#!/bin/python

# Import the libraries we are using. It is good practice to import all necessary
# libraries in the first lines of a file.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os as os
import sys as sys

# Create a function to read the data file
def read_data(filename,delimiter=',',starting_row=0):
    """This function reads data from a specified filename. 
    The specified filename should point to a .csv file."""
    # Create an array (a multi-dimensional table) out of our data file, full of text
    all_data = np.genfromtxt(filename, delimiter=delimiter,skip_header=0)

    # Select the data range we are interested in, convert it into a new array, full of numbers
    grainsize_data = np.array(all_data[1:,:], dtype=float)
    return grainsize_data

def process_data(grainsize_data):
    # Compute a new column by multiplying column number 1 to Kelvin
    grainsize_calculated = (grainsize_data[:,0,None] - 5) * 2

    # Append this new column to the existing temperature_data array
    processed_grainsize_data = np.append(grainsize_data, grainsize_calculated,1)
    return processed_grainsize_data

def plot_data(processed_grainsize_data, plot_filename):
    # Create a figure of the processed data
    grainsize_figure = plt.figure()
    grainsize_plot = plt.plot (processed_grainsize_data[:,2],processed_grainsize_data[:,1])

    plt.xlabel("Diameter(microns)")
    plt.ylabel("Concentration")
    plt.title("Grain Size Data")

    plt.show(block=True)
    grainsize_figure.savefig(plot_filename)

def convert_data(filename, output_filename):
    all_data = pd.read_csv(filename, header=0)
    all_data.info()
    all_data.to_json(output_filename)
    json_data = pd.read_json(output_filename)
    json_data.info()

def plot():
    input_file = "gs_data.csv"
    plot_file = "grainsize-fig.png"
    json_output_file = "data_output2.json"

    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"data"))
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"results"))
    
    input_filename = os.path.join(data_directory, input_file)
    plot_filename = os.path.join(results_directory, plot_file)
    json_output_file = os.path.join(results_directory, json_output_file)

    grainsize_data = read_data(input_filename, starting_row=0)
    processed_grainsize_data = process_data(grainsize_data)
    plot_data(processed_grainsize_data, plot_filename)
    convert_data(input_filename, json_output_file)

if __name__ == "__main__":
    print(sys.argv)
    plot()