import win32api
import win32con
import keyboard

import time

class ankleCutterListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None

    def stack(self, keybind, flowstatekeybind):
        def is_mouse_swapped():
            return win32api.GetSystemMetrics(23) != 0
        def anklecutter(*_): #ignores all arguments passed to it 
            keyboard.press_and_release('w')
            time.sleep(0.05)
            keyboard.press('w')
            time.sleep(0.05)
            keyboard.press('ctrl')
            time.sleep(0.075)
            keyboard.press_and_release(flowstatekeybind)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            time.sleep(0.05)
            keyboard.release('ctrl')
            keyboard.release('w')
            time.sleep(0.025)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            time.sleep(0.25)
        self.hotkey = keyboard.on_press_key(keybind, anklecutter)
        

    def run(self, keybind, flowstatekeybind):
        
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.stack(keybind=keybind, flowstatekeybind=flowstatekeybind)
            while self.running:
                time.sleep(0.1)
                

    def stop(self):
        
        self.running = False
        keyboard.unhook(self.hotkey) 
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)  # Wait up to 1 second for the thread to stop
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")

    def main(self):
        controller = ankleCutterListener()
        controller.run()  # Changed from start() to run()
        
        try:
            # Keep the main thread alive
            while controller.running:  # Changed from self.running to controller.running
                keyboard.wait(1)
        except KeyboardInterrupt:
            controller.stop()

if __name__ == "__main__":
    auto_feint = ankleCutterListener()
    auto_feint.main()