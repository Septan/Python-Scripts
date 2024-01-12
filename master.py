"""
Script Runner

This script allows the user to select and run various scripts from a list. It supports Python (.py) and Batch (.bat) scripts.

Usage:
1. Run the script.
2. Select a script from the displayed list.
3. The selected script will be executed based on its file extension.

Available Scripts:
1. file_organizer.py - Organizes files in a directory.
2. unused_file_mover.py - Moves unused files to a specified location.
3. meta.py - Processes a batch of mkv files convert to mp4 while adding metadata information.
4. meta_subtitle.py - Same as 3 but adds subtitles.
5. video_hightlight_extractor.py - It extracts highlight clips based on detected scenes, saving them with audio in a specified output folder.
6. frame_extractor.py - Extract frames from video file based on SSIM and PSNR thresholds.

Note: Make sure to have Python installed for Python scripts and FFMPEG for FFMPEG-related scripts.

"""

import os
import subprocess

# Define the available scripts with descriptions
scripts = [
    ("file_organizer.py", "Organizes files in a directory."),
    ("unused_file_mover.py", "Moves unused files to a specified location."),
    ("meta.py", "Processes a batch of mkv files convert to mp4 while adding metadata information."),
    ("meta_subtitle.py", "Same as 3 but adds subtitles."),
    ("video_hightlight_extractor.py", "It extracts highlight clips based on detected scenes, saving them with audio in a specified output folder."),
    ("frame_extractor.py", "Extract frames from video file based on SSIM and PSNR thresholds."),
]

# Prompt the user to select a script
print("Available scripts:")
for index, (script_name, description) in enumerate(scripts, start=1):
    print(f"{index}. {script_name} - {description}")

selected_index = int(input("Enter the number of the script you want to run: "))

# Validate the user's input
if selected_index < 1 or selected_index > len(scripts):
    print("Invalid script selection.")
    exit(1)

# Get the path to the selected script
script_name, _ = scripts[selected_index - 1]
script_path = os.path.join(os.getcwd(), "Scripts", script_name)

# Determine the execution method based on the file extension
file_extension = os.path.splitext(script_path)[1].lower()

if file_extension == ".py":
    # Execute the Python script
    subprocess.call(["python", script_path])
elif file_extension == ".bat":
    # Execute the Batch script
    subprocess.call([script_path])
else:
    print("Unsupported file extension.")