# CubeSat-Visibility-Simulator - System Description

## Overview
This tool predicts CubeSat visibility for a ground station using a hybrid approach:
- **Mathematical orbit propagation** (circular or SGP4)
- **Coordinate transformations** (ECI → ECEF → Lat/Lon/Alt)
- **Elevation angle computation**
- **Optional AI module** for hybrid pass prediction

## Architecture
- `orbit_propagation.py`: computes satellite positions
- `coordinate_transform.py`: ground station vectors
- `visibility_analysis.py`: elevation & pass detection
- `visualization.py`: plots elevation & ground tracks
- `ai_predictor.py`: optional ML regression model
- `main.py`: orchestrates simulation, plotting, CSV outputs

## Elevation Angle Formula
\[
\text{Elevation} = \arcsin\left(\frac{\vec{r}_{sat} \cdot \vec{r}_{gs}}{|\vec{r}_{sat}| \, |\vec{r}_{gs}|}\right)
\]

## AI Hybrid Prediction
- Uses past passes (CSV) to predict next pass start
- Simple linear regression
- Optional enhancement, does not replace math calculation
