import  keyboard
import time


class rollParryListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None

    def stack(self, keybind):


        def rollParry(self):
            keyboard.press_and_release('f')
            keyboard.press_and_release('q')
        if keybind != 'f':
            self.hotkey = keyboard.on_press_key(keybind, rollParry)
        else:
            self.hotkey = keyboard.on_press_key(keybind, rollParry, suppress=True)


        

    def run(self, keybind):
        
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.stack(keybind=keybind)  # Just call stack directly
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging
                

    def stop(self):
        
        self.running = False
        if self.hotkey is not None:
            keyboard.unhook(self.hotkey)
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)  # Wait up to 1 second for the thread to stop
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")

    def main(self):
        controller = rollParryListener()
        controller.run()  # Changed from start() to run()
        
        try:
            # Keep the main thread alive
            while controller.running:  # Changed from self.running to controller.running
                keyboard.wait(1)
        except KeyboardInterrupt:
            controller.stop()

if __name__ == "__main__":
    auto_feint = rollParryListener()
    auto_feint.main()