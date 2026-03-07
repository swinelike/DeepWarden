from pynput import mouse
import time

def get_pos():
    completed = False
    x_pos = None
    y_pos = None
    def onClick(x, y, button, pressed):
        if pressed:
            nonlocal completed
            completed = True
            nonlocal x_pos, y_pos
            
            x_pos = x
            y_pos = y
            return completed, x_pos, y_pos
    listener = mouse.Listener(on_click=onClick)
    listener.start()
    while not completed:
        time.sleep(0.05)
    if completed:
        listener.stop()
        return x_pos, y_pos
