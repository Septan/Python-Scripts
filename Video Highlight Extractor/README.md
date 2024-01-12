## Script Name: Video Highlight Extractor

### Description
This Python script utilizes the scenedetect library to perform content-aware scene detection on a collection of video files. It extracts highlight clips based on detected scenes, saving them with audio in a specified output folder.

### Usage
1. **Install Dependencies:**
    ```bash
    pip install opencv-python scenedetect tqdm
    ```

2. **Run the Script:**
    ```bash
    python video_highlight_extractor.py
    ```
    Ensure that you replace `video_highlight_extractor.py` with the actual name of your script file.

### Features
- Content-aware scene detection using scenedetect.
- Extraction of highlight clips with audio.
- Supports batch processing of multiple video files.

### How It Works
1. The script scans a specified input folder for video files (`.mp4`).
2. For each video file, it detects scenes using content-aware detection.
3. Detected scenes are saved as separate highlight clips in the specified output folder.

### Requirements
- Python 3.x
- Dependencies: OpenCV, scenedetect, tqdm

### Usage Example
```python
python video_highlight_extractor.py

### Configuration
- Input Folder: `folder_input_path`
- Output Folder: `highlight_clips`