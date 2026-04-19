import keyboard
import time
import win32api
import win32con


class DynamicUppercutListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.is_player_running = False
        self.last_press_time = 0
        self.last_release_time = 0
        self.w_held = False
        self.hooks = []

    def check_running_state(self, event):
        if event.name != 'w':
            return
        
        current_time = time.time()
        
        if event.event_type == 'down':
            if self.last_press_time == 0:  # First press
                self.last_press_time = current_time
            else:  # Second press
                if (current_time - self.last_press_time) < 0.6 and self.last_release_time > self.last_press_time:
                    self.is_player_running = True
                self.last_press_time = current_time
            self.w_held = True
            
        elif event.event_type == 'up':
            self.w_held = False
            self.last_release_time = current_time
            if self.is_player_running:
                self.is_player_running = False
                self.last_press_time = 0  

    def on_key(self, event):
        if event.name == 'w':
            self.check_running_state(event)
        elif event.name == 'ctrl':
            if not self.is_player_running:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0,0,0,0)  
                time.sleep(0.01)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0,0,0,0)  
                if self.toRoll:
                    time.sleep(0.03)
                    keyboard.press_and_release('q')




    def stack(self, toRoll):
        self.toRoll = toRoll
        self.remove_hooks()
        
        try:
            self.hooks.append(keyboard.on_press_key('w', self.on_key))
            self.hooks.append(keyboard.on_release_key('w', self.on_key))
            self.hooks.append(keyboard.on_press_key('ctrl', self.on_key))
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
        self.running = False
        self.is_player_running = False
        self.w_held = False
        self.last_press_time = 0
        self.last_release_time = 0
        self.remove_hooks()
        
        if self.thread and self.thread.is_alive():
            try:
                self.thread.join(timeout=1.0)
                if self.thread.is_alive():
                    print("Warning: Thread did not stop cleanly")
            except Exception as e:
                print(f"Error stopping thread: {e}")