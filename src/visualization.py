import matplotlib.pyplot as plt

def plot_elevation(time, elevations, min_angle=10):
    plt.figure(figsize=(12,5))
    plt.plot(time, elevations, 'b', linewidth=2)
    plt.axhline(min_angle, color='r', linestyle='--', linewidth=1.5)
    plt.xlabel('Time (min)')
    plt.ylabel('Elevation (deg)')
    plt.title('Satellite Elevation vs Time')
    plt.grid(True)
    plt.show()
