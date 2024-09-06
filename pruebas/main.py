import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import sys
np.set_printoptions(threshold=sys.maxsize)

# Cargar las imágenes
haystack_img = cv.imread('captura_ventana_5.png', cv.IMREAD_UNCHANGED)
needle_img = cv.imread('captura_ventana_prueba.png', cv.IMREAD_UNCHANGED)

# conversion imagenes
# haystack_img_gray = cv.cvtColor(haystack_img, cv.COLOR_BGR2GRAY)
# needle_img_gray = cv.cvtColor(needle_img, cv.COLOR_BGR2GRAY)

# result = cv.matchTemplate(haystack_img_gray, needle_img_gray, cv.TM_CCOEFF_NORMED)
result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
# print(result)

threshold = 0.5
locations = np.where(result >= threshold)
locations = list(zip(*locations[::-1]))
# print(locations)

if locations:
    print('Found needle.')

    needle_w = needle_img.shape[1]
    needle_h = needle_img.shape[0]
    line_color = (0, 255, 0)
    line_type = cv.LINE_4

    for loc in locations:
        top_left = loc
        bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

        cv.rectangle(haystack_img, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
    
    cv.imshow('Matches', haystack_img)
    cv.waitKey()
else:
    print('Needle not found.')
    