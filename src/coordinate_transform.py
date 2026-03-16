import numpy as np

def ground_station_vector(lat, lon, earth_radius=6371):
    """
    Convert ground station coordinates to ECEF vector
    """
    x = earth_radius * np.cos(np.radians(lat)) * np.cos(np.radians(lon))
    y = earth_radius * np.cos(np.radians(lat)) * np.sin(np.radians(lon))
    z = earth_radius * np.sin(np.radians(lat))
    return np.array([x, y, z])
