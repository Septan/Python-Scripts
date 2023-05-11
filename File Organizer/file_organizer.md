# File Organizer

The File Organizer is a Python script that helps you organize files in a source folder by moving them to corresponding folders in a destination folder based on their file extensions.

## Features

- Automatically creates a folder structure in the destination folder based on file extensions.
- Moves files from the source folder to the appropriate destination folder.
- Deletes empty folders from the source folder after the organization process.

## Usage

1. Make sure you have Python installed on your system.

2. Clone this repository or download the `file_organizer.py` script.

3. Open a terminal or command prompt and navigate to the directory where the `file_organizer.py` script is located.

4. Run the script by executing the following command:

   ```shell
   python file_organizer.py

1. Follow the prompts to enter the path of the source folder and the destination folder.

2. The script will organize the files based on their extensions and display a message when the process is complete.

## Customization

To customize the folder structure and file extensions used by the File Organizer, you can modify the `folders` dictionary in the script.

The `folders` dictionary represents the desired folder structure, where each key is a folder name and the corresponding value is a list of file extensions associated with that folder. Add or remove entries as needed to match your requirements.

```
folders = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf"],
    "Photos": [".jpg", ".jpeg", ".png", ".gif"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi", ".flv"],
    "Compressed": [".zip"],
    "Python Files": [".py"],
    "Batch Files": [".bat"]
}
