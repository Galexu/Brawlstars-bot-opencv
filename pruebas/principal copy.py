import pygetwindow as gw
import pyautogui
import time
from PIL import ImageGrab
import cv2 as cv
import numpy as np
import os
import sys
import replay_keyboard as rk

choose_map = "mapa1"

path_image_1 = "capturas/" + choose_map + "captura_ventana_1.png"
path_image_2 = "capturas/" + choose_map + "captura_ventana_2.png"
path_image_3 = "capturas/" + choose_map + "captura_ventana_3.png"
path_image_4 = "capturas/" + choose_map + "captura_ventana_4.png"
path_image_5 = "capturas/" + choose_map + "captura_ventana_5.png"
path_image_6 = "capturas/" + choose_map + "captura_ventana_6.png"
path_image_7 = "capturas/" + choose_map + "captura_ventana_7.png"
path_image_8 = "capturas/" + choose_map + "captura_ventana_7.png"
path_image_9 = "capturas/" + choose_map + "captura_ventana_8.png"
path_image_10 = "capturas/" + choose_map + "captura_ventana_10.png"

path_movement_1 = "capturas/" + choose_map + "move_1.json"
path_movement_2 = "capturas/" + choose_map + "move_2.json"
path_movement_3 = "capturas/" + choose_map + "move_3.json"
path_movement_4 = "capturas/" + choose_map + "move_4.json"
path_movement_5 = "capturas/" + choose_map + "move_5.json"
path_movement_6 = "capturas/" + choose_map + "move_6.json"
path_movement_7 = "capturas/" + choose_map + "move_7.json"
path_movement_8 = "capturas/" + choose_map + "move_8.json"
path_movement_9 = "capturas/" + choose_map + "move_9.json"
path_movement_10 = "capturas/" + choose_map + "move_10.json"

haystack_images = [
    path_image_1,
    path_image_2,
    path_image_3,
    path_image_4,
    path_image_5,
    path_image_6,
    path_image_7,
    path_image_8,
    path_image_9,
    path_image_10,
]

haystack_images_play = ["capturas/play.png"]

haystack_images_replay = ["capturas/exit.png", "capturas/play_again.png"]

os.chdir(os.path.dirname(os.path.abspath(__file__)))
np.set_printoptions(threshold=sys.maxsize)

threshold = 0.5

def focus_window(window_title):
    window = gw.getWindowsWithTitle(window_title)

    if window:
        window[0].activate()
        print("Ventana enfocada.")
    else:
        print(f"No se encontró ninguna ventana con el título: {window_title}")


def capture_window(window_title):
    window = gw.getWindowsWithTitle(window_title)

    if window:
        win = window[0]
        left, top, right, bottom = win.left, win.top, win.right, win.bottom

        img = ImageGrab.grab(bbox=(left, top, right, bottom))
        return img
    else:
        print(f"No se encontró ninguna ventana con el título: {window_title}")
        return None


if __name__ == "__main__":
    time.sleep(1)
    titulo_ventana = "BlueStacks App Player"

    focus_window(titulo_ventana)
    time.sleep(1)

loop_play = True
loop_replay = False
loop_game = False

try:
    while loop_play:
        captura = capture_window(titulo_ventana)

        if captura:
            captura.save("capturas/captura_ventana.png")
            print("Captura guardada.")

            for index, haystack_image in enumerate(haystack_images_play):
                haystack_img = cv.imread(haystack_image, cv.IMREAD_UNCHANGED)

                needle_img = cv.imread(
                    "capturas/captura_ventana.png", cv.IMREAD_UNCHANGED
                )
                result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
                locations = np.where(result >= threshold)
                locations = list(zip(*locations[::-1]))

                if locations:
                    loop_play = False
                    loop_game = True
                    print(f"Found needle in {haystack_image} in loop {index}.")
                    if index == 0:
                        print("play f")
                        pyautogui.press("f")
                else:
                    print(f"Needle not found in {haystack_image}.")
            cv.destroyAllWindows()
except KeyboardInterrupt:
    print("Screenshot capture stopped.")

try:
    while loop_game:
        captura = capture_window(titulo_ventana)

        if captura:
            captura.save("capturas/captura_ventana.png")
            print("Captura guardada.")

            for index, haystack_image in enumerate(haystack_images):
                haystack_img = cv.imread(haystack_image, cv.IMREAD_UNCHANGED)

                needle_img = cv.imread(
                    "capturas/captura_ventana.png", cv.IMREAD_UNCHANGED
                )
                result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
                locations = np.where(result >= threshold)
                locations = list(zip(*locations[::-1]))

                if locations:
                    loop_game = False
                    loop_replay = True
                    print(f"Found needle in {haystack_image} in loop {index}.")
                    if index == 0:
                        print("firts spawn")
                        rk.load_and_play_key_log(path_movement_1)
                    elif index == 1:
                        print("second spawn")
                        rk.load_and_play_key_log(path_movement_3)
                    elif index == 2:
                        print("third spawn")
                        rk.load_and_play_key_log(path_movement_3)
                    elif index == 3:
                        print("fourth spawn")
                        rk.load_and_play_key_log(path_movement_4)
                    elif index == 4:
                        print("fifth spawn")
                        rk.load_and_play_key_log(path_movement_5)
                    elif index == 5:
                        print("sixth spawn")
                        rk.load_and_play_key_log(path_movement_6)
                    elif index == 6:
                        print("seventh spawn")
                        rk.load_and_play_key_log(path_movement_7)
                    elif index == 7:
                        print("eighth spawn")
                        rk.load_and_play_key_log(path_movement_8)
                    elif index == 8:
                        print("nineth spawn")
                        rk.load_and_play_key_log(path_movement_9)
                    elif index == 9:
                        print("tenth spawn")
                        rk.load_and_play_key_log(path_movement_10)
                else:
                    print(f"Needle not found in {haystack_image}.")
            cv.destroyAllWindows()
except KeyboardInterrupt:
    print("Screenshot capture stopped.")

try:
    while loop_replay:
        captura = capture_window(titulo_ventana)

        if captura:
            captura.save("capturas/captura_ventana.png")
            print("Captura guardada.")

            for index, haystack_image in enumerate(haystack_images_replay):
                haystack_img = cv.imread(haystack_image, cv.IMREAD_UNCHANGED)

                needle_img = cv.imread(
                    "capturas/captura_ventana.png", cv.IMREAD_UNCHANGED
                )
                result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
                locations = np.where(result >= threshold)
                locations = list(zip(*locations[::-1]))

                if locations:
                    print(f"Found needle in {haystack_image} in loop {index}.")
                    if index == 0:
                        print("exit g")
                        pyautogui.press("g")
                    elif index == 1:
                        loop_replay = False
                        loop_play = True
                        print("play again e")
                        pyautogui.press("e")
                else:
                    print(f"Needle not found in {haystack_image}.")
            cv.destroyAllWindows()
except KeyboardInterrupt:
    print("Screenshot capture stopped.")
