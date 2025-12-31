# 📡 UnderTheRadar (v1.0.0)
**Stay Active. Stay Stealthy. Stay Under The Radar.**

`UnderTheRadar` is a cross-platform activity simulator designed to keep your status "Active" by mimicking human behavior through randomized mouse movements and keystrokes. It features a high-contrast "Dark Mode" interface and a stealthy background mode that keeps your workspace clean.

---

## 🚀 Installation

### Windows (No Admin Required)
1.  **Download** the `UnderTheRadar-1.0-win64.msi` installer.
2.  **Run** the installer. It will automatically install the app to your local `AppData` folder to bypass the need for an administrator password.
3.  **Launch** UnderTheRadar from your Desktop or Start Menu.

### macOS (Portable Mode)
1.  **Download** and unzip `UnderTheRadar_Mac.zip`.
2.  **Move** `UnderTheRadar.app` into your **Applications** folder.
3.  **To Launch**: Right-click the app icon and select **Open**. When the warning appears about an "unidentified developer," click **Open** again.

---

## 🛠 Features

* **Hybrid Simulation**: Randomly chooses between subtle mouse "jiggles" and safe keystrokes (like `Shift` or `F15`) to ensure activity is detected by all major monitoring platforms.
* **Stealth Tray Mode**: Closing the window with the **"X"** button hides the app to your System Tray (Windows) or Menu Bar (Mac). It continues running silently in the background.
* **No-Admin Architecture**: Built specifically to be installed and run without requiring IT department permissions.
* **Fail-Safe**: Need to stop it instantly? Move your mouse to any corner of the screen to trigger the "Fail-Safe" and kill the script.

---

## 🎮 How to Use

1.  **START**: Click the orange-bordered **START** button. The border will vanish from Start and appear around Stop, indicating the "Pulse" is active.
2.  **HIDE**: Close the window to move it to the tray/menu bar.
3.  **RESTORE**: Right-click the **Radar Icon** in your tray (bottom right on Windows) or menu bar (top right on Mac) and select **Show**.
4.  **STOP**: Click the **STOP** button to cease all activity.

---

## 📋 Technical Specs

| Detail | Specification |
| :--- | :--- |
| **Language** | Python 3.12 |
| **Libraries** | `pyautogui`, `tkinter`, `pystray`, `Pillow` |
| **Random Interval** | 30 to 120 seconds |
| **Platform** | Windows (MSI) & macOS (App Bundle) |

---

## ⚠️ Disclaimer
*This tool is for educational and simulation purposes only. Use of activity simulators may be subject to your organization's IT policy. Use responsibly.*


How to use this .spec file
## On Windows: 
Run 

```shell
pyinstaller UnderTheRadar.spec
```

It will ignore the BUNDLE section and create UnderTheRadar.exe using the .ico.

## On Mac: 
Run 
```shell
pyinstaller UnderTheRadar.spec 
```
on a Mac computer. It will trigger the BUNDLE section, create UnderTheRadar.app, and use the .icns.