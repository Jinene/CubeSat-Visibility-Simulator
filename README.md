# 🛰 CubeSat Ground Station Visibility Simulator – Python Orbital Tracker

![GitHub repo size](https://img.shields.io/github/repo-size/jinene/CubeSat-Visibility-Simulator?style=for-the-badge)
![Last commit](https://img.shields.io/github/last-commit/jinene/CubeSat-Visibility-Simulator?style=for-the-badge)
![Issues](https://img.shields.io/github/issues/jinene/CubeSat-Visibility-Simulator?style=for-the-badge)
![Forks](https://img.shields.io/github/forks/jinene/CubeSat-Visibility-Simulator?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)![Python version](https://img.shields.io/badge/python-3.11+-blue?style=for-the-badge)    

> **Simulate and visualize CubeSat visibility from ground stations with pass predictions, elevation/azimuth profiles, and Doppler calculations.**  
> Ideal for aerospace engineers, satellite operators, and space enthusiasts 🚀.

---

## ✨ Features
- 🛰 **TLE Parsing:** Fetch & parse Two-Line Element data automatically.  
- **Orbital Propagation:** Accurate satellite positions using SGP4/SDP4.  
- **Visibility Prediction:** Determine CubeSat visibility with elevation constraints.  
- **Visualization:** Interactive plots of passes over maps and azimuth-elevation profiles.  
- **Doppler Shift Calculation:** Estimate shifts for communications.  
- **Multi-Ground Station Support:** Simulate passes from multiple stations.  
- **Export Options:** Save predictions as CSV or JSON for further analysis.

---

## 🛠 Technologies Used
- **Python 3.11+**  
- **Libraries:** `numpy`, `pandas`, `sgp4`, `skyfield`, `matplotlib`, `plotly`, `geopy`, `requests`  
- **Jupyter Notebook** for interactive simulations  
- **GitHub Actions** for automated testing & linting (optional)

---

## ⚡ Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/CubeSat-Ground-Station-Visibility-Simulator.git
cd CubeSat-Ground-Station-Visibility-Simulator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
🚀 Usage
1️⃣ Fetch TLE Data
from simulator.tle_fetcher import fetch_tle
tle_data = fetch_tle("Cubesat Name or NORAD ID")
2️⃣ Configure Ground Station
from simulator.ground_station import GroundStation
gs = GroundStation(latitude=36.8, longitude=10.2, altitude=10)  # Example: Tunisia
3️⃣ Compute Visibility
from simulator.visibility import compute_passes
passes = compute_passes(
    tle_data, 
    gs, 
    start_time='2026-03-24T00:00:00', 
    end_time='2026-03-25T00:00:00', 
    min_elevation=10
)
print(passes)
4️⃣ Visualize Satellite Pass
from simulator.plotting import plot_pass
plot_pass(passes)
5️⃣ Export Predictions
passes.to_csv("cube_sat_passes.csv")
🗂 Repository Structure
Folder/File	Description
simulator/	Core Python package containing all simulation modules
simulator/__init__.py	Package initialization
simulator/tle_fetcher.py	Fetch and parse TLE satellite data
simulator/ground_station.py	Define ground station locations and parameters
simulator/visibility.py	Compute satellite passes and visibility windows
simulator/doppler.py	Doppler shift calculation for communication planning
simulator/plotting.py	Static and interactive plotting functions
simulator/utils.py	Helper functions for conversions and calculations
notebooks/	Jupyter notebooks for interactive demos
notebooks/demo.ipynb	Example simulation and visualization
requirements.txt	Python library dependencies
README.md	Project documentation
LICENSE	MIT License
📊 Example Output – Satellite Pass Table
Start Time	End Time	Max Elevation	Azimuth Start	Azimuth End	Doppler Shift (Hz)
2026-03-24 06:15	2026-03-24 06:20	65°	120°	210°	1450
2026-03-24 07:50	2026-03-24 07:55	42°	95°	170°	900
2026-03-24 09:20	2026-03-24 09:25	30°	60°	135°	500

Each row represents a single pass of the CubeSat over the ground station, including key metrics for planning communications.

🤝 Contribution

Contributions are welcome!

Fork the repo
Create a branch: git checkout -b feature/your-feature
Commit: git commit -m "Add new feature"
Push: git push origin feature/your-feature
Open a pull request
📚 References
CelesTrak TLE Data
SGP4 Python Library
Skyfield
 – Astronomical computations
⚖️ License

MIT License – see LICENSE file.
