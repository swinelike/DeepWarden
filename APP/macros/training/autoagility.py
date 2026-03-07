import keyboard
import time
import threading
import pyautogui

class AutoAgilityListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None

    def stack(self, keybind):
        # Define the keybind
        KEYBIND = keybind
        
        # Explicitly set running to False when stack() is called

        def continuous_task():
            keyboard.press_and_release('w')
            while self.running:
                pyautogui.click()
                time.sleep(0.05)
                # Press and hold w at the start
                keyboard.press('w')
                # Your sequence of q presses with checks
                for _ in range(11):  # For the 11 'q' presses in your original code
                    if not self.running:
                        keyboard.release('w')
                        return
                    keyboard.press_and_release('q')
                    time.sleep(2.5)
                
                # Release w at the end of the sequence
                keyboard.release('w')
                if not self.running:
                    break
                time.sleep(1)


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
