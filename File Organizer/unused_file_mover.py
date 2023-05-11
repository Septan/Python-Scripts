import os
import shutil
import datetime

# Define the path to search
path = "E:\\"

# Define the path to move the files to
new_path = "E:\\3Months+"

# Define the number of days for which a file should not have been accessed
days = 90

# Define a list of directories to ignore
ignore_dirs = ["PortableApps", "Program Files", "Program Files (x86)", "ProgramData", "SteamLibrary", "SleepyHeadData", "System Volume Information", "Users", "WpSystem", "WindowsApps"]

# Get the current date
today = datetime.datetime.now()

# Loop through the directories and files in the given path
for root, dirs, files in os.walk(path):

    # Check if the current directory should be ignored
    ignore = False
    for dir in ignore_dirs:
        if dir in root:
            ignore = True
            break
    if ignore:
        continue

    # Loop through the files in the current directory
    for file in files:

        # Get the full path of the file
        file_path = os.path.join(root, file)

        # Get the last access time of the file
        last_access_time = os.path.getatime(file_path)

        # Calculate the number of days since the file was last accessed
        days_since_access = (today - datetime.datetime.fromtimestamp(last_access_time)).days

        # Check if the file has not been accessed in the last 3 months
        if days_since_access >= days:

            # Create the new directory if it doesn't already exist
            if not os.path.exists(new_path):
                os.makedirs(new_path)

            # Get the relative path of the file
            rel_path = os.path.relpath(file_path, path)

            # Get the new path of the file
            new_file_path = os.path.join(new_path, rel_path)

            # Create any necessary directories in the new path
            new_file_dir = os.path.dirname(new_file_path)
            if not os.path.exists(new_file_dir):
                os.makedirs(new_file_dir)

            # Move the file to the new path
            shutil.move(file_path, new_file_path)

            print(f"Moved {file_path} to {new_file_path}")
