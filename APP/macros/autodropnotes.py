import keyboard
import time
import win32api
import win32con
import pydirectinput
class AutoDropNotesListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None

    def stack(self, keybind, repetitions, notecoordinates, startcoordinates, endcoordinates, confirmationcoordinates):
        notecoordinates_x = int(notecoordinates[0])
        notecoordinates_y = int(notecoordinates[1])

        startcoordinates_x = int(startcoordinates[0])
        startcoordinates_y = int(startcoordinates[1])

        endcoordinates_x = int(endcoordinates[0])
        endcoordinates_y = int(endcoordinates[1])

        confirmationcoordinates_x = int(confirmationcoordinates[0])
        confirmationcoordinates_y = int(confirmationcoordinates[1])

        def is_mouse_swapped():
            return win32api.GetSystemMetrics(23) != 0
        
        def on_key(event):
            if event.name in keybind:
                for i in range(repetitions):
                    pydirectinput.moveTo(notecoordinates_x, notecoordinates_y)
                    time.sleep(0.01)
                    pydirectinput.move(None, 5)
                    time.sleep(0.01)
                    pydirectinput.move(None, -5)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  
                    time.sleep(0.01) 
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                    time.sleep(0.01)
                    pydirectinput.moveTo(startcoordinates_x, startcoordinates_y)
                    time.sleep(0.01)
                    pydirectinput.move(None, 5)
                    time.sleep(0.01)
                    pydirectinput.move(None, -5)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                    time.sleep(0.01)
                    pydirectinput.moveTo(endcoordinates_x, endcoordinates_y)
                    pydirectinput.move(None, 5)
                    pydirectinput.move(None, -5)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                    time.sleep(0.1)
                    pydirectinput.moveTo(confirmationcoordinates_x, confirmationcoordinates_y)
                    pydirectinput.move(None, 5)
                    pydirectinput.move(None, -5)
                    time.sleep(0.1)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  
                    time.sleep(0.01) 
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP if is_mouse_swapped() else win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)









                


        # Register the key press handler
        self.hotkey = keyboard.on_press(on_key)

    def run(self, keybind, repetitions, notecoordinates, startcoordinates, endcoordinates, confirmationcoordinates):
        print('checking')
        startcoordinates = startcoordinates.split(' ')
        endcoordinates = endcoordinates.split(' ')
        notecoordinates = notecoordinates.split(' ')
        confirmationcoordinates = confirmationcoordinates.split(' ')
        repetitions = int(repetitions)
        
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.stack(keybind=keybind, startcoordinates=startcoordinates, endcoordinates=endcoordinates, notecoordinates=notecoordinates, repetitions=repetitions, confirmationcoordinates=confirmationcoordinates)  # Just call stack directly
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging

    def stop(self):
        
        self.running = False
        keyboard.unhook(self.hotkey)  # Remove all hotkeys when stopping
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")
