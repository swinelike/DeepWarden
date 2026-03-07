import keyboard
import time
import win32api
import win32con
import pydirectinput
class AutoEatListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None

    def stack(self, keybind, foodname, boxcoordinates, foodcoordinates):

        boxcoordinates_x = int(boxcoordinates[0])
        boxcoordinates_y = int(boxcoordinates[1])

        foodcoordinates_x = int(foodcoordinates[0])
        foodcoordinates_y = int(foodcoordinates[1])

        def is_mouse_swapped():
            return win32api.GetSystemMetrics(23) != 0
        
        def on_key(event):
            if event.name in keybind:
                pydirectinput.keyDown('tab')
                #time.sleep(0.01)
                pydirectinput.keyUp('tab')
                pydirectinput.moveTo(boxcoordinates_x, boxcoordinates_y)
                pydirectinput.move(None,5)
                #time.sleep(0.01)
                pydirectinput.move(None,-5)
                
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                #time.sleep(0.01)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

                keyboard.write(foodname, delay=0)
                #time.sleep(0.01)
                pydirectinput.moveTo(foodcoordinates_x, foodcoordinates_y)
                pydirectinput.move(None, 5)
                #time.sleep(0.01)
                pydirectinput.move(None, -5)
                
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                #time.sleep(0.01)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

                screen_width = win32api.GetSystemMetrics(0)
                screen_height = win32api.GetSystemMetrics(1)
                pydirectinput.moveTo(screen_width // 2, screen_height // 2)
                #time.sleep(0.01)
                pydirectinput.move(None, 5)
                pydirectinput.move(None, -5)
                #time.sleep(0.01)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                #time.sleep(0.01)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)






                


        # Register the key press handler
        self.hotkey = keyboard.on_press(on_key)

    def run(self,keybind, foodname, boxcoordinates, foodcoordinates):
        print('checking')
        boxcoordinates = boxcoordinates.split(' ')
        foodcoordinates = foodcoordinates.split(' ')
        
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.stack(keybind=keybind, foodname=foodname, boxcoordinates=boxcoordinates, foodcoordinates=foodcoordinates)  # Just call stack directly
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging

    def stop(self):
        
        self.running = False
        keyboard.unhook(self.hotkey)  # Remove all hotkeys when stopping
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")
