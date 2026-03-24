
CubeSat Ground Station Visibility Simulator 

A Python-based simulator for predicting and visualizing CubeSat visibility from ground stations.
Designed for satellite operators, aerospace engineers, and space enthusiasts 🚀.

✨ Features
 TLE Parsing: Fetch & parse Two-Line Element data automatically.
 Orbital Propagation: Accurate satellite positions using SGP4/SDP4.
 Visibility Prediction: Determine CubeSat visibility with elevation constraints.
 Visualization: Interactive plots of passes over maps and azimuth-elevation profiles.
 Doppler Shift Calculation: Estimate shifts for communications.
 Multi-Ground Station Support: Simulate passes from multiple stations.
 Export Options: Save predictions as CSV or JSON for further analysis.
 Technologies Used
Python 3.11+
Libraries:
numpy, pandas – data & numerical processing
sgp4, skyfield – orbital & astronomical calculations
matplotlib, plotly – visualization
geopy – geodetic calculations
requests – TLE fetching
Jupyter Notebook for interactive simulations
GitHub Actions for automated testing & linting (optional)
⚡ Installation
# Clone the repository
git clone https://github.com/<your-username>/CubeSat-Visibility-Simulator.git
cd CubeSat-Visibility-Simulator

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
passes = compute_passes(tle_data, gs, start_time='2026-03-24T00:00:00', end_time='2026-03-25T00:00:00', min_elevation=10)
print(passes)
4️⃣ Visualize Satellite Pass
from simulator.plotting import plot_pass
plot_pass(passes)
5️⃣ Export Predictions
passes.to_csv("cube_sat_passes.csv")
📂 Project Structure
CubeSat-Visibility-Simulator/
│
├── simulator/
│   ├── __init__.py
│   ├── tle_fetcher.py          # Fetch and parse TLE data
│   ├── ground_station.py       # Ground station class
│   ├── visibility.py           # Compute satellite passes
│   ├── doppler.py              # Doppler shift calculations
│   ├── plotting.py             # Visualization functions
│   └── utils.py                # Helper functions
│
├── notebooks/
│   └── demo.ipynb              # Interactive Jupyter demo
│
├── requirements.txt
├── README.md
└── LICENSE
📊 Example Output

Pass Table:

Start Time	End Time	Max Elevation	Azimuth Start	Azimuth End	Doppler Shift (Hz)
2026-03-24 06:15	2026-03-24 06:20	65°	120°	210°	1450

Visuals:

2D Map showing CubeSat trajectory
Elevation vs Time Plot
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
