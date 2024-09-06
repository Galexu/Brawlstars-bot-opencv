import json
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
time.sleep(1)
print("start")
def load_and_play_key_log(file_path):
    with open(file_path, "r") as file:
        key_log = json.load(file)

    def play_key_event(event):
        key = event["key"]
        if event["is_special"]:
            key = getattr(Key, key.split(".")[1])

        if event["type"] == "press":
            keyboard.press(key)
        elif event["type"] == "release":
            keyboard.release(key)

    print("Playing back the key log...")
    for event in key_log:
        play_key_event(event)
        time.sleep(0.1)

    print("Key log playback finished")
    
load_and_play_key_log("./capturas/passaje_oscuro/move_2.json")