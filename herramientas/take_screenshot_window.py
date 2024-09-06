import pygetwindow as gw
from PIL import ImageGrab
import time

time.sleep(1)
def capture_window(window_title):
    # Encuentra la ventana por su título
    window = gw.getWindowsWithTitle(window_title)
    if window:
        # Obtén las coordenadas de la ventana
        win = window[0]
        left, top, right, bottom = win.left, win.top, win.right, win.bottom
        
        # Captura la región específica de la ventana
        img = ImageGrab.grab(bbox=(left, top, right, bottom))
        return img
    else:
        print(f"No se encontró ninguna ventana con el título: {window_title}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    # Título de la ventana que deseas capturar
    titulo_ventana = "BlueStacks App Player"
    
    # Captura la ventana
    captura = capture_window(titulo_ventana)
    
    # Guarda la captura si se realizó correctamente
    if captura:
        captura.save("captura_ventana.png")
