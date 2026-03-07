import win32api
import win32con
import keyboard
import time
import threading

class rollCancelListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None

    def stack(self):
        def is_mouse_swapped():
            return win32api.GetSystemMetrics(23) != 0
        def rollcancel(*_): #ignores all arguments passed to it 
                time.sleep(0.05)
                if is_mouse_swapped():
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                        time.sleep(0.05)
                        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                else:
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                        time.sleep(0.05)
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
        self.hotkey = keyboard.on_press_key('q', rollcancel)
        

    def run(self):
            
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
        controller = rollCancelListener()
        controller.run()  # Changed from start() to run()
        
        try:
            # Keep the main thread alive
            while controller.running:  # Changed from self.running to controller.running
                keyboard.wait(1)
        except KeyboardInterrupt:
            controller.stop()

if __name__ == "__main__":
    auto_feint = rollCancelListener()
    auto_feint.main()