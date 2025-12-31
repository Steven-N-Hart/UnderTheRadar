import os

# The title of the DMG volume
filename = 'UnderTheRadar_Setup.dmg'
volume_name = 'UnderTheRadar'

# The contents of the DMG
# You must have built the .app bundle with PyInstaller first!
app_path = os.path.join('dist', 'UnderTheRadar.app')
files = [app_path]

# Create a symbolic link to the Applications folder
symlinks = {'Applications': '/Applications'}

# Icon locations
icon_locations = {
    'UnderTheRadar.app': (100, 120),
    'Applications': (300, 120)
}

# Icon for the DMG itself (the drive icon on the desktop)
icon = 'assets/radar.icns'

# Window configuration
window_rect = ((100, 100), (400, 300))
default_view = 'icon-view'
show_status_bar = False
show_tab_view = False
show_toolbar = False