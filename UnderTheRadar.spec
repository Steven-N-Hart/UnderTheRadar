# -*- mode: python ; coding: utf-8 -*-
import sys
import os

block_cipher = None
is_mac = sys.platform == 'darwin'

# Choose the correct icon based on the OS
icon_file = os.path.join('assets', 'radar.icns' if is_mac else 'radar.ico')

a = Analysis(
    ['UnderTheRadar.py'],
    pathex=[],
    binaries=[],
    datas=[('assets', 'assets')], # Ensures assets folder is included
    hiddenimports=['pystray', 'PIL._tkinter_finder'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='UnderTheRadar',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False, # Hides the terminal
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_file, # Uses the conditional icon
)

# Mac-Specific App Bundle logic
if is_mac:
    app = BUNDLE(
        exe,
        name='UnderTheRadar.app',
        icon=icon_file,
        bundle_identifier='com.statusquo.undertheradar',
        info_plist={
            'LSUIElement': True, # This hides the app from the Dock (Menu Bar only)
        },
    )