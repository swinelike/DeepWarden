import keyboard
import time
import threading

class rollCritListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None

    def stack(self):
        def roll(self):
            keyboard.press_and_release('r')
            time.sleep(0.01)
            keyboard.press_and_release('q')

        self.hotkey = keyboard.on_press_key('r', roll, suppress=True)
        

    def run(self):
            
            if not self.thread or not self.thread.is_alive():
                print('starting ' + (__file__).split("\\")[-1])
                self.running = True
                self.thread = threading.Thread(target=self.stack)
                self.thread.daemon = True
                self.thread.start()
            while self.running:
                time.sleep(0.1)
                

    def stop(self):
        
        self.running = False
        if self.hotkey is not None:
            keyboard.unhook(self.hotkey)
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)  # Wait up to 1 second for the thread to stop
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")