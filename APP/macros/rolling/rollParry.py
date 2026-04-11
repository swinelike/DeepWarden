import  keyboard
import time


class rollParryListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None
        self.onRelease = None

    def stack(self, keybind):
        self.alreadyPressed = False

        def rollParry(event):
            if not self.alreadyPressed:
                self.alreadyPressed = True
                keyboard.press_and_release('f')
                keyboard.press_and_release('q')

        def onReleaseKey(event):
            self.alreadyPressed = False
        
        self.hotkey = keyboard.on_press_key(keybind, rollParry)
        self.onRelease = keyboard.on_release_key(keybind, onReleaseKey)

        

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
            keyboard.unhook(self.onRelease)
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)  # Wait up to 1 second for the thread to stop
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")