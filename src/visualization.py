import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def plot_elevation(time, elevations, min_angle=10, sat_name="CubeSat", show_passes=True):
    """
    Professional satellite elevation plotting function.

    Parameters
    ----------
    time : array-like
        Array of datetime objects representing time points.
    elevations : array-like
        Corresponding elevation angles in degrees.
    min_angle : float, optional
        Minimum elevation for visibility (default=10°).
    sat_name : str, optional
        Satellite name for plot title (default="CubeSat").
    show_passes : bool, optional
        Highlight visible passes above min_angle (default=True).
    """
    fig, ax = plt.subplots(figsize=(14,6))
    
    ax.plot(time, elevations, color='#1f77b4', linewidth=2.5, label='Elevation Angle')
    ax.axhline(min_angle, color='#d62728', linestyle='--', linewidth=1.8, label=f'Min Elevation ({min_angle}°)')
    
    if show_passes:
        elevations = np.array(elevations)
        time = np.array(time)
        above = elevations >= min_angle
        start_idx = None
        for i in range(len(above)):
            if above[i] and start_idx is None:
                start_idx = i
            if (not above[i] or i == len(above)-1) and start_idx is not None:
                end_idx = i
                ax.fill_between(time[start_idx:end_idx+1], elevations[start_idx:end_idx+1],
                                min_angle, color='green', alpha=0.2)
                start_idx = None

    ax.set_title(f'{sat_name} Elevation vs Time', fontsize=18, fontweight='bold', pad=15)
    ax.set_xlabel('Time', fontsize=14)
    ax.set_ylabel('Elevation (°)', fontsize=14)
    ax.set_ylim(0, 90)
    ax.grid(True, which='both', linestyle='--', alpha=0.5)
    
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    
    ax.legend(fontsize=12, loc='upper right')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
