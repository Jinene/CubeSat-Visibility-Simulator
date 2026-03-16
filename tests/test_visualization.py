import numpy as np
from src.visualization import plot_elevation

def test_plot():
    time = np.arange(0,10,1)
    elevations = np.random.rand(10)*90
    plot_elevation(time, elevations)
