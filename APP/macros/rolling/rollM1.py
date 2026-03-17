import win32api
import win32con
import keyboard
import time


class rollM1Listener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None
    
    def stack(self, keybind):
        def is_mouse_swapped():

            return win32api.GetSystemMetrics(23) != 0

        def rollM1(self):
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            time.sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            time.sleep(0.01)
            keyboard.press_and_release('q')


        self.hotkey = keyboard.on_press_key(keybind, rollM1)


        

    def run(self, keybind):
        
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.stack(keybind=keybind)  # Just call stack directly
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging
                

    def stop(self):
        
        self.running = False
        if self.hotkey is not None:
            keyboard.unhook(self.hotkey) 
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)  # Wait up to 1 second for the thread to stop
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")