🛰 CubeSat Ground Station Visibility Simulator – Python Orbital Tracker

Simulate and visualize CubeSat visibility from ground stations with pass predictions, elevation/azimuth profiles, and Doppler calculations.
Ideal for aerospace engineers, satellite operators, and space enthusiasts .

🗂 Repository Structure
Folder/File	Description
simulator/	Core Python package containing all simulation modules
simulator/__init__.py	Package initialization
simulator/tle_fetcher.py	Fetch and parse TLE (Two-Line Element) satellite data
simulator/ground_station.py	Define ground station locations and parameters
simulator/visibility.py	Compute satellite passes and visibility windows
simulator/doppler.py	Doppler shift calculation for communication planning
simulator/plotting.py	Static and interactive plotting functions
simulator/utils.py	Helper functions for conversions and calculations
notebooks/	Jupyter notebooks for interactive demos
notebooks/demo.ipynb	Example simulation and visualization
requirements.txt	List of required Python libraries
README.md	Project documentation
LICENSE	MIT License
📊 Example Output – Satellite Pass Table
Start Time	End Time	Max Elevation	Azimuth Start	Azimuth End	Doppler Shift (Hz)
2026-03-24 06:15	2026-03-24 06:20	65°	120°	210°	1450
2026-03-24 07:50	2026-03-24 07:55	42°	95°	170°	900
2026-03-24 09:20	2026-03-24 09:25	30°	60°	135°	500
