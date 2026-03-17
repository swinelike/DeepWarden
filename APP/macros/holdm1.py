import win32api
import win32con
import time
import threading
from keyboard import press_and_release

class M1Listener:
    def __init__(self):
        self.running = True
        self.thread = None

    def is_mouse_swapped(self):
        return win32api.GetSystemMetrics(23) != 0

    def get_primary_button(self):
        if self.is_mouse_swapped():
            return "right"
        return "left"

    def press_button(self, keyToPress):
        press_and_release(keyToPress)

    def check_button_state(self, vk_code):
        state = win32api.GetAsyncKeyState(vk_code)
        return (state & 0x8000) != 0

    def macro_thread(self, keyToPress):
        hold_start = 0
        is_auto_clicking = False
        
        while self.running:
            try:
                # Check both buttons
                left_pressed = self.check_button_state(win32con.VK_LBUTTON)
                right_pressed = self.check_button_state(win32con.VK_RBUTTON)
                
                # Determine if the primary button is pressed
                primary_pressed = right_pressed if self.is_mouse_swapped() else left_pressed
                
                # Button just pressed
                if primary_pressed and hold_start == 0:
                    hold_start = time.time()
                
                # Button being held
                elif primary_pressed and hold_start > 0:
                    hold_duration = time.time() - hold_start
                    
                    # Check for auto-click threshold
                    if hold_duration >= 0.2:
                        if not is_auto_clicking:
                            is_auto_clicking = True
                        self.press_button(keyToPress)
                        time.sleep(0.04)
                
                # Button released
                elif not primary_pressed and hold_start > 0:
                    hold_start = 0
                    is_auto_clicking = False
                
                time.sleep(0.001)  # Prevent CPU overload
                
            except KeyboardInterrupt:
                print("\nStopping...")
                break

    def run(self, keyToPress):
        print('checking')
        if len(keyToPress) != 1:
            keyToPress = '`'
        
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.thread = threading.Thread(target=self.macro_thread, args=keyToPress)
            self.thread.daemon = True
            self.thread.start()

    def stop(self):
        
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)  # Wait up to 1 second for the thread to stop
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")