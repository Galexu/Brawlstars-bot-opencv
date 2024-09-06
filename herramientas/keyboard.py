import pyautogui
import time

# Function to press and hold a key
def press_and_hold(key, hold_time):
    pyautogui.keyDown(key)
    time.sleep(hold_time)
    pyautogui.keyUp(key)

# Function to press a key multiple times
def press_multiple_times(key, times, interval=0.1):
    for _ in range(times):
        pyautogui.press(key)
        time.sleep(interval)

# Example usage
if __name__ == "__main__":
    # Wait for 5 seconds to give you time to switch to the desired window
    time.sleep(1)

    # Press and hold the 'a' key for 2 seconds
    press_and_hold('a', 5)

    # Press the 'b' key 10 times with a 0.1-second interval
    press_multiple_times('d', 10, 0.1)
