import keyboard
import time
import pyautogui
import threading

class UppercutListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.is_clicking = False
        self.click_thread = None
        self.hooks = []  # Store keyboard hooks

    def clicker(self):
        try:
            while self.is_clicking and self.running:
                pyautogui.click()
                time.sleep(0.01)  # Adjust this value to control click speed
        except Exception as e:
            print(f"Error in clicker thread: {e}")
            self.is_clicking = False

    def remove_hooks(self):
        # Safely remove hooks
        for hook in self.hooks:
            try:
                keyboard.unhook(hook)
            except Exception as e:
                print(f"Warning: Failed to unhook keyboard listener: {e}")
        self.hooks.clear()

    def stack(self):
        # First remove any existing hooks
        self.remove_hooks()

        def on_ctrl_press(event):
            try:
                if not self.is_clicking and self.running:
                    self.is_clicking = True
                    self.click_thread = threading.Thread(target=self.clicker)
                    self.click_thread.start()
            except Exception as e:
                print(f"Error in ctrl press handler: {e}")
                self.is_clicking = False
                
        def on_ctrl_release(event):
            try:
                self.is_clicking = False
                if self.click_thread and self.click_thread.is_alive():
                    self.click_thread.join(timeout=1.0)
                    if self.click_thread.is_alive():
                        print("Warning: Click thread did not stop cleanly")
            except Exception as e:
                print(f"Error in ctrl release handler: {e}")

        try:
            # Register new hooks and store them
            self.hooks.append(keyboard.on_press_key('ctrl', on_ctrl_press))
            self.hooks.append(keyboard.on_release_key('ctrl', on_ctrl_release))
        except Exception as e:
            print(f"Error registering keyboard hooks: {e}")
            self.remove_hooks()  # Clean up any hooks that were added

    def run(self):
        print('checking')
        try:
            if not self.thread or not self.thread.is_alive():
                print('starting ' + (__file__).split("\\")[-1])
                self.running = True
                self.stack()
                while self.running:
                    time.sleep(0.1)
        except Exception as e:
            print(f"Error in run method: {e}")
            self.stop()

    def stop(self):
        try:
            self.running = False
            self.is_clicking = False
            
            # Stop the click thread if it's running
            if self.click_thread and self.click_thread.is_alive():
                try:
                    self.click_thread.join(timeout=1.0)
                    if self.click_thread.is_alive():
                        print("Warning: Click thread did not stop cleanly")
                except Exception as e:
                    print(f"Error stopping click thread: {e}")

            # Remove keyboard hooks
            self.remove_hooks()

            # Stop the main thread
            if self.thread and self.thread.is_alive():
                try:
                    self.thread.join(timeout=1.0)
                    if self.thread.is_alive():
                        print("Warning: Main thread did not stop cleanly")
                except Exception as e:
                    print(f"Error stopping main thread: {e}")

        except Exception as e:
            print(f"Error in stop method: {e}")
