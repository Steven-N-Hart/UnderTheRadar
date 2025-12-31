from PIL import Image

# Path to your existing png
img = Image.open('assets/radar.png')

# Define the standard Windows icon sizes
icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

# Save as ICO with all sizes included
img.save('assets/radar.ico', sizes=icon_sizes)
print("Success: assets/radar.ico created with multiple resolutions.")