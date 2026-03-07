import keyboard
import time
import win32api
import win32con
import pydirectinput
class AutoSellListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None

    def stack(self, keybind, repetitions, itemcoordinates, confirmationcoordinates):
        itemcoordinates_x = int(itemcoordinates[0])
        itemcoordinates_y = int(itemcoordinates[1])

        confirmationcoordinates_x = int(confirmationcoordinates[0])
        confirmationcoordinates_y = int(confirmationcoordinates[1])

        def is_mouse_swapped():
            return win32api.GetSystemMetrics(23) != 0
        
        def on_key(event):
            if event.name in keybind:
                for i in range(repetitions):
                    pydirectinput.moveTo(itemcoordinates_x, itemcoordinates_y)
                    time.sleep(0.01)
                    pydirectinput.move(None, 5)
                    time.sleep(0.01)
                    pydirectinput.move(None, -5)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  
                    time.sleep(0.01) 
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                    time.sleep(0.01)
                    pydirectinput.moveTo(confirmationcoordinates_x, confirmationcoordinates_y)
                    time.sleep(0.01)
                    pydirectinput.move(None, 5)
                    time.sleep(0.01)
                    pydirectinput.move(None, -5)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                    time.sleep(0.01)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                    time.sleep(0.15)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                    time.sleep(0.01)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                    time.sleep(0.15)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                    time.sleep(0.01)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                    time.sleep(0.25)
        # Register the key press handler
        self.hotkey = keyboard.on_press(on_key)

    def run(self, keybind, repetitions, itemcoordinates, confirmationcoordinates):
        confirmationcoordinates = confirmationcoordinates.split(' ')
        itemcoordinates = itemcoordinates.split(' ')
        print('checking')

        repetitions = int(repetitions)
        
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.stack(keybind=keybind, repetitions=repetitions, itemcoordinates=itemcoordinates, confirmationcoordinates=confirmationcoordinates)  # Just call stack directly
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging

    def stop(self):
        
        self.running = False
        keyboard.unhook(self.hotkey)  # Remove all hotkeys when stopping
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")
