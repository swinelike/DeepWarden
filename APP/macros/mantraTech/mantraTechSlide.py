import keyboard
import time

class MantraSlideTechListener:  
    def __init__(self):
        print('activated')
        self.running = False
        self.thread = None
        self.hotkey = None
        self.wPressed = None
        self.wReleased = None

    def stack(self, keybinds):
        allKeys = str(keybinds).split(',')
        allKeys = ''.join(allKeys)
        self.isRunning = False
        self.lastPress = 0
        def wPressed(event):
            print('pressed')
            self.isPressed = True
            if time.time() - self.lastPress <= 0.5:
                self.isRunning = True
            self.lastPress = time.time()

        def wReleased(event):
            print('released')
            self.isPressed = False
            

        def on_key(event):
            if event.name in allKeys:
                print(self.isPressed)
                if self.isRunning:
                    keyboard.press_and_release('ctrl')  
        # Register the key press handler
        self.wPressed = keyboard.on_press_key('w', wPressed)
        self.wReleased = keyboard.on_release_key('w', wReleased)
        self.hotkey = keyboard.on_press(on_key)



    def run(self,keybinds):
        print('checking')
        
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.stack(keybinds=keybinds)  # Just call stack directly
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging

    def stop(self):
        
        self.running = False
        keyboard.unhook(self.hotkey)  # Remove all hotkeys when stopping
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")
