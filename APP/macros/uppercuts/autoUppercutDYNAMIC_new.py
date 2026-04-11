import keyboard
import time
import win32api
import win32con


class DynamicUppercutListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.is_player_running = False

        self.w_held = False
        self.hooks = []







    def stack(self, toRoll):
        self.toRoll = toRoll # to roll or not to roll...
        self.remove_hooks()
        self.lastPress = -1

        def onPress(event):
            if time.time() - self.lastPress <= 0.65: 
                self.is_player_running = True 
            self.lastPress = time.time()

        def onRelease(event):
            self.is_player_running = False

        def on_key(self, event):
            if event.name == 'ctrl':
                if not self.is_player_running:
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0,0,0,0)  
                    time.sleep(0.01)
                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0,0,0,0)  
                    if self.toRoll:
                        time.sleep(0.03)
                        keyboard.press_and_release('q')     
        try:
            self.hooks.append(keyboard.on_press_key('w', onPress))
            self.hooks.append(keyboard.on_release_key('w', onRelease))
            self.hooks.append(keyboard.on_press_key('ctrl', on_key))
        except Exception as e:
            print(f"Error registering keyboard hooks: {e}")
            self.remove_hooks()

    def remove_hooks(self):
        for hook in self.hooks:
            try:
                keyboard.unhook(hook)
            except Exception as e:
                print(f"Warning: Failed to unhook keyboard listener: {e}")
        self.hooks.clear()

    def run(self, toRoll):
        print('checking')
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.stack(toRoll=toRoll)
            while self.running:
                time.sleep(0.1)

    def stop(self):
        self.remove_hooks()
        
        if self.thread and self.thread.is_alive():
            try:
                self.thread.join(timeout=1.0)
                if self.thread.is_alive():
                    print("Warning: Thread did not stop cleanly")
            except Exception as e:
                print(f"Error stopping thread: {e}")