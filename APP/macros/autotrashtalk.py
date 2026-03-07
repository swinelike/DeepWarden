import keyboard
import time
from random import randint

class TrashTalkListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None

    def stack(self, keybind, txtpath):
        def on_key(event):
            if event.name in keybind:
                with open(txtpath) as f:
                    trashtalks = f.read().split('\n')
                chosenMessage = trashtalks[randint(0, len(trashtalks)-1)]
                
                time.sleep(0.05)
                keyboard.press_and_release('/')
                time.sleep(0.05)
                keyboard.write(chosenMessage)
                time.sleep(0.05)
                keyboard.press_and_release('enter')  
        # Register the key press handler
        self.hotkey = keyboard.on_press(on_key)

    def run(self,keybind, txtpath):
        print('checking')
        
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.stack(keybind=keybind, txtpath=txtpath)  # Just call stack directly
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging

    def stop(self):
        
        self.running = False
        keyboard.unhook(self.hotkey)  # Remove all hotkeys when stopping
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")
