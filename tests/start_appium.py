import subprocess
import time
import os

def start_appium_server():
    """Start the Appium server"""
    try:
        # Start Appium server
        appium_process = subprocess.Popen(
            ['appium', '--allow-insecure', 'chromedriver_autodownload'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(10)  # Wait for Appium server to start
        return appium_process
    except Exception as e:
        print(f"Error starting Appium server: {e}")
        raise

def start_emulator():
    """Start the Android emulator"""
    try:
        # Start emulator
        emulator_process = subprocess.Popen(
            ['emulator', '-avd', 'test_avd', '-no-audio', '-no-window'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(30)  # Wait for emulator to start
        return emulator_process
    except Exception as e:
        print(f"Error starting emulator: {e}")
        raise

if __name__ == "__main__":
    appium_process = start_appium_server()
    emulator_process = start_emulator()