import sys, os
import numpy as np

sys.path.append(os.path.join(
        os.path.dirname(__file__),
        "../"))

import src.plotting as plotting

def test_read_data():
    input_file = "gs_data.csv"
    data_directory = os.path.realpath(os.path.join(os.path.dirname(__file__),"..","data"))
    input_filename = os.path.join(data_directory,input_file)
    grainsize_data = plotting.read_data(input_filename, starting_row=0)

    assert(grainsize_data.shape == (81,2))
    assert(grainsize_data[0,1] == 0.976563)
