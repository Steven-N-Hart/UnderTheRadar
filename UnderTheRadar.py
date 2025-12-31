import tkinter as tk
import pyautogui
import time
import random
import threading
import pystray
from PIL import Image
import sys
import os


class UnderTheRadarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UnderTheRadar")
        self.root.geometry("340x100")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        # Grid Configuration
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Configuration
        self.running = False
        self.MIN_SLEEP = 30
        self.MAX_SLEEP = 120
        self.SAFE_KEYS = ['shift', 'ctrl', 'f15']

        # Resource Path Helper (for bundled assets)
        self.icon_path = self.resource_path(os.path.join("assets", "radar.png"))

        # --- UI Elements ---
        # Start Button Wrapper
        self.start_border = tk.Frame(root, bg="orange", bd=0)
        self.start_border.grid(row=0, column=0, sticky="nsew", padx=10, pady=15)

        self.start_button = tk.Button(
            self.start_border,
            text="▶  START",
            font=("Arial", 11, "bold"),
            bg="black",
            fg="white",
            activebackground="#1a1a1a",
            activeforeground="orange",
            bd=0,
            cursor="hand2",
            command=self.start_pulse
        )
        self.start_button.pack(fill="both", expand=True, padx=2, pady=2)

        # Stop Button Wrapper
        self.stop_border = tk.Frame(root, bg="black", bd=0)
        self.stop_border.grid(row=0, column=1, sticky="nsew", padx=10, pady=15)

        self.stop_button = tk.Button(
            self.stop_border,
            text="■  STOP",
            font=("Arial", 11, "bold"),
            bg="black",
            fg="#444444",
            activebackground="#1a1a1a",
            activeforeground="white",
            bd=0,
            state=tk.DISABLED,
            command=self.stop_pulse
        )
        self.stop_button.pack(fill="both", expand=True, padx=2, pady=2)

        # --- Tray Icon Setup ---
        self.tray_icon = None
        self.root.protocol("WM_DELETE_WINDOW", self.hide_to_tray)

    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def activity_loop(self):
        """Background thread for mouse and keyboard simulation."""
        while self.running:
            action = random.choice(['mouse', 'key'])
            if action == 'mouse':
                x, y = random.randint(-5, 5), random.randint(-5, 5)
                pyautogui.moveRel(x, y, duration=0.2)
            else:
                pyautogui.press(random.choice(self.SAFE_KEYS))

            delay = random.randint(self.MIN_SLEEP, self.MAX_SLEEP)
            for _ in range(delay):
                if not self.running: break
                time.sleep(1)

    def start_pulse(self):
        self.running = True
        self.start_button.config(state=tk.DISABLED, text="● ACTIVE", fg="orange")
        self.start_border.config(bg="black")

        self.stop_button.config(state=tk.NORMAL, fg="white")
        self.stop_border.config(bg="orange")

        thread = threading.Thread(target=self.activity_loop, daemon=True)
        thread.start()

    def stop_pulse(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL, text="▶  START", fg="white")
        self.start_border.config(bg="orange")

        self.stop_button.config(state=tk.DISABLED, fg="#444444")
        self.stop_border.config(bg="black")

    # --- Stealth/Tray Logic ---
    def hide_to_tray(self):
        self.root.withdraw()
        image = Image.open(self.icon_path)
        menu = pystray.Menu(
            pystray.MenuItem("Show", self.show_from_tray),
            pystray.MenuItem("Exit", self.exit_completely)
        )
        self.tray_icon = pystray.Icon("UnderTheRadar", image, "UnderTheRadar", menu)
        threading.Thread(target=self.tray_icon.run, daemon=True).start()

    def show_from_tray(self):
        if self.tray_icon:
            self.tray_icon.stop()
        self.root.after(0, self.root.deiconify)

    def exit_completely(self):
        self.running = False
        if self.tray_icon:
            self.tray_icon.stop()
        self.root.destroy()
        sys.exit()


if __name__ == "__main__":
    pyautogui.FAILSAFE = True
    root = tk.Tk()
    app = UnderTheRadarApp(root)
    root.mainloop()