import numpy as np
from src.visibility_analysis import elevation_angle, detect_passes

def test_elevation_angle():
    sat_pos = np.array([6871,0,0])
    gs_pos = np.array([6371,0,0])
    angle = elevation_angle(sat_pos, gs_pos)
    assert angle > 0

def test_detect_passes():
    elevations = np.array([0,5,15,20,5,0])
    start_idx, end_idx = detect_passes(elevations, min_angle=10)
    assert len(start_idx) == 1
    assert len(end_idx) == 1
