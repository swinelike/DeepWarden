import keyboard
import time
import win32api
import win32con
import pydirectinput
class AutoBankListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None

    def stack(self, keybind, itemname, boxcoordinates, itemcoordinates, vowcoordinates, repetitions):

        boxcoordinates_x = int(boxcoordinates[0])
        boxcoordinates_y = int(boxcoordinates[1])

        itemcoordinates_x = int(itemcoordinates[0])
        itemcoordinates_y = int(itemcoordinates[1])

        if len(vowcoordinates) > 2:
            vowcoordinates = vowcoordinates.split(' ')
        else:
            vowcoordinates = [-1, -1]
        vowcoordinates_x = int(vowcoordinates[0])
        vowcoordinates_y = int(vowcoordinates[1])

        def is_mouse_swapped():
            return win32api.GetSystemMetrics(23) != 0
        
        def on_key(event):
            if event.name in keybind:
                pydirectinput.moveTo(boxcoordinates_x, boxcoordinates_y)
                pydirectinput.move(None,5)
                time.sleep(0.01)
                pydirectinput.move(None,-5)
                for i in range(int(repetitions)):
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                    time.sleep(0.01)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

                    keyboard.write(itemname, delay=0)
                    time.sleep(0.01)
                    pydirectinput.moveTo(itemcoordinates_x, itemcoordinates_y)
                    pydirectinput.move(None, 5)
                    time.sleep(0.01)
                    pydirectinput.move(None, -5)
                    
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                    time.sleep(0.01)

                    screen_width = win32api.GetSystemMetrics(0)
                    screen_height = win32api.GetSystemMetrics(1)
                    pydirectinput.moveTo(screen_width // 2, screen_height // 2)
                    time.sleep(0.01)
                    pydirectinput.move(None, 5)
                    pydirectinput.move(None, -5)
                    time.sleep(0.01)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

                    if vowcoordinates_x > -1 and vowcoordinates_y > -1:
                        time.sleep(0.5)
                        pydirectinput.moveTo(vowcoordinates_x, vowcoordinates_y)
                        pydirectinput.move(None, 5)
                        #time.sleep(0.01)
                        pydirectinput.move(None, -5)

                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                        #time.sleep(0.01)
                        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                    time.sleep(2)






                


        # Register the key press handler
        self.hotkey = keyboard.on_press(on_key)

    def run(self,keybind, itemname, boxcoordinates, itemcoordinates, vowcoordinates, repetitions):
        print('checking')
        boxcoordinates = boxcoordinates.split(' ')
        itemcoordinates = itemcoordinates.split(' ')
        
        
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.stack(keybind=keybind, itemname=itemname, boxcoordinates=boxcoordinates, itemcoordinates=itemcoordinates, vowcoordinates=vowcoordinates, repetitions=repetitions)  # Just call stack directly
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging

    def stop(self):
        
        self.running = False
        keyboard.unhook(self.hotkey)  # Remove all hotkeys when stopping
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")
