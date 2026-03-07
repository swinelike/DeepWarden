import keyboard
import time
import threading
import pyautogui


class autoCharismaListener:
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None
        self.hook_active = False

    def stack(self):
        replacements = {
            #! All lowercase
            "soh": "sohowswork",
            "wow": "wowthisbreezeisgreatright",
            "somew": "someweatherwerehavinghuh",
            "sow": "sowhatskeepingyoubusythesedays",
            "hey": "heyhivekincanibugyouforamoment",
            "mew": "mewowisthatthelatestfelinorfashion",
            "somet": "sometimesihavereallydeepthoughtsaboutlifeandstuff",
            "you": "youeverbeentoacanorrestaurantthefoodsprettyhowlright",
            #! Capital starting 
            "Soh": "sohowswork",
            "Wow": "wowthisbreezeisgreatright",
            "Somew": "someweatherwerehavinghuh",
            "Sow": "sowhatskeepingyoubusythesedays",
            "Hey": "heyhivekincanibugyouforamoment",
            "Mew": "mewowisthatthelatestfelinorfashion",
            "Somet": "sometimesihavereallydeepthoughtsaboutlifeandstuff",
            "You": "youeverbeentoacanorrestaurantthefoodsprettyhowlright",
        }

        # Variables to track user input and state
        current_input = ""
        last_replacement_time = 0
        replacement_cooldown = 1  # Prevent infinite replacements (in seconds)
        typing_in_progress = False  # Flag to indicate if the script is typing

        # List of common keys to block
        common_keys_to_block = [
            *list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"),  # Letters
            *list("0123456789"),  # Numbers
            "space", "enter", "backspace", "tab", "shift", "ctrl", "alt", "esc", "caps lock",
        ]

        def on_key_event(e):
            nonlocal current_input, last_replacement_time, typing_in_progress

            # If typing is in progress, block all key events
            if typing_in_progress:
                return

            # Only process key down events
            if e.event_type != "down":
                return

            # Ignore non-character keys like Shift, Ctrl, etc.
            if len(e.name) != 1 or not e.name.isprintable():
                return

            # Append the typed character to the current input
            current_input += e.name

            # Check if the current input matches any key in the replacements dictionary
            for key, value in replacements.items():
                if current_input.endswith(key):
                    # Ensure there is a cooldown between replacements
                    current_time = time.time()
                    if current_time - last_replacement_time < replacement_cooldown:
                        return

                    # Start typing the replacement
                    def perform_replacement(current_key=key, current_value=value):
                        nonlocal typing_in_progress, current_input, last_replacement_time
                        try:
                            typing_in_progress = True
                            blocked_keys = []  # List to store blocked keys

                            # Block common keys while typing
                            for key_name in common_keys_to_block:
                                try:
                                    keyboard.block_key(key_name)
                                    blocked_keys.append(key_name)
                                except Exception:
                                    pass  # Ignore invalid keys

                            # Perform the typing
                            print('TYPING THE LINE')
                            pyautogui.write(
                                current_value[len(current_key):], interval=0
                            )  # Type quickly
                            time.sleep(0.1)
                            keyboard.press_and_release("enter")  # Press Enter
                            time.sleep(0.25)
                            pyautogui.click()  # Click once
                        finally:
                            # Unblock all blocked keys after typing
                            for key_name in blocked_keys:
                                try:
                                    keyboard.unblock_key(key_name)
                                except Exception:
                                    pass  # Ignore errors during unblocking
                            typing_in_progress = False
                            current_input = ""  # Reset current input
                            last_replacement_time = time.time()

                    # Perform the replacement in a separate thread to avoid blocking the main loop
                    threading.Thread(target=perform_replacement).start()
                    break

        # Start listening for keyboard events
        self.hotkey = keyboard.hook(on_key_event)
        self.hook_active = True
        print("Script is running. Press Ctrl+C to stop.")

        # Keep the script running until stopped
        try:
            while self.running:
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging
        except KeyboardInterrupt:
            print("\nScript stopped.")

    def run(self):
        
        if not self.thread or not self.thread.is_alive():
            print('Starting charisma listener...')
            self.running = True
            self.thread = threading.Thread(target=self.stack)
            self.thread.start()

    def stop(self):
        
        if self.running:
            print('Stopping charisma listener...')
            self.running = False
            
            # Unhook keyboard only if it's active
            if self.hook_active and self.hotkey:
                try:
                    keyboard.unhook(self.hotkey)
                    self.hook_active = False
                except Exception as e:
                    print(f"Warning: Failed to unhook keyboard listener: {e}")
            
            # Stop the thread
            if self.thread and self.thread.is_alive():
                self.thread.join(timeout=1.0)
                if self.thread.is_alive():
                    print("Warning: Thread did not stop cleanly")