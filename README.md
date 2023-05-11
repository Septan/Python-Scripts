# Master File

The Master File is a Python script that allows you to select and run different Python scripts, Batch scripts, or executables based on user input. This provides a flexible way to execute various scripts or applications using a single master script.

## Usage

1. Clone or download this repository to your local machine.

2. Ensure that Python is installed on your system. You can download Python from the official Python website: [python.org](https://www.python.org/downloads/).

3. Customize the master file (`master.py`) and add your own Python scripts, Batch scripts, or executables to the `scripts` dictionary. Each script should be associated with a user-friendly name and the respective file path.

4. Run the master file using one of the following methods:

   - **Python**: Open a command prompt or terminal, navigate to the project directory, and run the following command:
     ```
     python master.py
     ```

   - **Batch script**: Double-click the `master.bat` file.

   - **Executable**: If you prefer to create an executable file, you can use tools like PyInstaller to convert the `master.py` script into an executable file. Once created, you can double-click the executable to run the master file.

5. The master file will display a list of available scripts based on the `scripts` dictionary. Enter the number corresponding to the script you want to run and press Enter.

6. The selected script will be executed using the appropriate method (Python, Batch script, or executable) based on the file extension.

## Customization

- **Adding Scripts**: To add new scripts, open the master file (`master.py`) and modify the `scripts` dictionary. Add a new entry with the user-friendly name as the key and the file path of the script as the value.

- **Modifying Scripts**: You can customize each individual script according to your requirements. Edit the respective Python scripts, Batch scripts, or executables to add your desired functionality.



