import numpy as np
from src.orbit_propagation import propagate_orbit

def test_orbit_length():
    t = np.arange(0, 95, 1)
    x, y, z = propagate_orbit(t)
    assert len(x) == len(t)
    assert len(y) == len(t)
    assert len(z) == len(t)
