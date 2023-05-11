import os
import subprocess

# Define the available scripts
scripts = [
    "File Organizer/file_organizer.py",
    "File Organizer/unused_file_mover.py",
]

# Prompt the user to select a script
print("Available scripts:")
for index, script_path in enumerate(scripts, start=1):
    script_name = os.path.basename(script_path)
    print(f"{index}. {script_name}")

selected_index = int(input("Enter the number of the script you want to run: "))

# Validate the user's input
if selected_index < 1 or selected_index > len(scripts):
    print("Invalid script selection.")
    exit(1)

# Get the path to the selected script
script_path = os.path.join(os.getcwd(), scripts[selected_index - 1])

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