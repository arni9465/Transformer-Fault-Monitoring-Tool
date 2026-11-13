# Transformer Fault Monitoring Tool

## Overview
A Python-based application designed to monitor transformer operating parameters and identify abnormal conditions using configurable threshold-based fault detection.

The application accepts voltage, current and temperature readings, evaluates the operating condition, generates alerts and stores monitoring records for future reference.

## Features
- Transformer voltage monitoring
- Current and load percentage calculation
- Temperature monitoring
- Threshold-based fault detection
- Normal, Warning and Critical status classification
- Automatic monitoring history storage
- CSV-based data logging
- View previously recorded readings

## Parameters Monitored

| Parameter | Unit |
|---|---|
| Voltage | Volts (V) |
| Current | Amperes (A) |
| Temperature | °C |
| Load | Percentage (%) |

## Technologies Used
- Python 3
- CSV
- File Handling
- Conditional Logic
- Date and Time Handling

## Project Structure

- `transformer_monitor.py` – Main monitoring application.
- `transformer_data.csv` – Sample monitoring records generated during testing.

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   `python transformer_monitor.py`

5. Enter transformer readings when prompted.
6. View monitoring history through the application menu.

## Testing
The application was tested using sample normal, warning and critical operating conditions.

## Important Note
This is a software-based prototype using manually entered or simulated readings. It is not connected to a physical transformer and is not intended to replace industrial protection equipment.

## Project Status
Under Development – Core monitoring and CSV data logging implemented. Dashboard and graphical analysis are planned.
