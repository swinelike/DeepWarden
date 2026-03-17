import keyboard
import time
import threading

class flashMapListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.pressed = False
        self.activated = False
        self.hotkey = None
        

    def stack(self):
        
        def on_press(event):
            if not self.pressed and not self.activated:
                self.pressed = True
                self.activated = True
        
        def on_release(event):
            if self.pressed and self.activated:
                print("closing map")
                time.sleep(0.2)
                keyboard.press_and_release('m')
                self.pressed = False
                self.activated = False
        
        # Register callbacks for key press and release
        self.hotkey= (
        keyboard.on_press_key('m', on_press),
        keyboard.on_release_key('m', on_release)
        )
        
        # Keep the thread alive
        while self.running:
            time.sleep(0.1)

    def run(self):
        print('checking')
        
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.thread = threading.Thread(target=self.stack)
            self.thread.daemon = True
            self.thread.start()
            

    def stop(self):
        
        self.running = False
        # Unhook all keyboard hooks
        if self.hotkey:
            # Unhook each hook individually
            for hook in self.hotkey:
                try:
                    keyboard.unhook(hook)
                except Exception as e:
                    print(f"Error unhooking: {e}")
        
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)  # Wait up to 1 second for the thread to stop
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")

