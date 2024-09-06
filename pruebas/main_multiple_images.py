import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import sys
np.set_printoptions(threshold=sys.maxsize)

# List of haystack images
haystack_images = ['capturas/captura_ventana_1.png', 'capturas/captura_ventana_2.png', 'capturas/captura_ventana_3.png', 'capturas/captura_ventana_4.png', 'capturas/captura_ventana_5.png']

# Load the needle image
needle_img = cv.imread('capturas/captura_ventana_prueba.png', cv.IMREAD_UNCHANGED)

# Threshold for template matching
threshold = 0.5

# Iterate over each haystack image
for haystack_image in haystack_images:
    haystack_img = cv.imread(haystack_image, cv.IMREAD_UNCHANGED)
    
    # Perform template matching
    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
    
    # Find locations where the match exceeds the threshold
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    
    if locations:
        print(f'Found needle in {haystack_image}.')
        
        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]
        line_color = (0, 255, 0)
        line_type = cv.LINE_4
        
        for loc in locations:
            top_left = loc
            bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
            
            cv.rectangle(haystack_img, top_left, bottom_right, color=line_color, thickness=2, lineType=line_type)
        
        cv.imshow(f'Matches in {haystack_image}', haystack_img)
        cv.waitKey()
    else:
        print(f'Needle not found in {haystack_image}.')

cv.destroyAllWindows()