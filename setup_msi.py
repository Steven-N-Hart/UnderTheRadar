import sys
from cx_Freeze import setup, Executable

# App metadata
product_name = "UnderTheRadar"

# Ensure the console is hidden
base = "Win32GUI" if sys.platform == "win32" else None

# Build options: include your assets folder and all required libraries
build_exe_options = {
    # Added pystray and PIL (Pillow) to ensure the tray icon works
    "packages": ["pyautogui", "tkinter", "pystray", "PIL"],
    "include_files": ["assets/"]
}

# MSI options: The key to "No Admin" is 'all_users': False
bdist_msi_options = {
    "add_to_path": False,
    "initial_target_dir": f"[AppDataFolder]\\{product_name}",
    "all_users": False,  # Installs for current user only, no admin needed
    "install_icon": "assets/radar.ico",
    "upgrade_code": "{92A57362-D3A6-4893-BC64-8022736C216F}"
}

setup(
    name=product_name,
    version="1.0",
    author="Ghost in the Machine",
    description="Stay Under The Radar",
    options={
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options
    },
    executables=[
        Executable(
            "UnderTheRadar.py",
            base=base,
            icon="assets/radar.ico",
            shortcut_name=product_name,
            shortcut_dir="DesktopFolder",
        )
    ],
)