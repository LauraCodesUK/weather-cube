# weather-cube
A tiny Python project to fetch and visualise live weather data from an API - the first step in my data-driven hardware experiments

## Overview
Weather Cube is a learning project exploring how to: 
- Pull live weather data using public APIs (e.g. OpenWeatherMap)
- Parse JSON responses and clean data
- Experiment with simple animations or LED displays
- Optionally serve results with FastAPI

This repo documents my experiments and what I learn along the way. 

## Goals 
- Fetch current weather data via API
- Parse and display temperature + conditions
- Experiment with simple visualisation or animation
- Explore FastAPI for serving data locally

## Hardware Requirements
- **Microcontroller:** ESP32 (Wi-Fi) or Raspberry Pi Pico W  
- **Display:** small OLED (SSD1306 128×64) / LED strip (WS2812B) / simple LEDs  
- **Power:** USB 5 V supply or battery pack  
- **Cable:** USB-C or Micro-USB **data** cable (not charge-only)  
- **Optional:** breadboard, jumper wires, resistor, and cube-style enclosure  

## ⚙️ Architecture
The Weather Cube operates in two coordinated layers:

| Layer | Purpose | Example Libraries |
|--------|----------|------------------|
| **Host Layer** | Fetches live API data, caches it locally or in the cloud, and exposes a simple `/weather.json` endpoint. | `requests`, `FastAPI`, `uvicorn`, `pandas`, `matplotlib` |

| **Device Layer** | Runs on a microcontroller using MicroPython; periodically retrieves the cached JSON and updates LEDs / display accordingly. | `urequests`, `machine`, `time` |

This separation keeps the device lightweight and allows the system to run even if the public API is temporarily unavailable.

## Tech Stack 
**Host (desktop/raspberry Pi):** 
Python • requests • FastAPI • matplotlib • uvicorn

**Device (on microcontroller):**
MicroPython (ESP32/Pico W) • urequests • machine • time

## Requirements

**Host (pip)**
requests
fastapi
uvicorn
pandas
matplotlib

**Device (MicroPython environment)**
No pip installs — upload the following to your board:
- `main.py`
- Any display drivers in `/lib` (e.g. `ssd1306.py`)

## Device Environment
- **Firmware:** MicroPython v1.22 or newer  
- **Upload tools:** Thonny / mpremote / rshell  
- **Network:** 2.4 GHz Wi-Fi configured in code  
- **Modules used:** `urequests`, `machine`, `time`  
- **Deployment:** Copy `device/main.py` to board → reset to run  



## Configuration
Create a `.env` file in the `host/` folder (not committed to GitHub) with:
```bash
OWM_API_KEY=your_api_key_here
CITY=Birmingham,GB
```

## Project Structure 
weather-cube/
├─ host/
│  ├─ app.py              # Optional FastAPI cache server
│  ├─ scripts/            # Experiments, test scripts, data pulls
│  ├─ requirements.txt    # pip dependencies (host environment)
│  ├─ .env.example        # Example of environment variable format
│  └─ .gitignore          # Excludes .env, .venv, etc.
└─ device/
   ├─ main.py             # MicroPython logic (runs on ESP32 / Pico W)
   └─ lib/                # Hardware drivers (e.g. ssd1306.py for OLED)

## Run Instructions
*To be completed once initial host and device scripts are ready.*

Planned structure:
- Host: virtual environment, `pip install -r requirements.txt`, run `app.py`
- Device: upload `main.py` to board and auto-run on boot

## License
This project is licensed under the [MIT License](LICENSE).

## Learning Log
| Date | What I Did | What I Learned | Next Step |
|------|-------------|----------------|------------|
| 2025-10-27 | Created repo and README | Learned host/device split | 

*More to come as the project develops.*