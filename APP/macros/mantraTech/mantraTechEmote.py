import keyboard
import time
import threading

class MantraEmoteTechListener:  
    def __init__(self):
        self.running = False
        self.thread = None

    def stack(self, keybinds, content):
        allKeys = str(keybinds).split(',')
        allKeys = ''.join(allKeys)
        def on_key(event):
            if event.name in allKeys:
                time.sleep(0.05)
                keyboard.press_and_release('/')  
                time.sleep(0.02)
                keyboard.write('/e ' + content)
                time.sleep(0.05)
                keyboard.press_and_release('enter')    
        # Register the key press handler
        keyboard.on_press(on_key)

    def run(self,keybinds,content):
        print('checking')
        
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.stack(keybinds=keybinds, content=content)  # Just call stack directly
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging

    def stop(self):
        
        self.running = False
        keyboard.unhook_all()  # Remove all hotkeys when stopping
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")
