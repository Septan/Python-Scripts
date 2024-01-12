import os
import subprocess

# Define the available scripts with descriptions
scripts = [
    ("File Organizer/file_organizer.py", "Organizes files in a directory."),
    ("File Organizer/unused_file_mover.py", "Moves unused files to a specified location."),
    ("MKV to MP4 Converter 1/meta.py", "Processes a batch of mkv files convert to mp4 while adding metadata information."),
    ("MKV to MP4 Converter 2/meta_subtitle.py", "Same as 3 but adds subtitles."),
    ("Video Highlight Extractor/video_hightlight_extractor.py", "It extracts highlight clips based on detected scenes, saving them with audio in a specified output folder."),
    ("Video Frame Extraction Tool/frame_extractor.py", "Extract frames from video file based on SSIM and PSNR thresholds."),
]

# Display available scripts with descriptions
print("Available scripts:")
for index, (script_name, description) in enumerate(scripts, start=1):
    print(f"{index}. {script_name.ljust(30)} - {description}")

# Prompt the user to select a script
selected_index = int(input("\nEnter the number of the script you want to run: "))

# Validate the user's input
if selected_index < 1 or selected_index > len(scripts):
    print("Invalid script selection.")
    exit(1)

# Get the path to the selected script
script_name, _ = scripts[selected_index - 1]
script_path = os.path.normpath(os.path.join(os.getcwd(), "Scripts", script_name))

# Determine the execution method based on the file extension
file_extension = os.path.splitext(script_path)[1].lower()

try:
    if file_extension == ".py":
        # Try executing with 'python'
        subprocess.call(["python", script_path])
    elif file_extension == ".bat":
        # Execute the Batch script
        subprocess.call([script_path])
    else:
        print("Unsupported file extension.")
except FileNotFoundError:
    print("Python interpreter not found. Make sure to have Python installed.")
except Exception as e:
    print(f"Error: {e}")
