# wifi_connect.py — MicroPython Wi-Fi helper for ESP32/ESP32-S3
import network, time

def connect(ssid: str, password: str, timeout_s: int = 25):
    """Connect to Wi-Fi in STA mode, return the active WLAN object."""
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active():
        wlan.active(True)

    if not wlan.isconnected():
        wlan.connect(ssid, password)
        t0 = time.ticks_ms()
        while not wlan.isconnected():
            if time.ticks_diff(time.ticks_ms(), t0) > timeout_s * 1000:
                raise RuntimeError("Wi-Fi connect timeout")
            time.sleep(0.2)

    ip = wlan.ifconfig()[0]
    print("✅ Wi-Fi connected →", ip)
    return wlan

