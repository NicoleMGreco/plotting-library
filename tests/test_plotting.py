import plotting2 as plotting
import sys as sys
import os as os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_read_data(filename, delimiter=','):
    all_data = np.genfromtxt(filename, delimiter=delimiter,skip_header=0)

    grainsize_data = np.array(all_data[1:,:], dtype=float)
    return grainsize_data

    assert(grainsize_data.shape == (81,2))
    assert(grainsize_data[0,1] == 0.976563)


def test_process_data():
    input_data = np.array([[0,20],[1,200]])
    function_output = plotting.process_data(input_data)
    expected_output = np.array([[0,20,30],[1,200,310]])
    
    assert(np.all(function_output == expected_output))

def test_plot_data():
    plot_file = "grainsize-fig.png"
    results_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"results"))
    plot_filename = os.path.join(results_directory,plot_file)

    input_data = np.array([[0,20,30],[1,200,310]])
    if os.path.exists(plot_filename):
        os.remove(plot_filename)
        
    plotting.plot_data(input_data, plot_filename)

    assert (os.path.exists(plot_filename))

