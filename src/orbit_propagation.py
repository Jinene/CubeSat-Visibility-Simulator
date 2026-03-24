import numpy as np

def propagate_orbit(t, altitude=500, inclination=51.6, period=95, r_earth=6371, degrees=False):
    """
    Propagate a simplified circular orbit in Earth-centered coordinates.

    Parameters
    ----------
    t : array-like
        Time array in minutes.
    altitude : float, optional
        Orbit altitude above Earth's surface in km (default=500 km).
    inclination : float, optional
        Orbital inclination in degrees (default=51.6°).
    period : float, optional
        Orbital period in minutes (default=95 min).
    r_earth : float, optional
        Earth radius in km (default=6371 km).
    degrees : bool, optional
        If True, returns positions in degrees instead of km (default=False).

    Returns
    -------
    x, y, z : np.ndarray
        Satellite positions in Earth-centered coordinates (km or degrees).
    """
    altitude = float(altitude)
    inclination = float(inclination)
    period = float(period)
    
    # Angular velocity in rad/min
    omega = 2 * np.pi / period
    theta = np.mod(omega * np.array(t), 2*np.pi)
    
    cos_i = np.cos(np.radians(inclination))
    sin_i = np.sin(np.radians(inclination))
    
    r = r_earth + altitude
    x = r * cos_i * np.cos(theta)
    y = r * cos_i * np.sin(theta)
    z = r * sin_i * np.ones_like(t)
    
    if degrees:
        # Convert km to degrees approx (latitude/longitude)
        x = np.degrees(x / r_earth)
        y = np.degrees(y / r_earth)
        z = np.degrees(z / r_earth)
    
    return x, y, z
