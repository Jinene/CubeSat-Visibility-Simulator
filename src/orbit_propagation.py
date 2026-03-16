
import numpy as np

def propagate_orbit(t, altitude=500, inclination=51.6, period=95):
    """
    Simplified circular orbit propagation
    :param t: time array in minutes
    :return: satellite positions x,y,z in km
    """
    earth_radius = 6371
    omega = 2*np.pi/period  # rad/min
    theta = np.mod(omega*t, 2*np.pi)
    
    x = (earth_radius + altitude) * np.cos(np.radians(inclination)) * np.cos(theta)
    y = (earth_radius + altitude) * np.cos(np.radians(inclination)) * np.sin(theta)
    z = (earth_radius + altitude) * np.sin(np.radians(inclination)) * np.ones_like(t)
    
    return x, y, z
