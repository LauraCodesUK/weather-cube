# main.py — auto Wi-Fi connect, then do nothing (for now)
import secrets, wifi_connect, time

try:
    wifi_connect.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
except Exception as e:
    print("Wi-Fi error:", e)

# Idle loop (we'll add display/weather next)
while True:
    time.sleep(1)
