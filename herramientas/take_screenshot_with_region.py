import pyautogui
import time
import os

# Set the directory to the script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Function to take a screenshot and save it
def take_screenshot(region=None):
    # Get the current time to use as the filename
    filename = 'screenshot_region.png'
    filepath = os.path.join(os.getcwd(), filename)

    # Take a screenshot
    screenshot = pyautogui.screenshot(region=region)

    # Save the screenshot
    screenshot.save(filepath)
    print(f'Screenshot saved: {filepath}')

# Example region (x, y, width, height)
# region = (1350, 825, 400, 150)
# region = (900, 875, 125, 75)
# region = (1425, 860, 290, 100)
region = (1455, 850, 290, 100)


# Main loop to take screenshots every 2 seconds
try:
    while True:
        take_screenshot(region=region)
        time.sleep(3)
except KeyboardInterrupt:
    print('Screenshot capture stopped.')
