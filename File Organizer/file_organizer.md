# File Organizer

This is a simple Python script to organize files in a directory based on their last accessed time. It moves files that haven't been accessed in the last 3 months to a new directory. This script can be useful for cleaning up a cluttered directory and making sure that old files are safely stored in a separate location.

## How to use

1. Clone this repository to your local machine
2. Install Python on your machine if it's not already installed
3. Open `file_organizer.py` and edit the following variables to match your requirements:
   - `path`: The path to the directory that you want to organize
   - `new_path`: The path to the directory where you want to move the old files
   - `days`: The number of days after which a file is considered old
   - `ignore_dirs`: A list of directory names to ignore (optional)
4. Run the script by running the command `python file_organizer.py`
5. The script will move all the old files to the specified directory and print out the path of each moved file.
