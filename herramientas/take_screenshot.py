import pyautogui
import time
import os
from datetime import datetime

# Set the directory to the script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Function to take a screenshot and save it
def take_screenshot():
    # Get the current time to use as the filename
    # timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    # filename = f'screenshot_{timestamp}.png'
    filename = 'screenshot.png'
    filepath = os.path.join(os.getcwd(), filename)
    
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    
    # Save the screenshot
    screenshot.save(filepath)
    print(f'Screenshot saved: {filepath}')

# Main loop to take screenshots every 2 seconds
try:
    while True:
        take_screenshot()
        time.sleep(3)
except KeyboardInterrupt:
    print('Screenshot capture stopped.')