import keyboard
import time
import pyautogui

class MotifSwapListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.thing = None
        

    def stack(self, keybind, motifnum, weaponnum):
        def on_key(event):
            if event.name in keybind:
                keyboard.press_and_release(str(motifnum))
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(0.1)
                keyboard.press_and_release(str(weaponnum))
        # Register the key press handler
        self.thing = keyboard.on_press(on_key)

    def run(self,keybind, motifnum, weaponnum):
        print('checking')
        
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.stack(keybind=keybind, motifnum=motifnum, weaponnum=weaponnum)  # Just call stack directly
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging

    def stop(self):
        
        self.running = False
        if self.thing:
            keyboard.unhook(self.thing)
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")
