# CubeSat-Visibility-Simulator

Python-based simulator to predict CubeSat visibility from ground stations using a **hybrid approach**: precise orbital math + optional AI predictions.

## Features
- Multi-pass simulation (24h)
- Elevation angle calculation & visibility detection
- Ground track and elevation plots
- Communication window reports (CSV)
- Optional AI module to optimize pass prediction
- Modular, professional Python tool

## Installation
```bash
git clone https://github.com/<username>/CubeSat-Visibility-Simulator.git
cd CubeSat-Visibility-Simulator
pip install -r requirements.txt
Usage
python src/main.py --tle data/tle/sample_satellite.tle --station "Tunis"
Mathematical Core

Elevation angle equation:

Elevation
=
arcsin
⁡
(
𝑟
⃗
𝑠
𝑎
𝑡
⋅
𝑟
⃗
𝑔
𝑠
∣
𝑟
⃗
𝑠
𝑎
𝑡
∣
 
∣
𝑟
⃗
𝑔
𝑠
∣
)
Elevation=arcsin(
∣
r
sat
	​

∣∣
r
gs
	​

∣
r
sat
	​

⋅
r
gs
	​

	​

)
AI Prediction (Optional)

Hybrid system: math calculates exact orbit, AI predicts best communication windows from past patterns.

Results

CSV of pass start/end times

Plots of elevation vs. time

Ground track map

Future Improvements

Real-time dashboard

Multi-satellite tracking

Telemetry & antenna pointing
