import json
from pynput import keyboard
import time

# Initialize a list to store the keyboard inputs
key_log = []

time.sleep(1)
print("Recording the key log...")
# Function to handle key presses
def on_press(key):
    try:
        key_log.append({"type": "press", "key": key.char, "is_special": False})
    except AttributeError:
        key_log.append({"type": "press", "key": str(key), "is_special": True})


# Function to handle key releases
def on_release(key):
    try:
        key_log.append({"type": "release", "key": key.char, "is_special": False})
    except AttributeError:
        key_log.append({"type": "release", "key": str(key), "is_special": True})
    # Stop listener on 'esc' key
    if key == keyboard.Key.esc:
        return False


# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Save the key_log to a JSON file
with open("key_log.json", "w") as file:
    json.dump(key_log, file, indent=4)

print("Key log saved to key_log.json")
