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
- **Firmware:** MicroPython v1.26.1 (See [Firmware Installation](#firmware-installation) for setup steps.)
- **Upload tools:** Thonny (recommended for beginners) / mpremote / rshell / VS Code with PyMakr or similar

## Current Architecture

The current recommended setup uses a direct device-to-API architecture:

```text
ESP32-S3 Device → Open-Meteo API
```

The ESP32 connects directly to Wi-Fi, requests weather data from a public weather API, and displays the result locally on the screen.

This keeps the project lightweight and beginner-friendly while I experiment with MicroPython, APIs, and hardware displays.

---

## Optional / Future Architecture

A future optional architecture may introduce a lightweight host layer:

```text
ESP32-S3 Device → Local FastAPI Host → Weather API
```

This could later support:

- local caching
- reduced API calls
- multi-device support
- dashboards and analytics
- offline-friendly behaviour

The host-side architecture is currently experimental and not required for the default build.

## Tech Stack

### Device (Current Primary Architecture)
- MicroPython (ESP32-S3 / Pico W)
- `urequests`
- `machine`
- `time`
- ST7789 / SSD1306 display drivers (planned)

### Optional Host Layer (Experimental / Future)
- Python
- requests
- FastAPI
- uvicorn
- pandas
- matplotlib

## Requirements

### Device Requirements (Current Build)

MicroPython environment running on ESP32-S3 or Pico W.

Modules are uploaded directly to the board rather than installed with pip.

Files currently used:

- `main.py`
- `wifi_connect.py`
- `secrets.py`
- display drivers in `/lib` (planned)

---

### Optional Host Requirements (Experimental)

If using the optional FastAPI host layer:

```bash
pip install -r host/requirements.txt
```

Host dependencies currently include:

- requests
- fastapi
- uvicorn
- pandas
- matplotlib

## Device Environment
- **Firmware:** MicroPython v1.22 or newer  
- **Upload tools:** Thonny / mpremote / rshell  
- **Network:** 2.4 GHz Wi-Fi configured in code  
- **Modules used:** `urequests`, `machine`, `time`  
- **Deployment:** Copy `device/main.py` to board → reset to run  

## Firmware Installation

This project was flashed with **MicroPython v1.26.1 (ESP32_GENERIC_S3)** using **Thonny IDE**.

### Quick Steps
1. Open *Thonny → Tools → Options → Interpreter*  
2. Select **MicroPython (ESP32)** → click **Install or update MicroPython**  
3. Choose **ESP32-S3** and select the downloaded `.bin` file  
4. Wait for confirmation, then connect to the board and verify with:
   ```python
   print("Hello Cube!")
   ```

## External Libraries / References

This project uses or experiments with the following open-source resources:

- ST7789 MicroPython display driver:
  https://github.com/russhughes/st7789py_mpy

Additional references and experiments will be added as the project develops.

## Environment & Secrets Configuration
This project uses local environment files to store credentials and location data.
Sensitive information such as Wi-Fi passwords or API keys should never be committed to GitHub.

### Host Environment (.env)
The host environment (used for API requests, optional FastAPI, etc.) uses a .env file.
An example file is provided at:
```bash
host/.env.example
```

To use it:
```bash
# Copy the example file
cp host/.env.example host/.env
```

Then edit host/.env to include:
- Your Wi-Fi credentials (if needed)
- Your latitude and longitude
- Your Weather service API key (if applicable)

The .env file is **ignored by Git**  (see .gitignore) for safety.

### Device Secrets (secrets.py)

The ESP32 device uses its own secrets file for Wi-Fi setup.
An example file is provided at:
```bash
device/secrets.example.py
```

To use it:
```bash
# Copy the example file
cp device/secrets.example.py device/secrets.py
```

Then edit device/secrets.py to include your:

Wi-Fi SSID and password

(Optional) API key or other constants

**Never commit your real secrets.py** — it’s listed in .gitignore to protect your credentials.

## Project Structure 
```plaintext
weather-cube/
├─ host/
│  ├─ app.py              # Optional FastAPI cache server
│  ├─ scripts/            # Experiments, test scripts, data pulls
│  ├─ requirements.txt    # pip dependencies (host environment)
│  ├─ .env.example        # Example of environment variable format
│  └─ .gitignore          # Excludes .env, .venv, etc.
└─ device/
   ├─ main.py             # MicroPython logic (runs on ESP32 / Pico W)
   ├─ secrets.example     # Example of secrets variables to allow microcontroller to access WiFi/direct API
   └─ lib/                # Hardware drivers (e.g. ssd1306.py for OLED)
```

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
| 2025-10-27 | Created venv and config.py | Learned how to set up virtual environments and contextualised within the project | Write and test API weather code|
| 2025-10-27 | Created secrets file for microcontroller | Learned how to add specific files to .gitignore, and what a microcontroller needs to connect to WiFi | Write and test API weather code|
| 2025-10-28 | Reviewed and updated project architecture structure, pivoting from a two-layer host/device approach to a simpler direct device-to-API architecture for the initial build. Updated README and `host/app.py` to reflect the revised structure and future optional host-layer plans. | Learned the importance of simplifying project scope early in development, separating “current implementation” from “future architecture,” and keeping documentation aligned with the actual working state of the project. | Verify board functionality and begin testing display control to ensure the ESP32-S3 can render custom output to the screen. |

*More to come as the project develops.*
