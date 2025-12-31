import icnsutil
from PIL import Image
import os


def create_icns(source_png, output_icns):
    # 1. Create a temporary folder for the iconset (as required by macOS standards)
    iconset = icnsutil.IcnsFile()

    # 2. Use the library to add the media.
    # For a professional look, it's best to have a 1024x1024 or 512x512 PNG.
    iconset.add_media(file=source_png)

    # 3. Export to ICNS
    iconset.write(output_icns)
    print(f"Success: {output_icns} created.")


if __name__ == "__main__":
    png_path = 'assets/radar.png'
    icns_path = 'assets/radar.icns'

    if os.path.exists(png_path):
        create_icns(png_path, icns_path)
    else:
        print(f"Error: Could not find {png_path}")