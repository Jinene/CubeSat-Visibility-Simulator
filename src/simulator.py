"""
CubeSat Ground Station Visibility Simulator
---------------------------------------------
Professional Python module for CubeSat pass prediction, orbit propagation,
ground station visibility, and visualization using real TLE data and Skyfield.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skyfield.api import EarthSatellite, load, wgs84
import matplotlib.dates as mdates

# -------------------------
# Ground Station Definition
# -------------------------
class GroundStation:
    def __init__(self, name, latitude, longitude, altitude=0):
        self.name = name
        self.lat = latitude
        self.lon = longitude
        self.alt = altitude

# -------------------------
# Satellite Definition
# -------------------------
class Satellite:
    def __init__(self, name, tle_line1, tle_line2):
        self.name = name
        self.satellite = EarthSatellite(tle_line1, tle_line2, name, load.timescale())
    
    def propagate(self, times):
        """
        Propagate satellite orbit to given times
        :param times: Skyfield Timescale object array
        :return: geocentric positions
        """
        return self.satellite.at(times)
    
    def eci_to_ecef(self, geocentric):
        """
        Convert geocentric positions to latitude, longitude, elevation
        :param geocentric: Skyfield position object
        :return: latitudes (deg), longitudes (deg), elevations (km)
        """
        lat, lon = wgs84.latlon_of(geocentric)
        alt = geocentric.distance().km - 6371  # approximate altitude above Earth's surface
        return lat.degrees, lon.degrees, alt

# -------------------------
# Visibility Computation
# -------------------------
def compute_elevation(geocentric, ground_station):
    """
    Compute satellite elevation relative to a ground station
    :param geocentric: Skyfield position object
    :param ground_station: GroundStation object
    :return: elevation array in degrees
    """
    gs = wgs84.latlon(ground_station.lat, ground_station.lon, ground_station.alt)
    difference = geocentric - gs
    topocentric = difference.at(load.timescale().now())
    alt, az, distance = topocentric.altaz()
    return alt.degrees

def filter_visible(elevations, min_elevation=10):
    """
    Returns boolean mask for elevations above threshold
    """
    return np.array(elevations) >= min_elevation

def predict_passes(satellite, ground_station, times, min_elevation=10):
    """
    Generate pass predictions (start, end, max elevation) for a 24h window
    """
    geocentric = satellite.propagate(times)
    lats, lons, alts = satellite.eci_to_ecef(geocentric)
    elevations = compute_elevation(geocentric, ground_station)
    visible_mask = filter_visible(elevations, min_elevation)
    
    # Identify pass intervals
    passes = []
    start_idx = None
    for i, visible in enumerate(visible_mask):
        if visible and start_idx is None:
            start_idx = i
        if (not visible or i == len(visible_mask)-1) and start_idx is not None:
            end_idx = i
            max_elev = np.max(elevations[start_idx:end_idx+1])
            passes.append({
                'start_time': times[start_idx].utc_datetime(),
                'end_time': times[end_idx].utc_datetime(),
                'max_elevation': max_elev
            })
            start_idx = None
    return pd.DataFrame(passes)

# -------------------------
# Plotting Utilities
# -------------------------
def plot_elevation(times, elevations, min_angle=10, sat_name="CubeSat"):
    """
    Professional elevation vs time plot
    """
    fig, ax = plt.subplots(figsize=(14,6))
    ax.plot(times, elevations, color='#1f77b4', linewidth=2.5, label='Elevation Angle')
    ax.axhline(min_angle, color='#d62728', linestyle='--', linewidth=1.8, label=f'Min Elevation ({min_angle}°)')

    elevations = np.array(elevations)
    times = np.array(times)
    above = elevations >= min_angle
    start_idx = None
    for i in range(len(above)):
        if above[i] and start_idx is None:
            start_idx = i
        if (not above[i] or i == len(above)-1) and start_idx is not None:
            end_idx = i
            ax.fill_between(times[start_idx:end_idx+1], elevations[start_idx:end_idx+1], min_angle, color='green', alpha=0.2)
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

def plot_ground_track(lats, lons, sat_name="CubeSat"):
    """
    Plot satellite ground track in 2D
    """
    plt.figure(figsize=(12,6))
    plt.plot(lons, lats, 'b-', linewidth=2, label=f'{sat_name} Ground Track')
    plt.xlabel("Longitude (°)")
    plt.ylabel("Latitude (°)")
    plt.title(f"{sat_name} Ground Track Over Earth", fontsize=16, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.show()

def plot_3d_orbit(x, y, z, sat_name="CubeSat"):
    """
    3D orbit visualization
    """
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label=sat_name, linewidth=2)
    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    ax.set_title(f"{sat_name} 3D Orbit", fontsize=16, fontweight='bold')
    ax.legend()
    plt.show()
