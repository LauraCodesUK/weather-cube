## For use if using intermediary device 2-layer architecture where the ESP32 display pulls from desktop or Raspberry Pi
from fastapi import FastAPI
import requests
from config import LATITUDE, LONGITUDE

app = FastAPI()

@app.get("/current")
def current():
    url = ("https://api.open-meteo.com/v1/forecast"
           f"?latitude={LATITUDE}&longitude={LONGITUDE}"
           "&current=temperature_2m,weather_code")
    cur = requests.get(url, timeout=10).json()["current"]
    return {"temp_c": cur["temperature_2m"], "code": cur["weather_code"]}
