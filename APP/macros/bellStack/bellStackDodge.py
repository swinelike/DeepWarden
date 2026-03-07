import keyboard
import time
import threading

class BellStackDodgeListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey=None

    def stack(self):
        def on_key(event):
            if event.name == 'c':
                time.sleep(0.05)
                keyboard.press_and_release('q')
        # Register the key press handler
        self.hotkey = keyboard.on_press(on_key)
        

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
        keyboard.unhook(self.hotkey)
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)  # Wait up to 1 second for the thread to stop
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")

    def main(self):
        controller = BellStackDodgeListener()
        controller.run()  # Changed from start() to run()
        
        try:
            # Keep the main thread alive
            while controller.running:  # Changed from self.running to controller.running
                keyboard.wait(1)
                print('loopin around')
        except KeyboardInterrupt:
            controller.stop()

if __name__ == "__main__":
    bell_stack = BellStackDodgeListener()
    bell_stack.main()
