from pynput import keyboard, mouse
import time
from threading import Thread, Event
class AirListener:
    def __init__(self):
        self.spacebar_pressed = Event()
        self.click_detected = False
        self.last_click_time = 0
        self.debounce_interval = 0.1
        self.running = True
        self.keyboard_controller = keyboard.Controller()
        self.mouse_listener = None
        self.keyboard_listener = None

    def on_click(self, x, y, button, pressed):
        try:
            current_time = time.time()
            if pressed and button.name == "left":
                if current_time - self.last_click_time > self.debounce_interval:
                    print(f"Primary mouse button pressed at ({x}, {y})")
                    self.click_detected = True
                    self.last_click_time = current_time
            elif not pressed and button.name == "left":
                print(f"Primary mouse button released at ({x}, {y})")
            else:
                print(f"Ignoring {button.name} button event")
        except Exception as e:
            print(f"Error in on_click: {e}")

    def wait_for_click(self):
        self.click_detected = False
        start_time = time.time()
        while time.time() - start_time < 0.5:
            if self.click_detected:
                time.sleep(0.07)
                self.keyboard_controller.press('q')
                self.keyboard_controller.release('q')
                self.click_detected = False
                break
            time.sleep(0.01)
        self.spacebar_pressed.clear()

    def on_press(self, key):
        try:
            if key == keyboard.Key.space:
                self.spacebar_pressed.set()
                Thread(target=self.wait_for_click).start()
        except AttributeError:
            pass

    def run(self):
        self.mouse_listener = mouse.Listener(on_click=self.on_click)
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press)
        
        self.mouse_listener.start()
        self.keyboard_listener.start()
        

    def stop(self):
        self.running = False
        if self.mouse_listener:
            self.mouse_listener.stop()
        if self.keyboard_listener:
            self.keyboard_listener.stop()