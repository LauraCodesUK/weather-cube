from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access the environment variables
WIFI_SSID = os.getenv("WIFI_SSID")
WIFI_PASSWORD = os.getenv("WIFI_PASSWORD")
LATITUDE = os.getenv("LATITUDE")
LONGITUDE = os.getenv("LONGITUDE")
WEATHER_API_KEY = os.getenv("ACCUWEATHER_API_KEY")

# Print to check they’re loading correctly
if __name__ == "__main__":
    print("Wi-Fi SSID:", WIFI_SSID)
    print("Latitude:", LATITUDE)
    print("Longitude:", LONGITUDE)
