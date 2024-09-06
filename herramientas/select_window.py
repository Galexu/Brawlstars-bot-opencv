import pygetwindow as gw
import pyautogui
import time

def focus_window(window_title):
    # Encuentra la ventana por su título
    window = gw.getWindowsWithTitle(window_title)
    if window:
        # Trae la ventana al frente
        window[0].activate()
    else:
        print(f"No se encontró ninguna ventana con el título: {window_title}")

# Ejemplo de uso
if __name__ == "__main__":
    # Espera 5 segundos para darte tiempo de abrir la ventana correcta si es necesario
    time.sleep(1)

    # Título de la ventana que deseas enfocar (puedes cambiarlo según sea necesario)
    titulo_ventana = "BlueStacks App Player"

    # Enfoca la ventana
    focus_window(titulo_ventana)

    # Opcional: realiza alguna acción en la ventana enfocada
    # pyautogui.write('Hola mundo!')
