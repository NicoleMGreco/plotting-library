"""This file contains tests for plotting libarary"""

import sys
import os
import numpy as np
import pandas as pd

sys.path.append(os.path.join(
    os.path.dirname(__file__),
    ".."))

from src import plotting2 as plotting

def test_read_data():
    """Test that data can be read"""
    input_file = "gs_data.csv"
    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    input_filename = os.path.join(data_directory,input_file)
    grainsize_data = plotting.read_data(input_filename, starting_row=1)

    assert(grainsize_data.shape == (81,2))
    assert(grainsize_data[0,0] == 0.976563)

def test_plot_data():
    """Test that converted data is plotted"""
    plot_file = "grainsize-fig.png"
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))
    plot_filename = os.path.join(results_directory,plot_file)

    input_data = np.array([[0,20,30],[1,200,310]])
    
    if os.path.exists(plot_filename):
        os.remove(plot_filename)
        
    plotting.plot_data(input_data, plot_filename)

    assert (os.path.exists(plot_filename))

def test_convert_data():
    """Test that data is converted"""
    input_file = "gs_data.csv"
    json_output_file = "data_output2.json"

    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","results"))

    input_filename = os.path.join(data_directory,input_file)
    json_filename = os.path.join(results_directory,json_output_file)

    plotting.convert_data(input_filename, json_filename)

    input_data = pd.read_csv(input_filename, index_col='Microns', header=0)
    output_data = pd.read_json(json_filename)

    assert input_data.info() is output_data.info()