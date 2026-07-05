#!/usr/bin/env python3
import time
import os
from datetime import datetime
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306

def get_pi_temp():
    """Reads the native system core temperature of the Raspberry Pi."""
    try:
        # Executes the official system diagnostic call
        temp_data = os.popen("vcgencmd measure_temp").readline()
        # Clean string from 'temp=43.2'C\n' to just '43.2'
        return temp_data.replace("temp=", "").replace("'C\n", "").strip()
    except Exception:
        return "0.0"

def main():
    # Initialize I2C connection channel 1 at address 0x3C
    serial_bus = i2c(port=1, address=0x3C)
    device = ssd1306(serial_bus, width=128, height=64)

    print("🚀 Dynamic Loop Started. Press Ctrl+C to terminate.")

    try:
        while True:
            # 1. Fetch current live telemetry states
            current_time = datetime.now().strftime("%H:%M:%S")
            pi_temperature = get_pi_temp()

            # 2. Open canvas context to push fresh frame state
            with canvas(device) as draw:
                # Decorative top tracking header
                draw.text((5, 2), "--- PI MONITOR ---", fill="white")
                
                # Render Time Metric
                draw.text((5, 18), f"TIME: {current_time}", fill="white")
                
                # Render Temperature Metric
                draw.text((5, 32), f"TEMP: {pi_temperature}°C", fill="white")
                
                # 3. Draw an ASCII/Unicode Smiling Face text asset on the right
                draw.text((95, 24), "( ^_^ )", fill="white")
                
                # Subtext status anchor
                draw.text((5, 50), "Status: ACTIVE", fill="white")

            # 4. Wait exactly 1 second before re-polling system files
            time.sleep(1)

    except KeyboardInterrupt:
        # Gracefully handle Ctrl+C breakdown loops
        print("\n🛑 Shutting down interface matrix...")
        with canvas(device) as draw:
            draw.text((5, 25), "Display Sleeping...", fill="white")
        time.sleep(1)

if __name__ == "__main__":
    main()