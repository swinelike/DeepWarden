import keyboard
import time
import threading
import pyautogui

class AutoFortitudeListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None

    def stack(self, keybind):
        # Define the keybind
        KEYBIND = keybind
        
        # Explicitly set running to False when stack() is called
        self.running = False  # Add this line

        def continuous_task():
            while self.running:
                pyautogui.click()
                time.sleep(25)
                if not self.running:
                    break
                keyboard.press_and_release('e')
                time.sleep(30)
                if not self.running:
                    break
                keyboard.press_and_release('e')
                time.sleep(0.5)

        def toggle_running_state(e):
            if e.name == KEYBIND:
                print(f"Current running state: {self.running}")
                if not self.running:
                    print("Starting...")
                    self.running = True
                    self.thread = threading.Thread(target=continuous_task, daemon=True)
                    self.thread.start()
                    print(f"Started running code on keypress: {KEYBIND}")
                else:
                    print("Stopping...")
                    self.running = False
                    print(f"Stopped running code on keypress: {KEYBIND}")

        self.hotkey = keyboard.on_press(toggle_running_state)

        try:
            keyboard.wait('esc')
        except KeyboardInterrupt:
            pass
        finally:
            self.running = False





    def run(self, keybind):
        print('checking')
        
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.stack(keybind=keybind)  # Just call stack directly
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging

    def stop(self):
        
        self.running = False
        keyboard.unhook(self.hotkey)  # Remove all hotkeys when stopping
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")
