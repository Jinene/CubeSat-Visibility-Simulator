import numpy as np
import pandas as pd
from src.orbit_propagation import propagate_orbit
from src.coordinate_transform import ground_station_vector
from src.visibility_analysis import elevation_angle, detect_passes
from src.visualization import plot_elevation
from src.ai_predictor import predict_next_pass

# Simulation parameters
t_total = 24*60
time = np.arange(0, t_total, 1)

# Satellite orbit
sat_x, sat_y, sat_z = propagate_orbit(time)

# Ground station
gs_pos = ground_station_vector(lat=36.8065, lon=10.1815)

# Elevation angle for each time step
elevations = np.array([elevation_angle(np.array([sat_x[i],sat_y[i],sat_z[i]]), gs_pos) for i in range(len(time))])

# Detect passes
start_idx, end_idx = detect_passes(elevations)

# Save results
results = []
for i in range(len(start_idx)):
    s = time[start_idx[i]]
    e = time[end_idx[i]]
    duration = e - s
    max_el = np.max(elevations[start_idx[i]:end_idx[i]+1])
    results.append([i+1, s, e, duration, max_el])
df = pd.DataFrame(results, columns=['Pass','Start','End','Duration','MaxElevation'])
df.to_csv('results/passes.csv', index=False)

# Plot elevation
plot_elevation(time, elevations)

# Optional AI prediction
next_pass = predict_next_pass('results/passes.csv')
print(f"Predicted next pass start (hybrid AI): {next_pass:.2f} min")
