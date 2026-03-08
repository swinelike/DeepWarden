import os
import time
import cv2
import numpy as np
import mss
import keyboard
import threading

# Constants
DETECTION_THRESHOLD = 0.85

# Time-Based Settings
STABILITY_DURATION = 0.15  # Time (seconds) the letters must stay the same to be "confirmed" (waiting for animation to end)
MAX_SCAN_DURATION = 1.0    # Hard limit for scanning before forcing execution
DEFAULT_PING = 100

#1080 x 1920, 125% 
POS_1920_1080_125 = [
    [{"left": 835, "top": 250, "width": 50, "height": 50}, {"left": 835, "top": 300, "width": 50, "height": 50}], # Column 1
    [{"left": 935, "top": 250, "width": 50, "height": 50}, {"left": 935, "top": 300, "width": 50, "height": 50}], # Column 2
    [{"left": 1035, "top": 250, "width": 50, "height": 50}, {"left": 1035, "top": 300, "width": 50, "height": 50}], # Column 3
    [{"left": 1135, "top": 250, "width": 50, "height": 50}, {"left": 1135, "top": 300, "width": 50, "height": 50}]  # Column 4
]
#1200 x 1920, 125%
POS_1920_1200_125 = [
    [{"left": 835, "top": 262, "width": 50, "height": 50}, {"left": 835, "top": 312, "width": 50, "height": 50}], # Column 1
    [{"left": 935, "top": 262, "width": 50, "height": 50}, {"left": 935, "top": 312, "width": 50, "height": 50}], # Column 2
    [{"left": 1035, "top": 262, "width": 50, "height": 50}, {"left": 1035, "top": 312, "width": 50, "height": 50}], # Column 3
    [{"left": 1135, "top": 262, "width": 50, "height": 50}, {"left": 1135, "top": 312, "width": 50, "height": 50}]  # Column 4
]
#1080 x 1920, 100%
POS_1920_1080_100 = [
    [{"left": 858, "top": 217, "width": 50, "height": 50}, {"left": 858, "top": 257, "width": 50, "height": 50}], # Column 1
    [{"left": 938, "top": 217, "width": 50, "height": 50}, {"left": 938, "top": 257, "width": 50, "height": 50}], # Column 2
    [{"left": 1018, "top": 217, "width": 50, "height": 50}, {"left": 1018, "top": 257, "width": 50, "height": 50}], # Column 3
    [{"left": 1098, "top": 217, "width": 50, "height": 50}, {"left": 1098, "top": 257, "width": 50, "height": 50}]  # Column 4
]
#1200 x 1920, 100%
POS_1920_1200_100 = [
    [{"left": 858, "top": 229, "width": 50, "height": 50}, {"left": 858, "top": 269, "width": 50, "height": 50}], # Column 1
    [{"left": 938, "top": 229, "width": 50, "height": 50}, {"left": 938, "top": 269, "width": 50, "height": 50}], # Column 2
    [{"left": 1018, "top": 229, "width": 50, "height": 50}, {"left": 1018, "top": 269, "width": 50, "height": 50}], # Column 3
    [{"left": 1098, "top": 229, "width": 50, "height": 50}, {"left": 1098, "top": 269, "width": 50, "height": 50}]  # Column 4
]

# thanks Wormcave for these resolutions
POS_2560_1440_100 = [ # the placements of the symbols
    [{"left": 1178, "top": 253, "width": 50, "height": 50}, {"left": 1178, "top": 293, "width": 50, "height": 50}], #column 1
    [{"left": 1258, "top": 253, "width": 50, "height": 50}, {"left": 1258, "top": 293, "width": 50, "height": 50}], # column 2
    [{"left": 1338, "top": 253, "width": 50, "height": 50}, {"left": 1338, "top": 293, "width": 50, "height": 50}], # column 3
    [{"left": 1418, "top": 253, "width": 50, "height": 50}, {"left": 1418, "top": 293, "width": 50, "height": 50}] # column 4
]

POS_2560_1440_125 = [ # the placements of the symbols
    [{"left": 1155, "top": 286, "width": 50, "height": 50},{"left": 1155, "top": 336, "width": 50, "height": 50}], #column 1
    [{"left": 1255, "top": 286, "width": 50, "height": 50}, {"left": 1255, "top": 336, "width": 50, "height": 50}], # column 2
    [{"left": 1355, "top": 286, "width": 50, "height": 50}, {"left": 1355, "top": 336, "width": 50, "height": 50}], # column 3
    [{"left": 1455, "top": 286, "width": 50, "height": 50}, {"left": 1455, "top": 336, "width": 50, "height": 50}] # column 4
]









POS_1600_900_125 = [ # the placements of the symbols
       [{"left": 675, "top": 232, "width": 50, "height": 50},
      {"left": 675, "top": 282, "width": 50, "height": 50}], #column 1

    [{"left": 775, "top": 232, "width": 50, "height": 50}, 
     {"left": 775, "top": 282, "width": 50, "height": 50}], # column 2

    [{"left": 875, "top": 232, "width": 50, "height": 50}, 
     {"left": 875, "top": 282, "width": 50, "height": 50}], # column 3

    [{"left": 975, "top": 232, "width": 50, "height": 50}, 
     {"left": 975, "top": 282, "width": 50, "height": 50}] # column 4
]

POS_1600_900_100 = [ # the placements of the symbols
        [{"left": 698, "top": 199, "width": 50, "height": 50},
      {"left": 698, "top": 239, "width": 50, "height": 50}], #column 1

    [{"left": 778, "top": 199, "width": 50, "height": 50}, 
     {"left": 778, "top": 239, "width": 50, "height": 50}], # column 2

    [{"left": 858, "top": 199, "width": 50, "height": 50}, 
     {"left": 858, "top": 239, "width": 50, "height": 50}], # column 3

   [ {"left": 938, "top": 199, "width": 50, "height": 50}, 
     {"left": 938, "top": 239, "width": 50, "height": 50}] # column 4
]

POS_1128_634_100 = [ # the placements of the symbols
      [{"left": 462, "top": 173, "width": 50, "height": 50},
      {"left": 462, "top": 213, "width": 50, "height": 50}], #column 1

    [{"left": 542, "top": 173, "width": 50, "height": 50}, 
     {"left": 542, "top": 213, "width": 50, "height": 50}], # column 2

    [{"left": 622, "top": 173, "width": 50, "height": 50}, 
     {"left": 622, "top": 213, "width": 50, "height": 50}], # column 3

    [{"left": 702, "top": 173, "width": 50, "height": 50}, 
     {"left": 702, "top": 213, "width": 50, "height": 50}] # column 4
] 
# According to Wormcave, there is no 125 option so we will leave it as is for now
POS_1128_634_125 = [ # the placements of the symbols
      [{"left": 462, "top": 173, "width": 50, "height": 50},
      {"left": 462, "top": 213, "width": 50, "height": 50}], #column 1

    [{"left": 542, "top": 173, "width": 50, "height": 50}, 
     {"left": 542, "top": 213, "width": 50, "height": 50}], # column 2

    [{"left": 622, "top": 173, "width": 50, "height": 50}, 
     {"left": 622, "top": 213, "width": 50, "height": 50}], # column 3

    [{"left": 702, "top": 173, "width": 50, "height": 50}, 
     {"left": 702, "top": 213, "width": 50, "height": 50}] # column 4
] 

POS_1600_1200_125 = [ # the placements of the symbols
       [{"left": 675, "top": 262, "width": 50, "height": 50},
      {"left": 675, "top": 312, "width": 50, "height": 50}], #column 1

    [{"left": 775, "top": 262, "width": 50, "height": 50}, 
     {"left": 775, "top": 312, "width": 50, "height": 50}], # column 2

    [{"left": 875, "top": 262, "width": 50, "height": 50}, 
     {"left": 875, "top": 312, "width": 50, "height": 50}], # column 3

    [{"left": 975, "top": 262, "width": 50, "height": 50}, 
     {"left": 975, "top": 312, "width": 50, "height": 50}] # column 4

]

POS_1600_1200_100 = [ # the placements of the symbols
       [{"left": 698, "top": 229, "width": 50, "height": 50},
      {"left": 698, "top": 269, "width": 50, "height": 50}], #column 1

    [{"left": 778, "top": 229, "width": 50, "height": 50}, 
     {"left": 778, "top": 269, "width": 50, "height": 50}], # column 2

    [{"left": 858, "top": 229, "width": 50, "height": 50}, 
     {"left": 858, "top": 269, "width": 50, "height": 50}], # column 3

    [{"left": 938, "top": 229, "width": 50, "height": 50}, 
     {"left": 938, "top": 269, "width": 50, "height": 50}] # column 4

]

POS_3440_1440_125 = [ # the placements of the symbols
     [ {"left": 1595, "top": 286, "width": 50, "height": 50},
      {"left": 1595, "top": 336, "width": 50, "height": 50}], #column 1

    [{"left": 1695, "top": 286, "width": 50, "height": 50}, 
     {"left": 1695, "top": 336, "width": 50, "height": 50}], # column 2

   [ {"left": 1795, "top": 286, "width": 50, "height": 50}, 
     {"left": 1795, "top": 336, "width": 50, "height": 50}], # column 3

    [{"left": 1895, "top": 286, "width": 50, "height": 50}, 
     {"left": 1895, "top": 336, "width": 50, "height": 50}] # column 4
]


POS_3440_1440_100 = [ # the placements of the symbols
      [{"left": 1618, "top": 253, "width": 50, "height": 50},
      {"left": 1618, "top": 293, "width": 50, "height": 50}], #column 1

    [{"left": 1698, "top": 253, "width": 50, "height": 50}, 
     {"left": 1698, "top": 293, "width": 50, "height": 50}], # column 2

    [{"left": 1778, "top": 253, "width": 50, "height": 50}, 
     {"left": 1778, "top": 293, "width": 50, "height": 50}], # column 3

    [{"left": 1858, "top": 253, "width": 50, "height": 50}, 
     {"left": 1858, "top": 293, "width": 50, "height": 50}] # column 4
]

POS_2560_1080_125 = [ # the placements of the symbols
      [{"left": 1155, "top": 250, "width": 50, "height": 50},
      {"left": 1155, "top": 300, "width": 50, "height": 50}], #column 1

      [{"left": 1255, "top": 250, "width": 50, "height": 50}, 
     {"left": 1255, "top": 300, "width": 50, "height": 50}], # column 2

    [{"left": 1355, "top": 250, "width": 50, "height": 50}, 
     {"left": 1355, "top": 300, "width": 50, "height": 50}], # column 3

    [{"left": 1455, "top": 250, "width": 50, "height": 50}, 
     {"left": 1455, "top": 300, "width": 50, "height": 50}] # column 4
]

POS_2560_1080_100 = [ # the placements of the symbols
      [{"left": 1178, "top": 217, "width": 50, "height": 50},
      {"left": 1178, "top": 257, "width": 50, "height": 50}], #column 1

    [{"left": 1258, "top": 217, "width": 50, "height": 50}, 
     {"left": 1258, "top": 257, "width": 50, "height": 50}], # column 2

    [{"left": 1338, "top": 217, "width": 50, "height": 50}, 
     {"left": 1338, "top": 257, "width": 50, "height": 50}], # column 3

    [{"left": 1418, "top": 217, "width": 50, "height": 50}, 
     {"left": 1418, "top": 257, "width": 50, "height": 50}] # column 4
]

POS_1366_768_100 = [
    [{"left": 556, "top": 167, "width": 80, "height": 80},
     {"left": 562, "top": 215, "width": 80, "height": 80}],

    [{"left": 640, "top": 164, "width": 80, "height": 80},
     {"left": 644, "top": 218, "width": 80, "height": 80}],

    [{"left": 720, "top": 164, "width": 80, "height": 80},
     {"left": 722, "top": 212, "width": 80, "height": 80}],

    [{"left": 802, "top": 160, "width": 80, "height": 80},
     {"left": 801, "top": 217, "width": 80, "height": 80}]
]

POS_1366_768_125 = [
    [{"left": 421, "top": 157, "width": 80, "height": 80},
     {"left": 429, "top": 194, "width": 80, "height": 80}],

    [{"left": 504, "top": 156, "width": 80, "height": 80},
     {"left": 506, "top": 196, "width": 80, "height": 80}],

    [{"left": 583, "top": 157, "width": 80, "height": 80},
     {"left": 586, "top": 194, "width": 80, "height": 80}],

    [{"left": 670, "top": 158, "width": 80, "height": 80},
     {"left": 670, "top": 196, "width": 80, "height": 80}]
]
positions100 = [POS_1128_634_100, POS_1366_768_100, POS_1600_900_100, POS_1600_1200_100, POS_1920_1080_100, POS_1920_1200_100, POS_2560_1080_100, POS_2560_1440_100, POS_3440_1440_100]
positions125 = [POS_1128_634_125, POS_1366_768_125, POS_1600_900_125, POS_1600_1200_125, POS_1920_1080_125, POS_1920_1200_125, POS_2560_1080_125, POS_2560_1440_125, POS_3440_1440_125]



class RitualCastListener:  
    def __init__(self):
        self.running = False
        self.thread = None
        self.templates = {}


    def load_templates(self, filepath):
        if not os.path.isdir(filepath):
            print(f"ERROR: Template folder not found at: {filepath}")
            return False

        count = 0
        for f in os.listdir(filepath):
            if not f.endswith('.png') or f == 'background.png':
                continue
            
            name = os.path.splitext(f)[0]
            char = None
            for c in reversed(name):
                if c.isalpha():
                    char = c.upper()
                    break
            
            if char:
                path = os.path.join(filepath, f)
                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    self.templates[char] = img
                    count += 1
        
        if count == 0:
            print("ERROR: No .png templates found!")
            return False
        
        print(f"Loaded {count} templates.")
        return True

    def grab_regions(self, sct):
        for i, roi in enumerate(self.flat_regions):
            img = np.array(sct.grab(roi))
            if img.ndim == 3 and img.shape[2] == 4:
                img = img[:, :, :3]
            self.current_images[i] = img

    def detect_letter(self, region_img, template_list):
        best_letter = None
        best_score = 0.0
        
        region_gray = cv2.cvtColor(region_img, cv2.COLOR_BGR2GRAY)
        if np.mean(region_gray) < 10: 
            return None, 0.0

        for letter, template in template_list:
            if template.shape[0] > region_gray.shape[0] or template.shape[1] > region_gray.shape[1]:
                continue

            res = cv2.matchTemplate(region_gray, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, _ = cv2.minMaxLoc(res)

            if max_val > best_score and max_val >= DETECTION_THRESHOLD:
                best_score = max_val
                best_letter = letter

        return best_letter, best_score

    def scan_cycle(self, sct, template_list):
        self.grab_regions(sct)
        current_findings = [None] * 4
        
        for col_idx in range(4):
            top_idx = col_idx * 2
            bot_idx = top_idx + 1
            
            l_top, s_top = self.detect_letter(self.current_images[top_idx], template_list)
            l_bot, s_bot = self.detect_letter(self.current_images[bot_idx], template_list)
            
            if l_top and l_bot:
                current_findings[col_idx] = l_top if s_top >= s_bot else l_bot
            elif l_top:
                current_findings[col_idx] = l_top
            elif l_bot:
                current_findings[col_idx] = l_bot
            else:
                current_findings[col_idx] = None

        return current_findings

    def is_sequence_valid(self, sequence):
        gap_found = False
        has_content = False
        
        for item in sequence:
            if item is None:
                gap_found = True
            else:
                has_content = True
                if gap_found:
                    return False # Found a letter after a gap like [X, None, C, V]
        return has_content

    def perform_macro_cycle(self, sct, template_list, ping_ms):
        accumulated_slots = [None] * 4
        
        # Stability tracking
        last_change_time = time.time()
        start_scan_time = time.time()
        
        while True:
            if not self.running:
                return

            # execute after max duration reached
            if (time.time() - start_scan_time) > MAX_SCAN_DURATION:
                #p print("Hard timeout reached")
                break


            scan_result = self.scan_cycle(sct, template_list)
            
            # Detected/found letters are stored here
            changed = False
            for i in range(4):
                if accumulated_slots[i] is None and scan_result[i] is not None:
                    accumulated_slots[i] = scan_result[i]
                    changed = True

            # check if the letters changed
            if changed:
                last_change_time = time.time()
            else:
                # if letters are detected, check how long it's been stable 
                if any(accumulated_slots):
                    if (time.time() - last_change_time) > STABILITY_DURATION:
                        #p print("DEBUG: Stability reached!")
                        break

            # exit immediately if 4 are found
            if None not in accumulated_slots:
                break
            
            time.sleep(0.005)

        if self.is_sequence_valid(accumulated_slots):
            final_sequence = [char for char in accumulated_slots if char is not None]
            print(f"Sequence: {''.join(final_sequence)}")
            
            key_delay = 0.02 + (int(ping_ms) * 0.001)
            for char in final_sequence:
                k = char.lower()
                time.sleep(key_delay)
                keyboard.press(k)
                time.sleep(0.04)
                keyboard.release(k)
                print(f"Pressed: {k}")
            
            # Wait a bit before scanning again to avoid double-typing the same instance
            time.sleep(0.2)
        else:
            time.sleep(0.05)

    def stack(self, ping_ms, filepath):
        print(f"Ping: {ping_ms}ms")
        if not self.load_templates(filepath):
            self.running = False
            return

        with mss.mss() as sct:
            template_list = list(self.templates.items())
            while self.running:
                try:
                    self.perform_macro_cycle(sct, template_list, ping_ms)
                except Exception as e:
                    print(f"Error: {e}")
                    time.sleep(0.5)

    def run(self, basepath, ping_ms, resolution, scale):

        if scale == 0: #scale 100
            filepath = os.path.join(basepath, '100')
            column_regions = positions100[resolution]
        elif scale == 1:
            filepath = os.path.join(basepath, '125')
            column_regions = positions125[resolution]
            
        
        self.flat_regions = [r for col in column_regions for r in col]
        self.current_images = [None] * len(self.flat_regions)
        if ping_ms is None or not str(ping_ms).isdigit():
            ping_ms = DEFAULT_PING
            
        if not self.thread or not self.thread.is_alive():
            self.running = True
            self.thread = threading.Thread(target=self.stack, args=(ping_ms, filepath))
            self.thread.daemon = True
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join(timeout=1.0)