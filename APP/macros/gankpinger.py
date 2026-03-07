import keyboard
import time
import requests
import mss
import json
import os
from PySide6.QtCore import QStandardPaths

class GankPingListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.hotkey = None

    def stack(self, webhook_url, message, takeimage, username, avatar_url, hotkey, monitornumber):
        def send_discord_message(webhook_url, message, takeimage=False, username=None, avatar_url=None):
            # Prepare the payload
            payload = {
                "content": message,
                "username": username if username else None,
                "avatar_url": avatar_url if avatar_url else None
            }
            
            # Remove None values from payload
            payload = {k: v for k, v in payload.items() if v is not None}

            try:
                files = {}
                
                # Handle screenshot
                if takeimage:
                    dataLocation = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
                    sspath = os.path.join(dataLocation, 'screenshot.png')
                    
                    try:
                        monitor = mss.mss().monitors[int(monitornumber)]
                        screenshot = mss.mss().grab(monitor)
                        mss.tools.to_png(screenshot.rgb, screenshot.size, output=sspath)
                        if os.path.exists(sspath):
                            with open(sspath, 'rb') as screenshot:
                                files['file'] = ('screenshot.png', screenshot.read(), 'image/png')
                    except Exception as e:
                        print(f"Error taking screenshot: {str(e)}")
                        return

                # Send request
                if files:
                    response = requests.post(
                        webhook_url,
                        data={'payload_json': json.dumps(payload)},
                        files=files
                    )
                else:
                    response = requests.post(
                        webhook_url,
                        json=payload
                    )
                
                if response.status_code in [200, 204]:
                    print(f"Message sent successfully with status code {response.status_code}")
                else:
                    print(f"Failed to send message. Status code: {response.status_code}")
                    print(f"Response content: {response.text}")

            except Exception as e:
                print(f"Error sending message: {str(e)}")
            finally:
                # Clean up screenqshot if it exists
                if takeimage and os.path.exists(sspath):
                    try:
                        os.remove(sspath)
                    except Exception:
                        pass
        self.hotkey = keyboard.on_press_key(hotkey, lambda e:send_discord_message(webhook_url=webhook_url, message=message, username=username if username else None, avatar_url=avatar_url if avatar_url else None, takeimage=takeimage))

    def run(self, webhook_url, message, username, avatar_url, takeimage, hotkey, monitornumber):
        print('checking')
        if not self.thread or not self.thread.is_alive():
            print('starting ' + (__file__).split("\\")[-1])
            self.running = True
            self.stack(webhook_url=webhook_url, hotkey=hotkey, message=message, username=username, avatar_url=avatar_url, takeimage=takeimage, monitornumber=monitornumber)  # Just call stack directly
            while self.running:  # Keep the thread alive
                time.sleep(0.1)  # Add a small sleep to prevent CPU hogging

    def stop(self):
        self.running = False
        keyboard.unhook(self.hotkey)  # Remove all hotkeys when stopping
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
            if self.thread.is_alive():
                print("Warning: Thread did not stop cleanly")
