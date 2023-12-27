import os
import shutil

# Define the folder structure you want to create
folders = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf"],
    "Photos": [".jpg", ".jpeg", ".png", ".gif", ".PNG", ".JPG"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi", ".flv", ".mkv", ".ts", ".m4v", ".3gp", ".wmv", ".mov", ".MOV"],
    "Compressed": [".zip", ".rar", ".7z"],
    "Python Files": [".py"],
    "Batch Files": [".bat"]
}

# Get the paths for the source and destination folders from user input
src_folder = input("Enter the path of the source folder: ")
dest_folder = input("Enter the path of the destination folder: ")

# Create the folder structure in the destination folder
for folder in folders:
    folder_path = os.path.join(dest_folder, folder)
    os.makedirs(folder_path, exist_ok=True)

# Move files to the appropriate folders (including subfolders)
for root, dirs, files in os.walk(src_folder):
    for file_name in files:
        src_path = os.path.join(root, file_name)
        if os.path.isfile(src_path):
            for folder_name, extensions in folders.items():
                for extension in extensions:
                    if file_name.endswith(extension):
                        dest_path = os.path.join(dest_folder, folder_name, file_name)
                        shutil.move(src_path, dest_path)
                        break

# Delete empty folders from source folder
for root, dirs, files in os.walk(src_folder, topdown=False):
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)
        if not any(os.scandir(dir_path)):
            os.rmdir(dir_path)

print("File organization complete!")