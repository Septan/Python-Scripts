import os
import sys
import subprocess

def extract_album_art(flac_file):
    try:
        output_path = os.path.join(os.path.dirname(flac_file), 'cover.jpg')
        subprocess.run(['ffmpeg', '-i', flac_file, '-an', '-vcodec', 'copy', output_path], check=True)
        print(f"Album art extracted from {flac_file} and saved to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error processing {flac_file}: {e}")

def main():
    flac_file = input("Enter the path to the FLAC file: ").strip()

    # Remove quotes if present
    if flac_file.startswith('"') and flac_file.endswith('"'):
        flac_file = flac_file[1:-1]

    if not os.path.exists(flac_file) or not flac_file.lower().endswith('.flac'):
        print("Please provide a valid FLAC file.")
        sys.exit(1)

    extract_album_art(flac_file)

if __name__ == "__main__":
    main()
