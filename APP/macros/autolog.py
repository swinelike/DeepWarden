import keyboard
import time
import win32api
import win32con
import pydirectinput
class AutoLogListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None

    def stack(self, keybind, x_coordinate,y_coordinate):
        def is_mouse_swapped():
            return win32api.GetSystemMetrics(23) != 0
        
        def on_key(event):
            if event.name in keybind:
                pydirectinput.moveTo(x_coordinate, y_coordinate)
                pydirectinput.move(None,5)
                pydirectinput.move(None,-5)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                pydirectinput.keyDown('shift')
                pydirectinput.keyUp('shift')
                pydirectinput.moveTo(x_coordinate, y_coordinate)
                pydirectinput.move(None,5)
                pydirectinput.move(None,-5)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


                


        # Register the key press handler
        self.hotkey = keyboard.on_press(on_key)

    def run(self,keybind, coordinates):
        print('checking')
        coordinates = coordinates.split(' ')
        x_coordinate = int(coordinates[0])
        y_coordinate = int(coordinates[1])
        
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.stack(keybind=keybind, x_coordinate=x_coordinate, y_coordinate=y_coordinate)  # Just call stack directly
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging

    def stop(self):
        
        self.running = False
        keyboard.unhook(self.hotkey)  # Remove all hotkeys when stopping
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")
